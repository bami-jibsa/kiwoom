import sys
from PyQt5.QtWidgets import *
from login import Kiwoom

def last_price():
    app = QApplication(sys.argv)

    kiwoom = Kiwoom()
    kiwoom.CommConnect()

    price = kiwoom.GetMasterLastPrice("005930")
    print(price)


if __name__ == "__main__":
    last_price()