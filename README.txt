==========================================================================

The Freeseer project is a powerful software suite for capturing or
streaming video. 

It enables you to capture great presentations, demos, training material, 
and other videos. It handles desktop screen-casting with ease.
 
It is one of a few such tools that can also record vga output or video
from external sources such as firewire, usb, s-video, or rca.

It is particularly good at handling very large conferences with hundreds 
of talks and speakers using varied hardware and operating systems.

Freeseer itself can run on commodity hardware such as a laptop or desktop.
It is supported on Windows, and Linux, It will support MacOS soon.
 
Freeseer is written in Python, and uses Qt4 for its
GUI. It also uses Gstreamer for video/audio processing.

Freeseer is licensed under the GPL license, version 3.
http://www.fsf.org/licensing/licenses/gpl.html

Freeseer supports free (royalty free) audio and video codecs.

-------------------------------------------------------------------------

Download the latest installers: https://github.com/Freeseer/freeseer/downloads

Download the latest source code: https://github.com/Freeseer/freeseer

-------------------------------------------------------------------------

You can install Freeseer from binary packages. Visit our download site
if you would like to do so.

To develop and run freeseer, you require:
    Make, Git, Python 2.6, PyQT development tools

For Fedora Linux, install:
--------------------------
    “sudo yum install git make PyQt4-devel python-feedparser.noarch python-setuptools”    

For Ubuntu Linux, install:
--------------------------
    “sudo apt-get install build-essential qt4-qmake pyqt4-dev-tools cmake \
    libqt4-dev python-qt4 python-qt4-dev python2.6-dev python-feedparser”

For Windows, install: 
---------------------
    python-2.6.6, GStreamer-WinBuilds-GPL-x86, GStreamer-WinBuilds-SDK-GPL-x86, PyQt-Py2.6-x86-gpl-4.8.3-1, 
    pygtk-all-in-one-2.22.6.win32-py2.6, feedparser-5.0.1, cmake: cmake-2.8.4-win32-x86 mingw-get-inst-20110316
    
    NOTES: The above software versions are known to work well. Python does need to be version 2.6.*

          On windows, add the following paths to your PATH variable:
          C:\Python26;C:\Python26\Lib\site-packages\PyQt4\bin;C:\MinGW\bin

-------------------------------------------------------------------------

Once you have the prerequisite components, build freeseer by changing
directory into the freeseer directory (above src directory), and run:

$ ( mkdir -p build; cd build; cmake .. )

    NOTE: If you are running on windows you will need an additional option
          for cmake to work. You can run 'cmake -G "MinGW Makefiles" ..'

This will compile the gui files. Once this completes, you can then:

$ src/freeseer-record

This starts up the Freeseer recording tool GUI.

If you would like to create packages, read PACKAGE.txt for instructions.

--------------------------------------------------------------------------

Read more about hardware capture options here: 
    http://wiki.github.com/Freeseer/freeseer/capture-hardware

If you wish to capture vga input using epiphan's vga2usb device:
    first, copy the vga2usb.ko driver to /lib/modules/<kernel version>
    for the kernel you're running. Epiphan provides a list of pre-compiled
    drivers at http://epiphan.com

    Then, configure the driver:
    "sudo cp vga2usb.conf /etc/modprobe.d/; depmod -a"

For support, questions, suggestions or any other inquiries, visit:
    http://wiki.github.com/Freeseer/freeseer/
  
==========================================================================
