# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Wed Jun  5 21:07:08 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Spellcheck(object):
    def setupUi(self, Spellcheck):
        Spellcheck.setObjectName(_fromUtf8("Spellcheck"))
        Spellcheck.resize(688, 481)
        self.centralwidget = QtGui.QWidget(Spellcheck)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        Spellcheck.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Spellcheck)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Spellcheck.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Spellcheck)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Spellcheck.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Spellcheck)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Spellcheck.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew = QtGui.QAction(Spellcheck)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(Spellcheck)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(Spellcheck)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(Spellcheck)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionCut = QtGui.QAction(Spellcheck)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(Spellcheck)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(Spellcheck)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionUpdate = QtGui.QAction(Spellcheck)
        self.actionUpdate.setObjectName(_fromUtf8("actionUpdate"))
        self.actionAbout = QtGui.QAction(Spellcheck)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Spellcheck)
        QtCore.QMetaObject.connectSlotsByName(Spellcheck)

    def retranslateUi(self, Spellcheck):
        Spellcheck.setWindowTitle(QtGui.QApplication.translate("Spellcheck", "Nepali SpellChecker v2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Spellcheck", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("Spellcheck", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("Spellcheck", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("Spellcheck", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("Spellcheck", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("Spellcheck", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("Spellcheck", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("Spellcheck", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("Spellcheck", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("Spellcheck", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("Spellcheck", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate.setText(QtGui.QApplication.translate("Spellcheck", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("Spellcheck", "About", None, QtGui.QApplication.UnicodeUTF8))
