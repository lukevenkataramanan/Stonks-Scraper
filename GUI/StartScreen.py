import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
from GUI.MainScreen import MainScreen


dark_blue = 'rgba(16, 49, 208, 255)'
light_blue = 'rgba(19, 149, 242, 255)'
orange = 'rgba(255, 171, 17, 255)'


class StartScreen(QWidget):
    def start_button_clicked(self):  # opens the main window, used when start button is pressed
        self.main_screen_class = MainScreen()  # # line that opens the main window
        self.close()

    def __init__(self):
        super().__init__()
        # create window
        self.setWindowTitle('Stonks Simulator')
        self.setGeometry(0, 0, 1440, 800)
        self.setStyleSheet(f'background-color: {dark_blue}')
        self.main_screen_class = None
        # add the image
        stonks_image_label = QLabel(self)
        pixmap = QtGui.QPixmap('images/stonksImage.png').scaledToWidth(1008).scaledToHeight(560)
        stonks_image_label.setPixmap(pixmap)
        stonks_image_label.setStyleSheet(f"margin: 0px;\
                                        padding: 0px; \
                                        font-weight: 600; \
                                        border-style: solid; \
                                        border-radius: 14px; \
                                        border-width: 5px; \
                                        border-color: {light_blue};")
        # add title label
        title_label = QLabel('Stonks Simulator')
        title_label.setStyleSheet(f"margin: 5px;\
                                    padding: 10px; \
                                    background-color: {dark_blue}; \
                                    font-weight: 300; \
                                    color: rgba(255, 255, 255, 255); \
                                    border-style: solid; \
                                    border-radius: 14px; \
                                    border-width: 5px; \
                                    border-color: {light_blue};")
        title_label.setFont(QtGui.QFont('Times New Roman', 80))
        title_label.setAlignment(QtCore.Qt.AlignVCenter)
        # add button
        self.start_button = QPushButton('Start')
        self.start_button.setStyleSheet(f"margin: 0px;\
                                        padding: 40px; \
                                        background-color: {orange}; \
                                        color: {dark_blue}; \
                                        font-weight: 600; \
                                        border-style: solid; \
                                        border-radius: 14px; \
                                        border-width: 5px; \
                                        border-color: {light_blue};")
        self.start_button.setFont(QtGui.QFont('Times New Roman', 40))
        self.start_button.clicked.connect(self.start_button_clicked)
        # add credits
        credits_label = QLabel('Created by Luke Venkataramanan©\n'
                               '\t(Press ⌘+Q to Quit)')
        credits_label.setStyleSheet("margin: 0px;\
                                    padding: 0px; \
                                    background-color: rgba(16, 49, 208, 255); \
                                    font-weight: 300; \
                                    color: rgba(255, 255, 255, 255);")
        credits_label.setFont(QtGui.QFont('Times New Roman', 25))
        # grid placements
        grid = QGridLayout()
        grid.addWidget(title_label, 0, 0, 1, 3)
        grid.addWidget(self.start_button, 0, 3, 1, 2)
        grid.addWidget(stonks_image_label, 1, 0, 1, 3)
        grid.addWidget(credits_label, 1, 3, 2, 1)
        self.setLayout(grid)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StartScreen()
    sys.exit(app.exec())
