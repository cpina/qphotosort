# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Sat Nov  1 18:34:07 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(410,340)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(144)
        sizePolicy.setVerticalStretch(232)
        sizePolicy.setHeightForWidth(about.sizePolicy().hasHeightForWidth())
        about.setSizePolicy(sizePolicy)
        about.setMinimumSize(QtCore.QSize(410,340))
        about.setMaximumSize(QtCore.QSize(410,340))
        about.setModal(False)
        self.layoutWidget = QtGui.QWidget(about)
        self.layoutWidget.setGeometry(QtCore.QRect(21,21,371,301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridlayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtGui.QSpacerItem(281,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem,1,0,1,1)
        self.Ok = QtGui.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addFile(":/icons/close.png")
        self.Ok.setIcon(icon)
        self.Ok.setObjectName("Ok")
        self.gridlayout.addWidget(self.Ok,1,1,1,1)
        self.tabWidget2 = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget2.setObjectName("tabWidget2")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.textLabel1 = QtGui.QLabel(self.tab)
        self.textLabel1.setGeometry(QtCore.QRect(30,55,291,141))
        self.textLabel1.setScaledContents(False)
        self.textLabel1.setWordWrap(True)
        self.textLabel1.setObjectName("textLabel1")
        self.versio = QtGui.QLabel(self.tab)
        self.versio.setGeometry(QtCore.QRect(110,30,131,20))
        self.versio.setTextFormat(QtCore.Qt.AutoText)
        self.versio.setAlignment(QtCore.Qt.AlignCenter)
        self.versio.setObjectName("versio")
        self.tabWidget2.addTab(self.tab,"")
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName("tab1")
        self.textLabel2 = QtGui.QLabel(self.tab1)
        self.textLabel2.setGeometry(QtCore.QRect(50,20,261,151))
        self.textLabel2.setWordWrap(True)
        self.textLabel2.setObjectName("textLabel2")
        self.tabWidget2.addTab(self.tab1,"")
        self.TabPage = QtGui.QWidget()
        self.TabPage.setObjectName("TabPage")
        self.textLabel3 = QtGui.QLabel(self.TabPage)
        self.textLabel3.setGeometry(QtCore.QRect(28,22,290,151))
        self.textLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.textLabel3.setWordWrap(True)
        self.textLabel3.setObjectName("textLabel3")
        self.tabWidget2.addTab(self.TabPage,"")
        self.gridlayout.addWidget(self.tabWidget2,0,0,1,2)

        self.retranslateUi(about)
        self.tabWidget2.setCurrentIndex(0)
        QtCore.QObject.connect(self.Ok,QtCore.SIGNAL("clicked()"),about.close)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        about.setWindowTitle(QtGui.QApplication.translate("about", "About qphotosort", None, QtGui.QApplication.UnicodeUTF8))
        self.Ok.setText(QtGui.QApplication.translate("about", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel1.setText(QtGui.QApplication.translate("about", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Integral application to manage photos (merge directories, resize, rotate, renumearte)</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">More information in: </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.catalandictionary.org\"><span style=\" text-decoration: underline; color:#0000ff;\">http://pintant.cat/qphotosort</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.versio.setText(QtGui.QApplication.translate("about", "Version 1Beta", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab), QtGui.QApplication.translate("about", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel2.setText(QtGui.QApplication.translate("about", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Carles Pina i Estany. 2006.</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Suggestions, patches, ideas, photos :-), etc. to <a href=\"mailto:carles@pina.cat\"><span style=\" text-decoration: underline; color:#0000ff;\">carles@pina.cat</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab1), QtGui.QApplication.translate("about", "Authors", None, QtGui.QApplication.UnicodeUTF8))
        self.textLabel3.setText(QtGui.QApplication.translate("about", "Program is licensed in GPL 2.0 or later\n"
"\n"
"Other needed programs or modules are also free", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.TabPage), QtGui.QApplication.translate("about", "License", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
