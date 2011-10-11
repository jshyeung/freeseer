#!/usr/bin/python
# -*- coding: utf-8 -*-

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

@author: Thanh Ha
'''

from PyQt4 import QtCore, QtGui

class LoggerWidget(QtGui.QWidget):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        QtGui.QWidget.__init__(self, parent)
        
        self.mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.mainLayout)
        
        
        # Console Logger
        self.consoleLoggerGroupBox = QtGui.QGroupBox()
        self.consoleLoggerGroupBox.setTitle(self.tr("Console Logger"))
        self.consoleLoggerGroupBox.setCheckable(True)
        self.consoleLoggerFormLayout = QtGui.QFormLayout()
        self.consoleLoggerGroupBox.setLayout(self.consoleLoggerFormLayout)
        self.mainLayout.addWidget(self.consoleLoggerGroupBox)
        
        self.consoleLoggerLevelLabel = QtGui.QLabel(self.tr("Log Level"))
        self.consoleLoggerLevelComboBox = QtGui.QComboBox()
        self.consoleLoggerFormLayout.addRow(self.consoleLoggerLevelLabel, 
                                            self.consoleLoggerLevelComboBox)
        # --- End Console Logger
        
        # Syslog Logger
        self.syslogLoggerGroupBox = QtGui.QGroupBox()
        self.syslogLoggerGroupBox.setTitle(self.tr("Syslog Logger"))
        self.syslogLoggerGroupBox.setCheckable(True)
        self.syslogLoggerFormLayout = QtGui.QFormLayout()
        self.syslogLoggerGroupBox.setLayout(self.syslogLoggerFormLayout)
        self.mainLayout.addWidget(self.syslogLoggerGroupBox)
        
        self.syslogLoggerLevelLabel = QtGui.QLabel(self.tr("Log Level"))
        self.syslogLoggerLevelComboBox = QtGui.QComboBox()
        self.syslogLoggerFormLayout.addRow(self.syslogLoggerLevelLabel, 
                                            self.syslogLoggerLevelComboBox)
        # --- End Syslog Logger
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    main = LoggerWidget()
    main.show()
    sys.exit(app.exec_())