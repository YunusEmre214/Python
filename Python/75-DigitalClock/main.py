import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt, QLocale
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700,400,300,100)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size:150px;"
                                      "color:#17bd1c;")
        self.setStyleSheet("background-color:black;")

        script_dir = os.path.dirname(__file__)
        font_path = os.path.join(script_dir, "DS-DIGIT.TTF")

        font_id=QFontDatabase.addApplicationFont(font_path)
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_family,150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        locale = QLocale(QLocale.English, QLocale.UnitedStates)
        current_time=QTime.currentTime()
        time_string = locale.toString(current_time, "hh:mm:ss AP")
        self.time_label.setText(time_string)



if __name__=="__main__":
    app=QApplication(sys.argv)
    clock=DigitalClock()
    clock.show()
    sys.exit(app.exec_())