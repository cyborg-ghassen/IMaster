import os
from os import listdir
from PIL import Image
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QFileDialog, QLineEdit, QPushButton


class Design(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "IMaster"
        self.x, self.y, self.width, self.height = 100, 100, 700, 600
        self.logo_label = QLabel(self)
        self.logo = QPixmap('IMaster logo.png').scaled(100, 100)
        self.icon = QIcon(self.logo)
        self.label_first = QLabel("Enter folder path:", self)
        self.line_first = QLineEdit(self)
        self.browse_first = QPushButton("Browse", self)
        self.label_second = QLabel("Choose an image to add:", self)
        self.line_second = QLineEdit(self)
        self.browse_second = QPushButton("Browse", self)
        self.execute = QPushButton("Execute", self)
        self.initUI()

    def initUI(self):
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('web.png'))

        self.show()

    def getFolder(self):
        fileName = QFileDialog.getExistingDirectory(caption='Choose Directory', directory=QDir.currentPath())
        self.line_first.setText(fileName)

    def getImage(self):
        fileName = QFileDialog.getOpenFileName(caption='Choose Image', directory=QDir.currentPath())
        self.line_second.setText(fileName[0])

    def image(self):
        self.logo.isQBitmap()
        self.logo_label.setPixmap(self.logo)
        self.logo_label.resize(100, 100)
        self.logo_label.setGeometry(30, 30, 100, 100)

    def folder_browsing(self):
        # Label
        self.label_first.setGeometry(200, 70, 300, 25)
        # LINE EDIT
        self.line_first.setGeometry(200, 100, 300, 25)
        # BROWSE
        self.browse_first.setGeometry(550, 100, 100, 25)
        if self.browse_first.clicked:
            self.browse_first.clicked.connect(lambda: self.getFolder())

    def image_browsing(self):
        # Label
        self.label_second.setGeometry(200, 150, 300, 25)
        # LINE EDIT
        self.line_second.setGeometry(200, 180, 300, 25)
        # BROWSE
        self.browse_second.setGeometry(550, 180, 100, 25)
        if self.browse_second.clicked:
            self.browse_second.clicked.connect(lambda: self.getImage())

    def executes(self):
        # Button
        self.execute.setGeometry(350, 260, 100, 25)
        if self.execute.clicked:
            self.execute.clicked.connect(lambda: self.process())

    def area(self):
        for i in listdir(self.line_first.text()):
            width, height = Image.open(self.line_first.text() + "/" + i).size
            left = 4
            top = height / 5
            right = 0
            bottom = 0
            im = Image.open(self.line_first.text() + "/" + i)
            im.copy()
            im.crop((left, top, right, bottom))
            Resize = (100, 100)
            im.resize(Resize)

    def getImageSize(self, image):
        return image.size

    def process(self):
        j = 0
        for i in listdir(self.line_first.text()):
            try:
                images = Image.open(self.line_first.text() + "/" + i)
            except Exception as ee:
                print(i, " - ", ee)
                continue
            img = Image.open(self.line_second.text())
            images.copy()
            img.copy()
            self.area()
            w, h = self.getImageSize(images)
            wl, hl = self.getImageSize(img)
            img = img.resize((wl // 6, hl // 6))
            wl2, hl2 = self.getImageSize(img)
            try:
                images.paste(img, (0, 0), mask=img)
                images.save(self.line_first.text() + "/{} - {}".format(j, i))
            except Exception as e:
                print(i, " - ", e)
                continue
            j += 1
