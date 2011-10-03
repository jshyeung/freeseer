'''
freeseer - vga/presentation capture software

Copyright (C) 2011  Free and Open Source Software Learning Centre
http://fosslc.org

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

For support, questions, suggestions or any other inquiries, visit:
http://wiki.github.com/fosslc/freeseer/

@author: Joseph Yeung
'''

import pygst
pygst.require("0.10")
import gst

from freeseer.framework.plugin import IVideoInput

class USBSrc(IVideoInput):
    name ="ISight-OSX Source"
    
    def get_videoinput_bin(self):
        bin = gst.Bin(self.name)
        
        ## replace first argument with what ever the source is
        videosrc = gst.element_factory_make("qtkitvideosrc", "videosrc")
        bin.add(videosrc)
        
        # Setup ghost pad
        pad = videosrc.get_pad("src")
        ghostpad = gst.GhostPad("videosrc", pad)
        bin.add_pad(ghostpad)
        
        return bin
