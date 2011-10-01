import pygst
pygst.require("0.10")
import gst

from freeseer.framework.plugin import IVideoInput

class USBSrc(IVideoInput):
    name ="Desktop-OSX Source"
    
    def get_videoinput_bin(self):
        bin = gst.Bin(self.name)
        
        ##replace first argument with what ever the source is
        videosrc = gst.element_factory_make("", "videosrc")
        bin.add(videosrc)
        
        # Setup ghost pad
        pad = videosrc.get_pad("src")
        ghostpad = gst.GhostPad("videosrc", pad)
        bin.add_pad(ghostpad)
        
        return bin
