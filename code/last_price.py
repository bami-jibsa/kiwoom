import sys
from PyQt5.QtWidgets import *
from login import Kiwoom2

def last_price(num):
    app = QApplication(sys.argv)

    kiwoom = Kiwoom2()
    kiwoom.CommConnect()

    price = kiwoom.GetMasterLastPrice(f"{num}")
    
    return price


if __name__ == "__main__":
    last_price()