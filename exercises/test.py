# importing libraries
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

# creating a class
# that inherits the QDialog class


class Window(QDialog):

    # the contribution amount in dollars for TSLA SPY NTDOY and AAPL
    contribution = float(100)
    compound_frequency = 12  # the compound frequency in months

    # constructor
    def __init__(self):
        super(Window, self).__init__()

        # setting window title
        self.setWindowTitle("Python")

        # setting geometry to the window
        self.setGeometry(200, 200, 400, 500)

        # creating a group box
        self.formGroupBox = QGroupBox("Finance Functions")

        # creating a line edit
        self.startPrice = QLineEdit()
        self.startPrice.setValidator(QIntValidator())
        self.startPrice.setMaxLength(1021)
        self.startPrice.setAlignment(Qt.AlignRight)
        self.startPrice.setFont(QFont("Arial",20))
        
        self.endPrice = QLineEdit()
        self.endPrice.setValidator(QIntValidator())
        self.endPrice.setMaxLength(1021)
        self.endPrice.setAlignment(Qt.AlignRight)
        self.endPrice.setFont(QFont("Arial",20))
        
        self.investLength = QLineEdit()
        self.investLength.setValidator(QIntValidator())
        self.investLength.setMaxLength(1021)
        self.investLength.setAlignment(Qt.AlignRight)
        self.investLength.setFont(QFont("Arial",20))

        self.e1 = QLineEdit()
        self.e1.setValidator(QIntValidator())
        self.e1.setMaxLength(1021)
        self.e1.setAlignment(Qt.AlignRight)
        self.e1.setFont(QFont("Arial",20))

        self.startPrice = self.startPrice
        self.endPrice = self.endPrice
        self.investLength = self.investLength


        self.compound_frequency = QComboBox()
        self.compound_frequency.addItems(["4","12","52","365"])

        # calling the method that create the form
        self.createForm()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.calc_apr)

        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting lay out
        self.setLayout(mainLayout)

       

    # get info method called when form is accepted

    def getInfo(self):

        # printing the form information
        print("Starting Price : {0}".format(float((self.startPrice.text()))))
        print("Ending Price : {0}".format(float((self.endPrice.text()))))
        print("Investment Length : {0}".format(float(self.investLength.text())))

        # closing the window
        self.close()

    # creat form method
    def createForm(self):

        # creating a form layout
        layout = QFormLayout()

        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Enter Starting Price:"), self.startPrice)
        layout.addRow(QLabel("Enter Ending Price"), self.endPrice)
        layout.addRow(QLabel("Enter Investment Length"), self.investLength)
        layout.addRow(QLabel("Enter The Compound Frequency"), self.compound_frequency)
        layout.addRow(QLabel("Enter The Compound Frequency"), self.e1)
        # setting layout
        self.formGroupBox.setLayout(layout)

    # calculate the apr based on start price, end price, and length of investment in years
    def calc_apr(self):
        # compound interest formula
        rate = self.compound_frequency*((self.endPrice/self.startPrice)**(1/(self.compound_frequency*self.investLength))-1)
        # multiplies the rate by 100 for correct decimal placement and rounds 2 places after decimal
        rate = round(rate*100, 2)
        return rate

    def calc_annuity(self):
        amount = self.contribution*((1+(rate/100)/self.compound_frequency)**(self.compound_frequency*self.investLength)-1)/(rate/self.compound_frequency)  # annuity formula
        # multiplies the amount by 100 for correct decimal placement and rounds 2 places after decimal
        amount = round(amount*100, 2)
        return amount


# main method
if __name__ == '__main__':

    # create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # showing the window
    window.show()

    # start the app
    sys.exit(app.exec())
