'''
Minor Project :-

Title : Optical Character Recognition
Developers : Bavani Sankar A. B. and Tejas Verghese

'''


from PyQt4 import QtCore, QtGui
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

        # MainWindow setup
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

        # Black Background image behind the Image to be scanned
        self.labelBackground = QtGui.QLabel(self.centralwidget)
        self.labelBackground.setGeometry(QtCore.QRect(0, 0, 641, 201))
        self.labelBackground.setText(_fromUtf8(""))
        self.labelBackground.setPixmap(QtGui.QPixmap(_fromUtf8("labelBackground.jpg")))
        self.labelBackground.setObjectName(_fromUtf8("labelBackground"))

        # First line separator
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 205, 640, 5))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        # Scan Button setup
        self.scanButton = QtGui.QPushButton(self.centralwidget)
        self.scanButton.setGeometry(QtCore.QRect(280, 210, 85, 27))
        self.scanButton.setObjectName(_fromUtf8("scanButton"))
        self.scanButton.clicked.connect(self.scanFunction)

        # Second line separator
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 240, 640, 5))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        # Output Text Area
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(4, 250, 632, 200))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        # Empty Label for Input Image
        self.labelForPicture = QtGui.QLabel(self.centralwidget)
        self.labelForPicture.setGeometry(QtCore.QRect(142, 0, 356, 201))
        self.labelForPicture.setText(_fromUtf8(""))
        self.labelForPicture.setObjectName(_fromUtf8("labelForPicture"))

        MainWindow.setCentralWidget(self.centralwidget)

        # MenuBar basic setup
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        # File Menu Option setup
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))

        # About Menu Option setup
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))

        MainWindow.setMenuBar(self.menubar)

        # StatusBar setup
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)

        # File -> Open Option setup
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.triggered.connect(self.selectWindow)

        # File -> Exit Option setup
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(self.closeApplication)

        # About -> About Developers Option setup
        self.actionAbout_Developers = QtGui.QAction(MainWindow)
        self.actionAbout_Developers.setObjectName(_fromUtf8("actionAbout_Developers"))

        # About -> About Software Option setup
        self.actionAbout_Software = QtGui.QAction(MainWindow)
        self.actionAbout_Software.setObjectName(_fromUtf8("actionAbout_Software"))

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.menuAbout.addAction(self.actionAbout_Developers)
        self.menuAbout.addAction(self.actionAbout_Software)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())


        # This is used to call retranslateUi function to show button names, shortcuts, etc.
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
        '''
            This function will first open a file dialog box.
            There we will select an Image file.
            And then a preview is created for that image,
            while the image is given as input to scanFunction().
        '''

        fileDialog = QtGui.QFileDialog()
        self.pic = fileDialog.getOpenFileName()
        pixmap = QtGui.QPixmap(self.pic)
        w = pixmap.width()
        h = pixmap.height()
        center = int((641 - w) / 2)
        # print(center)

        if center < 0:
            pixmap = pixmap.scaledToHeight(201)
            w = pixmap.width()
            h = pixmap.height()
            center = int((641 - w) / 2)
            self.labelForPicture.setGeometry(center, 0, w, 201)
        elif center >= 0:
            self.labelForPicture.setGeometry(center, 0, w, 201)

        if w > h:
            if h < 201:
                pixmap = pixmap.scaledToWidth(w)
            elif h > 201:
                pixmap = pixmap.scaledToHeight(201)
                w = pixmap.width()
                h = pixmap.height()
                center = int((641 - w) / 2)
                self.labelForPicture.setGeometry(center, 0, w, h)

        elif w == h and h <= 201:
            pixmap = pixmap.scaledToHeight(h)
        elif w < h:
            pixmap = pixmap.scaledToHeight(201)
        self.labelForPicture.setPixmap(pixmap)
        self.labelForPicture.show()


    def scanFunction(self):
        '''
            This Function will display the segments of image data.
            This is a temporary activity. 
        '''

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
        '''
            This Function will Exit/Quit the Application.
            It will also ask for confirmation before exit. 
        '''

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

