# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Sat Jun 29 00:31:10 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QTextEdit
from PyQt4.QtCore import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class MyTextEdit(QTextEdit):
    mousePressedSignal = pyqtSignal(QPoint)
    def __init__(self, *args):
        QTextEdit.__init__(self, *args)

    def mousePressEvent(self, event):
        pos = event.pos()
        self.mousePressedSignal.emit(pos)
                
class Ui_Spellcheck(object):
    def setupUi(self, Spellcheck):
        Spellcheck.setObjectName(_fromUtf8("Spellcheck"))
        Spellcheck.resize(671, 481)
        Spellcheck.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/mpplogo.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Spellcheck.setWindowIcon(icon)
        Spellcheck.setWindowOpacity(1.0)
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
        self.textEdit = MyTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.Bugwidget = QtGui.QWidget(self.centralwidget)
        self.Bugwidget.setObjectName(_fromUtf8("Bugwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Bugwidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.Bugwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.BugType = QtGui.QLineEdit(self.Bugwidget)
        self.BugType.setObjectName(_fromUtf8("BugType"))
        self.gridLayout_2.addWidget(self.BugType, 0, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.Bugwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.ReportButton = QtGui.QPushButton(self.Bugwidget)
        self.ReportButton.setObjectName(_fromUtf8("ReportButton"))
        self.gridLayout_2.addWidget(self.ReportButton, 0, 4, 1, 1)
        self.label_7 = QtGui.QLabel(self.Bugwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 4, 3, 1, 1)
        self.BugDetail = QtGui.QTextEdit(self.Bugwidget)
        self.BugDetail.setObjectName(_fromUtf8("BugDetail"))
        self.gridLayout_2.addWidget(self.BugDetail, 3, 3, 1, 2)
        self.verticalLayout.addWidget(self.Bugwidget)
        self.Findwidget = QtGui.QWidget(self.centralwidget)
        self.Findwidget.setObjectName(_fromUtf8("Findwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.Findwidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.Findwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.SearchKey = QtGui.QLineEdit(self.Findwidget)
        self.SearchKey.setObjectName(_fromUtf8("SearchKey"))
        self.horizontalLayout_2.addWidget(self.SearchKey)
        self.MatchCase = QtGui.QCheckBox(self.Findwidget)
        self.MatchCase.setObjectName(_fromUtf8("MatchCase"))
        self.horizontalLayout_2.addWidget(self.MatchCase)
        self.next = QtGui.QPushButton(self.Findwidget)
        self.next.setObjectName(_fromUtf8("next"))
        self.horizontalLayout_2.addWidget(self.next)
        self.previous = QtGui.QPushButton(self.Findwidget)
        self.previous.setObjectName(_fromUtf8("previous"))
        self.horizontalLayout_2.addWidget(self.previous)
        self.verticalLayout.addWidget(self.Findwidget)
        self.Replacewidget = QtGui.QWidget(self.centralwidget)
        self.Replacewidget.setObjectName(_fromUtf8("Replacewidget"))
        self.gridLayout = QtGui.QGridLayout(self.Replacewidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.Replacewidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.Replacewidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.NewText = QtGui.QLineEdit(self.Replacewidget)
        self.NewText.setObjectName(_fromUtf8("NewText"))
        self.gridLayout.addWidget(self.NewText, 1, 1, 1, 1)
        self.OldText = QtGui.QLineEdit(self.Replacewidget)
        self.OldText.setObjectName(_fromUtf8("OldText"))
        self.gridLayout.addWidget(self.OldText, 0, 1, 1, 1)
        self.next_2 = QtGui.QPushButton(self.Replacewidget)
        self.next_2.setObjectName(_fromUtf8("next_2"))
        self.gridLayout.addWidget(self.next_2, 0, 3, 1, 1)
        self.replace = QtGui.QPushButton(self.Replacewidget)
        self.replace.setObjectName(_fromUtf8("replace"))
        self.gridLayout.addWidget(self.replace, 1, 4, 1, 1)
        self.previous_2 = QtGui.QPushButton(self.Replacewidget)
        self.previous_2.setObjectName(_fromUtf8("previous_2"))
        self.gridLayout.addWidget(self.previous_2, 0, 4, 1, 1)
        self.MatchCase_2 = QtGui.QCheckBox(self.Replacewidget)
        self.MatchCase_2.setObjectName(_fromUtf8("MatchCase_2"))
        self.gridLayout.addWidget(self.MatchCase_2, 0, 2, 1, 1)
        self.r_all = QtGui.QPushButton(self.Replacewidget)
        self.r_all.setObjectName(_fromUtf8("r_all"))
        self.gridLayout.addWidget(self.r_all, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.Replacewidget)
        self.Gotowidget = QtGui.QWidget(self.centralwidget)
        self.Gotowidget.setStyleSheet(_fromUtf8(""))
        self.Gotowidget.setObjectName(_fromUtf8("Gotowidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.Gotowidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.Gotowidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineNo = QtGui.QLineEdit(self.Gotowidget)
        self.lineNo.setObjectName(_fromUtf8("lineNo"))
        self.horizontalLayout.addWidget(self.lineNo)
        self.GoButton = QtGui.QPushButton(self.Gotowidget)
        self.GoButton.setObjectName(_fromUtf8("GoButton"))
        self.horizontalLayout.addWidget(self.GoButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.Gotowidget)
        Spellcheck.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Spellcheck)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 25))
        self.menubar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setSeparatorsCollapsible(False)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        Spellcheck.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(Spellcheck)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Spellcheck.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.formatBar = QtGui.QToolBar(Spellcheck)
        self.formatBar.setObjectName(_fromUtf8("formatBar"))
        Spellcheck.addToolBar(QtCore.Qt.TopToolBarArea, self.formatBar)
        self.actionNew = QtGui.QAction(Spellcheck)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/New.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(Spellcheck)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(Spellcheck)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(Spellcheck)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon4)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionCut = QtGui.QAction(Spellcheck)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Cut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon5)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(Spellcheck)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon6)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(Spellcheck)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon7)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionBug = QtGui.QAction(Spellcheck)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBug.setIcon(icon8)
        self.actionBug.setObjectName(_fromUtf8("actionBug"))
        self.actionAbout = QtGui.QAction(Spellcheck)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/About.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon9)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSaveAs = QtGui.QAction(Spellcheck)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/SaveAs.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon10)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionUndo = QtGui.QAction(Spellcheck)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon11)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(Spellcheck)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon12)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionSearch = QtGui.QAction(Spellcheck)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/Find.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon13)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionReplace = QtGui.QAction(Spellcheck)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/FindReplace.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReplace.setIcon(icon14)
        self.actionReplace.setObjectName(_fromUtf8("actionReplace"))
        self.actionGoto = QtGui.QAction(Spellcheck)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8("Resources/GoTo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoto.setIcon(icon15)
        self.actionGoto.setObjectName(_fromUtf8("actionGoto"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionBug)
        self.menuHelp.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionSearch)
        self.menuTools.addAction(self.actionReplace)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionGoto)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Spellcheck)
        QtCore.QMetaObject.connectSlotsByName(Spellcheck)
        Spellcheck.setTabOrder(self.textEdit, self.SearchKey)
        Spellcheck.setTabOrder(self.SearchKey, self.MatchCase)
        Spellcheck.setTabOrder(self.MatchCase, self.next)
        Spellcheck.setTabOrder(self.next, self.previous)
        Spellcheck.setTabOrder(self.previous, self.OldText)
        Spellcheck.setTabOrder(self.OldText, self.NewText)
        Spellcheck.setTabOrder(self.NewText, self.MatchCase_2)
        Spellcheck.setTabOrder(self.MatchCase_2, self.next_2)
        Spellcheck.setTabOrder(self.next_2, self.previous_2)
        Spellcheck.setTabOrder(self.previous_2, self.r_all)
        Spellcheck.setTabOrder(self.r_all, self.replace)
        Spellcheck.setTabOrder(self.replace, self.lineNo)
        Spellcheck.setTabOrder(self.lineNo, self.GoButton)
        Spellcheck.setTabOrder(self.GoButton, self.BugType)
        Spellcheck.setTabOrder(self.BugType, self.BugDetail)
        Spellcheck.setTabOrder(self.BugDetail, self.ReportButton)

    def retranslateUi(self, Spellcheck):
        Spellcheck.setWindowTitle(QtGui.QApplication.translate("Spellcheck", "Nepali SpellChecker v2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Spellcheck", "Bug Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Spellcheck", "Bug Type", None, QtGui.QApplication.UnicodeUTF8))
        self.ReportButton.setText(QtGui.QApplication.translate("Spellcheck", " Report Bug", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Spellcheck", "Please ensure that you have a working internet connection.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Spellcheck", "Find              ", None, QtGui.QApplication.UnicodeUTF8))
        self.MatchCase.setText(QtGui.QApplication.translate("Spellcheck", "Match Case", None, QtGui.QApplication.UnicodeUTF8))
        self.next.setText(QtGui.QApplication.translate("Spellcheck", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.previous.setText(QtGui.QApplication.translate("Spellcheck", "Find Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Spellcheck", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Spellcheck", "Replace With", None, QtGui.QApplication.UnicodeUTF8))
        self.next_2.setText(QtGui.QApplication.translate("Spellcheck", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.replace.setText(QtGui.QApplication.translate("Spellcheck", "Replace Next", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_2.setText(QtGui.QApplication.translate("Spellcheck", "Find Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.MatchCase_2.setText(QtGui.QApplication.translate("Spellcheck", "Match Case", None, QtGui.QApplication.UnicodeUTF8))
        self.r_all.setText(QtGui.QApplication.translate("Spellcheck", "Replace All", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Spellcheck", "Goto Line", None, QtGui.QApplication.UnicodeUTF8))
        self.GoButton.setText(QtGui.QApplication.translate("Spellcheck", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setStatusTip(QtGui.QApplication.translate("Spellcheck", "Displays all File Operations", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Spellcheck", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("Spellcheck", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("Spellcheck", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("Spellcheck", "&Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("Spellcheck", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.formatBar.setWindowTitle(QtGui.QApplication.translate("Spellcheck", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("Spellcheck", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setStatusTip(QtGui.QApplication.translate("Spellcheck", "Create a New file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("Spellcheck", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setStatusTip(QtGui.QApplication.translate("Spellcheck", "Open a New file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("Spellcheck", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setStatusTip(QtGui.QApplication.translate("Spellcheck", "Allows you to Save current file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("Spellcheck", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setStatusTip(QtGui.QApplication.translate("Spellcheck", "Close the file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("Spellcheck", "C&ut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setStatusTip(QtGui.QApplication.translate("Spellcheck", "Cuts selected text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("Spellcheck", "&Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setStatusTip(QtGui.QApplication.translate("Spellcheck", "Copies selected text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("Spellcheck", "&Paste               ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setStatusTip(QtGui.QApplication.translate("Spellcheck", "Paste copied text", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBug.setText(QtGui.QApplication.translate("Spellcheck", "Report &Bug          ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("Spellcheck", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("Spellcheck", "Save &As             ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("Spellcheck", "&Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("Spellcheck", "&Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setText(QtGui.QApplication.translate("Spellcheck", "&Find", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReplace.setText(QtGui.QApplication.translate("Spellcheck", "&Replace             ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReplace.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+Shift+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoto.setText(QtGui.QApplication.translate("Spellcheck", "&Goto", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoto.setShortcut(QtGui.QApplication.translate("Spellcheck", "Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))

