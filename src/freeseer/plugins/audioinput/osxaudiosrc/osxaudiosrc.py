import pygst
pygst.require("0.10")
import gst

from freeseer.framework.plugin import IAudioInput

class PulseSrc(IAudioInput):
    name = "OSX Audio Source"
    
    def get_audioinput_bin(self):
        bin = gst.Bin(self.name)
        
        #replace first argument with what ever OSX uses
        audiosrc = gst.element_factory_make("", "audiosrc")
        bin.add(audiosrc)
        
        # Setup ghost pad
        pad = audiosrc.get_pad("src")
        ghostpad = gst.GhostPad("audiosrc", pad)
        bin.add_pad(ghostpad)
        
        return bin
