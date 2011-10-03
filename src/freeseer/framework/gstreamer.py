#!/usr/bin/python
# -*- coding: utf-8 -*-

# freeseer - vga/presentation capture software
#
#  Copyright (C) 2011  Free and Open Source Software Learning Centre
#  http://fosslc.org
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For support, questions, suggestions or any other inquiries, visit:
# http://wiki.github.com/fosslc/freeseer/

import logging
import sys
import gobject
gobject.threads_init()
import pygst
pygst.require("0.10")
import gst


class Gstreamer:
    def __init__(self, window_id=None, audio_feedback=None):
        self.window_id = window_id
        self.audio_feedback_event = audio_feedback
        
        self.record_audio = False
        self.record_video = False
        
        # Initialize Player
        self.player = gst.Pipeline('player')
        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect('message', self.on_message)
        bus.connect('sync-message::element', self.on_sync_message)
        
        # Initialize Entry Points
        self.audio_tee = gst.element_factory_make('tee', 'audio_tee')
        self.video_tee = gst.element_factory_make('tee', 'video_tee')
        self.player.add(self.audio_tee, self.video_tee)
        
        logging.debug("Gstreamer initialized.")

    ##
    ## GST Player Functions
    ##
    def on_message(self, bus, message):
        t = message.type
      
        if t == gst.MESSAGE_EOS:
            self.stop()
            pass
        elif t == gst.MESSAGE_ERROR:
            err, debug = message.parse_error()
            #self.core.logger.log.debug('Error: ' + str(err) + str(debug))
            #self.player.set_state(gst.STATE_NULL)
            #self.stop()

        elif message.structure is not None:
            s = message.structure.get_name()

            if s == 'level':
                msg = message.structure.to_string()
                rms_dB = float(msg.split(',')[6].split('{')[1].rstrip('}'))
                
                # This is an inaccurate representation of decibels into percent
                # conversion, this code should be revisited.
                try:
                    percent = (int(round(rms_dB)) + 50) * 2
                except OverflowError:
                    percent = 0
                self.audio_feedback_event(percent)
            
    def on_sync_message(self, bus, message):
        if message.structure is None:
            return
        message_name = message.structure.get_name()
        if message_name == 'prepare-xwindow-id':
            imagesink = message.src
            if sys.platform != 'darwin': ## OSX does not support force-aspect-ratio
                imagesink.set_property('force-aspect-ratio', True)
            imagesink.set_xwindow_id(int(self.window_id))
            logging.debug("Preview loaded into window.")
            
    def keyboard_event(self, key):
        """
        Keyboard event handler.
        """
        pass
            
    ##
    ## Recording functions
    ##
    def record(self):
        """
        Start recording.
        """
        self.player.set_state(gst.STATE_PLAYING)
        logging.debug("Recording started.")
    
    def stop(self):
        """
        Stop recording.
        """
        self.player.set_state(gst.STATE_NULL)
        
        # Unlink Audio plugins
        if self.record_audio is True:
            for plugin in self.audio_input_plugins:
                gst.element_unlink_many(self.audio_tee, plugin)
                self.player.remove(plugin)
        
            gst.element_unlink_many(self.audiomixer, self.audio_tee)
            self.player.remove(self.audiomixer)
        
        # Unlink Video plugins
        if self.record_video is True:
            for plugin in self.video_input_plugins:
                gst.element_unlink_many(self.video_tee, plugin)
                self.player.remove(plugin)
            
            gst.element_unlink_many(self.videomixer, self.video_tee)
            self.player.remove(self.videomixer)
            
        for plugin in self.output_plugins:
            gst.element_unlink_many(self.video_tee, plugin)
            self.player.remove(plugin)
        
        logging.debug("Recording stopped.")
    
    def load_output_plugins(self, plugins, metadata):
        self.output_plugins = []
        for plugin in plugins:
            type = plugin.get_type()
            bin = plugin.get_output_bin(metadata)
            self.output_plugins.append(bin)
            
            if type == "audio":
                self.player.add(bin)
                self.audio_tee.link(bin)
            elif type == "video":
                self.player.add(bin)
                self.video_tee.link(bin)
            elif type == "both":
                self.player.add(bin)
                self.audio_tee.link_pads("src%d", bin, "audiosink")                
                self.video_tee.link_pads("src%d", bin, "videosink")
    
    def load_audiomixer(self, mixer, inputs):
        self.record_audio = True
        self.audio_input_plugins = []
        
        self.audiomixer = mixer.get_audiomixer_bin()
        self.player.add(self.audiomixer)
        self.audiomixer.link(self.audio_tee)
        
        self.audio_input_plugins = mixer.load_inputs(self.player, self.audiomixer, inputs)

    def load_videomixer(self, mixer, inputs):
        self.record_video = True
        self.video_input_plugins = []
        
        self.videomixer = mixer.get_videomixer_bin()
        self.player.add(self.videomixer)
        self.videomixer.link(self.video_tee)
        
        self.video_input_plugins = mixer.load_inputs(self.player, self.videomixer, inputs)
