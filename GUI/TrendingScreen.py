import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from main import trending_scraper


menu = trending_scraper()
menu.insert(0, ['Name', 'Symbol', 'True'])

# menu is a 2D array in the form of
# 0: ticker symbol,  1: name,  2: if it is positive change or not (did it increase)


class TrendingScreen(QWidget):
    def __init__(self):
        super().__init__()
        # create window
        self.setWindowTitle('Trending Menu')
        self.setGeometry(1000, 0, 440, 800)
        self.setMaximumWidth(440)
        self.setStyleSheet('background-color: rgba(16, 49, 208, 255)')
        # create grid
        grid = QGridLayout()
        for r in range(len(menu)):  # create menu of ticker symbols and names
            for c in range(2):
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
                    # green rgba(0, 135, 60, 255)
                    # red rgba(235, 17, 43, 255)
                    if menu[r][2]:
                        label.setStyleSheet("margin: 5px;\
                                            padding: 10px; \
                                            background-color: rgba(16, 49, 208, 255); \
                                            font-weight: 300; \
                                            color: rgba(255, 255, 255, 255); \
                                            border-style: solid; \
                                            border-radius: 4px; \
                                            border-width: 5px; \
                                            border-color: rgba(0,135,60,255);")
                    else:
                        label.setStyleSheet("margin: 5px;\
                                            padding: 10px; \
                                            background-color: rgba(16, 49, 208, 255); \
                                            font-weight: 300; \
                                            color: rgba(255, 255, 255, 255); \
                                            border-style: solid; \
                                            border-radius: 4px; \
                                            border-width: 5px; \
                                            border-color: rgba(235,17,43,255);")
                    label.setFont(QtGui.QFont('Times New Roman', 10))  # lower puts it closer to edge, higher farther
                if c == 0:
                    label.setAlignment(QtCore.Qt.AlignLeft)
                else:  # right column
                    label.setAlignment(QtCore.Qt.AlignCenter)
                # label.setMaximumWidth(640)
                grid.addWidget(label, r, c)
        group_box = QGroupBox()
        group_box.setLayout(grid)

        scroll = QScrollArea()
        scroll.setWidget(group_box)
        scroll.setFixedHeight(800)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TrendingScreen()
    sys.exit(app.exec())
