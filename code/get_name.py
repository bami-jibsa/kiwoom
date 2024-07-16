from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
# kiwoom.CommConnect(block=True)
def get_name(num):
    num = (f"{num}")
    name = kiwoom.GetMasterCodeName(num)

    return name
n = '005930'
name = get_name(n)
print(name)

