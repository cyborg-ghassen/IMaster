import sys
from PyQt5.QtWidgets import QApplication
from Classes.Design import Design


def main():
    app = QApplication(sys.argv)
    d = Design()
    d.image()
    d.folder_browsing()
    d.image_browsing()
    d.executes()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
