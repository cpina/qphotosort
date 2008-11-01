# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created: Sat Nov  1 18:34:07 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_help(object):
    def setupUi(self, help):
        help.setObjectName("help")
        help.resize(313,249)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(help.sizePolicy().hasHeightForWidth())
        help.setSizePolicy(sizePolicy)
        help.setMinimumSize(QtCore.QSize(0,0))
        help.setMaximumSize(QtCore.QSize(9999999,9999999))
        help.setModal(True)
        self.gridlayout = QtGui.QGridLayout(help)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.exit = QtGui.QPushButton(help)
        self.exit.setMinimumSize(QtCore.QSize(70,0))
        icon = QtGui.QIcon()
        icon.addFile(":/icons/button_ok.png")
        self.exit.setIcon(icon)
        self.exit.setObjectName("exit")
        self.gridlayout.addWidget(self.exit,1,1,1,1)
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem,1,0,1,1)
        self.frame = QtGui.QGroupBox(help)
        self.frame.setObjectName("frame")
        self.text = QtGui.QLabel(self.frame)
        self.text.setGeometry(QtCore.QRect(10,20,321,401))
        self.text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text.setWordWrap(True)
        self.text.setObjectName("text")
        self.gridlayout.addWidget(self.frame,0,0,1,2)

        self.retranslateUi(help)
        QtCore.QObject.connect(self.exit,QtCore.SIGNAL("clicked()"),help.close)
        QtCore.QMetaObject.connectSlotsByName(help)

    def retranslateUi(self, help):
        help.setWindowTitle(QtGui.QApplication.translate("help", "Form1", None, QtGui.QApplication.UnicodeUTF8))
        self.exit.setText(QtGui.QApplication.translate("help", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setTitle(QtGui.QApplication.translate("help", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.text.setText(QtGui.QApplication.translate("help", "\n"
"as\n"
"df\n"
"asdf\n"
"sa\n"
"dfa\n"
"sdf\n"
"asd\n"
"f", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
