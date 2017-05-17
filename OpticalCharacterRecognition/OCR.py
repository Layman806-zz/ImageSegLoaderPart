# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OCR.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
# from ImgLoader import ImgLoad
import cv2
from ImageSegmenter import Segmenter as Seg

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Star_10_Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.labelBackground = QtGui.QLabel(self.centralwidget)
        self.labelBackground.setGeometry(QtCore.QRect(0, 0, 641, 201))
        self.labelBackground.setText(_fromUtf8(""))
        self.labelBackground.setPixmap(QtGui.QPixmap(_fromUtf8("labelBackground.jpg")))
        self.labelBackground.setObjectName(_fromUtf8("labelBackground"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 205, 640, 5))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.scanButton = QtGui.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(280, 210, 85, 27))
        self.scanButton.setObjectName(_fromUtf8("scanButton"))
        self.scanButton.clicked.connect(self.scanFunction)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 240, 640, 5))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(4, 250, 632, 200))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.labelForPicture = QtGui.QLabel(self.centralwidget)
        self.labelForPicture.setGeometry(QtCore.QRect(142, 0, 356, 201))
        self.labelForPicture.setText(_fromUtf8(""))
        self.labelForPicture.setObjectName(_fromUtf8("labelForPicture"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.triggered.connect(self.selectWindow)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(self.closeApplication)
        self.actionAbout_Developers = QtGui.QAction(MainWindow)
        self.actionAbout_Developers.setObjectName(_fromUtf8("actionAbout_Developers"))
        self.actionAbout_Software = QtGui.QAction(MainWindow)
        self.actionAbout_Software.setObjectName(_fromUtf8("actionAbout_Software"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout_Developers)
        self.menuAbout.addAction(self.actionAbout_Software)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR", None))
        self.scanButton.setText(_translate("MainWindow", "Scan", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionAbout_Developers.setText(_translate("MainWindow", "About Developers", None))
        self.actionAbout_Software.setText(_translate("MainWindow", "About Software", None))

    def selectWindow(self):
        fileDialog = QtGui.QFileDialog()
        self.pic = fileDialog.getOpenFileName()
        pixmap = QtGui.QPixmap(self.pic)
        w = pixmap.width()
        h = pixmap.height()
        # self.labelBackground.setGeometry(0, 0, 641, h)
        # self.labelForPicture.setGeometry(142, 0, w, h)
        if w > h:
            if h < 201:
                pixmap = pixmap.scaledToWidth(356)
            elif h > 201:
                pixmap = pixmap.scaledToHeight(201)
        else:
            pixmap = pixmap.scaledToHeight(201)
        self.labelForPicture.setPixmap(pixmap)
        self.labelForPicture.show()

    def scanFunction(self):
        # self.textBrowser.append("Hello World!")
        # imLoad = ImgLoad()
        # img = self.selectWindow()
        # imLoad.ImgFunction(self.pic)

        # Using Segmenter.py file
        S = Seg.Segmenter(self.pic)
        segments = S.segment()

        for s in segments:
            cv2.imshow('segment', s)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


    def closeApplication(self):
        choice = QtGui.QMessageBox.question(self, 'Exit Application!', "Are you sure you want to Quit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

