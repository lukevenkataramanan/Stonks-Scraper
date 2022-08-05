import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore


menu = [['Name', 'Symbol'],
        ['Amazon', 'AMZN'],
        ['Apple', 'AAPL'],
        ['Disney ', 'DIS'],
        ['GameStop ', 'GME'],
        ['Google  ', 'GOOGL'],
        ['Microsoft', 'MSFT'],
        ['Netflix', 'NFLX'],
        ['Nvidia', 'NVDA'],
        ['Starbucks', 'SBUX'],
        ['Tesla', 'TSLA']]
# menu is a 2D array, with the 0 column showing the ticker symbol and the 1 column showing the name


class MenuScreen(QWidget):
    def __init__(self):
        super().__init__()
        # create window
        self.setWindowTitle('Favorites Menu')
        self.setGeometry(1000, 0, 440, 800)
        self.setStyleSheet('background-color: rgba(16, 49, 208, 255)')
        # create grid
        grid = QGridLayout()
        for r in range(len(menu)):  # create menu of ticker symbols and names
            for c in range(len(menu[r])):
                label = QLabel(menu[r][c])
                if r == 0:
                    label.setStyleSheet("margin: 0px;\
                                        padding: 10px; \
                                        background-color: rgba(255, 171, 17, 255); \
                                        font-weight: 600; \
                                        border-style: solid; \
                                        border-radius: 4px; \
                                        border-width: 5px; \
                                        border-color: rgba(19,149,242,255);")
                    label.setFont(QtGui.QFont('Times New Roman', 30))
                    label.setAlignment(QtCore.Qt.AlignCenter)
                else:
                    label.setStyleSheet("margin: 5px;\
                                        padding: 10px; \
                                        background-color: rgba(16, 49, 208, 255); \
                                        font-weight: 300; \
                                        color: rgba(255, 255, 255, 255); \
                                        border-style: solid; \
                                        border-radius: 4px; \
                                        border-width: 5px; \
                                        border-color: rgba(19,149,242,255);")
                    label.setFont(QtGui.QFont('Times New Roman', 20))
                if c == 0:
                    label.setAlignment(QtCore.Qt.AlignLeft)
                else:  # right column
                    label.setAlignment(QtCore.Qt.AlignCenter)
                grid.addWidget(label, r, c)
        # done editing
        # wid = QWidget(self)
        # self.setCentralWidget(wid)
        # wid.setLayout(grid)
        self.setLayout(grid)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MenuScreen()
    sys.exit(app.exec())