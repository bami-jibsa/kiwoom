import sys
from PyQt5.QtWidgets import *
from login import Kiwoom2

def log_info():
        app = QApplication(sys.argv)

        kiwoom = Kiwoom2()
        kiwoom.CommConnect()    

        accno = kiwoom.GetLoginInfo("ACCNO")   # 전체 계좌 반환
        accno_list = accno.split(";")[:-1]
        return accno_list
        


if __name__ == "__main__":
        log_info()