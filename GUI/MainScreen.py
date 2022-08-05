import sys
from PyQt5.QtCore import QTimer, QTime, Qt
from main import ui_stock_scraper
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
from GUI.MenuScreen import MenuScreen
from GUI.TrendingScreen import TrendingScreen

dark_blue = 'rgba(16, 49, 208, 255)'
light_blue = 'rgba(19, 149, 242, 255)'
orange = 'rgba(255, 171, 17, 255)'


class MainScreen(QWidget):
    def toggle_button_pressed(self):  # cycle is favorites -> trending -> closed
        if self.favorites_screen_class:  # if click and favorites tab is open, close and open trending
            self.favorites_screen_class.close()
            self.favorites_screen_class = None
            self.trending_screen_class = TrendingScreen()
            self.toggle_button.setText('Close')
        elif self.trending_screen_class:  # elif click and trending tab is open, close
            self.trending_screen_class.close()
            self.trending_screen_class = None
            self.toggle_button.setText('Favorites')
        else:  # if both are closed, open favorites
            self.favorites_screen_class = MenuScreen()
            self.toggle_button.setText('Trending')

    def enter_button_pressed(self):
        text_to_add = ui_stock_scraper(self.line_edit.text())  # find text to add to output
        if self.line_edit.text() == '':
            return
        # if length of it is already _____, then clear it first
        if self.output_length >= 10:
            self.output_box.setText(text_to_add)
            self.output_length = 1
        else:  # less than _____, so just add it to bottom
            current_text = self.output_box.text()
            self.output_box.setText(current_text + '\n' + text_to_add)
            self.output_length += 1
        self.line_edit.setText('')

    def pin_clicked(self):
        if self.current_pin == 0:  # right now is kalm
            self.stonks_pin_image_label.setPixmap(QtGui.QPixmap('images/panik.png').scaledToHeight(100).scaledToWidth(100))
            self.current_pin = 1
        else:
            self.stonks_pin_image_label.setPixmap(QtGui.QPixmap('images/kalm.png').scaledToHeight(100).scaledToWidth(100))
            self.current_pin = 0

    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.clock_label.setText(label_time)

    def __init__(self):
        super().__init__()
        # create window
        self.setWindowTitle('Stonks Simulator')
        self.setGeometry(0, 0, 1000, 800)
        self.setStyleSheet(f'background-color: {dark_blue}')
        self.favorites_screen_class = MenuScreen()  # opens menu on launch
        self.trending_screen_class = None  # initializes, but is closed
        # add Line Edit
        self.line_edit = QLineEdit(self)
        self.line_edit.setFont(QtGui.QFont('Times New Roman', 15))
        self.line_edit.setPlaceholderText('Enter a ticker symbol')
        # line_edit.setMinimumWidth(500)
        self.line_edit.setStyleSheet("margin: 10px;\
                                padding: 10; \
                                background-color: rgba(255, 171, 17, 255); \
                                font-weight: 600; \
                                border-style: solid; \
                                border-radius: 4px; \
                                border-width: 5px; \
                                border-color: rgba(19,149,242,255);")
        self.line_edit.setFixedHeight(75)
        self.line_edit.returnPressed.connect(lambda: self.enter_button_pressed())
        # add enter button
        self.enter_button = QPushButton('enter')
        self.enter_button.setFont(QtGui.QFont('Times New Roman', 15))
        self.enter_button.setStyleSheet("margin: 10px;\
                                    padding: 10px; \
                                    background-color: rgba(255, 171, 17, 255); \
                                    font-weight: 600; \
                                    border-style: solid; \
                                    border-radius: 4px; \
                                    border-width: 5px; \
                                    border-color: rgba(19,149,242,255);")
        self.enter_button.clicked.connect(lambda: self.enter_button_pressed())
        self.enter_button.setFixedHeight(75)
        # add menu button
        self.toggle_button = QPushButton('Trending')
        self.toggle_button.setFont(QtGui.QFont('Times New Roman', 15))
        self.toggle_button.setStyleSheet("margin: 10px;\
                                        padding: 10px; \
                                        background-color: rgba(255, 171, 17, 255); \
                                        font-weight: 600; \
                                        border-style: solid; \
                                        border-radius: 4px; \
                                        border-width: 5px; \
                                        border-color: rgba(19,149,242,255);")
        self.toggle_button.clicked.connect(lambda: self.toggle_button_pressed())
        self.toggle_button.setFixedHeight(75)
        # add clock label
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.showTime())
        self.timer.start(1000)
        self.clock_label = QLabel(QTime.currentTime().toString('hh:mm:ss'))
        self.clock_label.setStyleSheet(f"margin: 10px;\
                                        padding: 10px; \
                                        background-color: {orange}; \
                                        font-weight: 600; \
                                        color: rgba(0, 0, 0, 255); \
                                        border-style: solid; \
                                        border-radius: 4px; \
                                        border-width: 5px; \
                                        border-color: {light_blue};")
        self.clock_label.setAlignment(Qt.AlignCenter)
        self.clock_label.setFont(QtGui.QFont('Times New Roman', 20))
        self.clock_label.setFixedHeight(75)
        # add stocks pin image and clear button
        self.stonks_pin_image_label = QLabel(self)
        pixmap = QtGui.QPixmap('images/kalm.png').scaledToHeight(100).scaledToWidth(100)
        self.stonks_pin_image_label.setPixmap(pixmap)
        self.stonks_pin_image_label.setAlignment(Qt.AlignCenter)
        stonks_pin_image_label_button = QPushButton(self)
        stonks_pin_image_label_button.setFixedHeight(100)
        stonks_pin_image_label_button.setFixedWidth(100)
        stonks_pin_image_label_button.setStyleSheet('border-radius: 50;\
                                                     background-color: rgba(0, 0, 0, 0);')
        self.current_pin = 0  # 0 means kalm, 1 means panik
        stonks_pin_image_label_button.clicked.connect(lambda: self.pin_clicked())
        # add output box
        self.output_length = 0
        self.output_box = QLabel('')
        self.output_box.setStyleSheet(f"margin: 5px;\
                                        padding: 10px; \
                                        background-color: {dark_blue}; \
                                        font-weight: 300; \
                                        color: rgba(255, 255, 255, 255); \
                                        border-style: solid; \
                                        border-radius: 14px; \
                                        border-width: 5px; \
                                        border-color: {light_blue};")
        self.output_box.setAlignment(Qt.AlignTop)
        self.output_box.setFont(QtGui.QFont('Times New Roman', 20))
        # grid placements
        grid = QGridLayout()
        grid.addWidget(self.line_edit, 0, 0, 1, 3)
        grid.addWidget(self.enter_button, 0, 3, 1, 2)
        grid.addWidget(self.clock_label, 1, 0, 1, 2)
        grid.addWidget(self.stonks_pin_image_label, 1, 2)
        grid.addWidget(stonks_pin_image_label_button, 1, 2)
        grid.addWidget(self.toggle_button, 1, 3, 1, 2)
        grid.addWidget(self.output_box, 2, 0, 2, 5)
        self.setLayout(grid)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainScreen()
    sys.exit(app.exec())
