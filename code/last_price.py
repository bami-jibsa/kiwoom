import sys
from PyQt5.QtWidgets import *
from login import Kiwoom


if __name__ == "__main__":
    app = QApplication(sys.argv)

    kiwoom = Kiwoom()
    kiwoom.CommConnect()

    price = kiwoom.GetMasterLastPrice("005930")
    print(price)
