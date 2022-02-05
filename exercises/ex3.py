from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    
    # the contribution amount in dollars for TSLA SPY NTDOY and AAPL
    contribution = float(100)
    compound_frequency = 12  # the compound frequency in months    
    
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Finance Functions")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50, 50)
        

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.move(50,70)
        self.b1.clicked.connect(self.clicked)

    def user_input(self):
        name, done1 = QtWidgets.QInputDialog.getText(
            self, 'Input Dialog', 'Enter your name: ')
        

    def clicked(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

    # calculate the apr based on start price, end price, and length of investment in years
    def calc_apr(start, end, time):
        # compound interest formula
        rate = compound_frequency * \
            ((end/start)**(1/(compound_frequency*time))-1)
        # multiplies the rate by 100 for correct decimal placement and rounds 2 places after decimal
        rate = round(rate*100, 2)
        return rate

    def calc_annuity(contribution, rate, time, compound_frequency):
        amount = contribution*((1+(rate/100)/compound_frequency)**(
            compound_frequency*time)-1)/(rate/compound_frequency)  # annuity formula
        # multiplies the amount by 100 for correct decimal placement and rounds 2 places after decimal
        amount = round(amount*100, 2)
        return amount


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
