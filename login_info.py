import sys
from PyQt5.QtWidgets import *
from login import Kiwoom


if __name__ == "__main__":
    app = QApplication(sys.argv)

    kiwoom = Kiwoom()
    kiwoom.CommConnect()

    accno = kiwoom.GetLoginInfo("ACCNO")   # 전체 계좌 반환
    accno_list = accno.split(";")[:-1]
    print(accno_list)
