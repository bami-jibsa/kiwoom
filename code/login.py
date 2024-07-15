import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pythoncom
import time
import win32gui
import win32con

class Kiwoom2:
    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.login = False

        self.ocx.OnEventConnect.connect(self.OnEventConnect)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        while self.login is False:
            pythoncom.PumpWaitingMessages()

    def OnEventConnect(self, err_code):
        if err_code == 0:
            self.login = True
            print("로그인 성공")
        else:
            print("로그인 실패, 코드:", err_code)

    def show_account_window(self):
        if self.login:
            self.ocx.dynamicCall("KOA_Functions(QString, QString)", "ShowAccountWindow", "")
            print("ShowAccountWindow 호출 완료")
        else:
            print("로그인되지 않았습니다.")

    def auto_login(self, user_password):
        def find_window(title):
            hwnd = win32gui.FindWindow(None, title)
            if hwnd == 0:
                return None
            else:
                return hwnd

        def set_text(hwnd, text):
            win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, 0, text)
            time.sleep(0.1)

        def click_button(hwnd):
            win32gui.PostMessage(hwnd, win32con.BM_CLICK, 0, 0)
            time.sleep(0.1)

        login_hwnd = None
        while login_hwnd is None:
            login_hwnd = find_window("번개 Login")
            time.sleep(0.1)

        if login_hwnd:
            hwnd_password = win32gui.GetDlgItem(login_hwnd, 0x3E9)
            hwnd_login_button = win32gui.GetDlgItem(login_hwnd, 0x1)

            set_text(hwnd_password, user_password)
            click_button(hwnd_login_button)

    def GetLoginInfo(self, tag):
        ret = self.ocx.dynamicCall("GetLoginInfo(QString)", tag)
        return ret  

    def GetMasterLastPrice(self, code):
        ret = self.ocx.dynamicCall("GetMasterLastPrice(QString)", code)
        return int(ret) 
    
def login():
    app = QApplication(sys.argv)
    
    kiwoom = Kiwoom2()
    kiwoom.CommConnect()
    # print("블록킹 로그인 완료")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom2()
    
    # 자동 로그인 정보 (비밀번호만 입력)
    user_password = "tls4637"
    
    kiwoom.auto_login(user_password)
    kiwoom.CommConnect()
    kiwoom.show_account_window()
