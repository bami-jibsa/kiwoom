from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
def get_name(num):
    name = kiwoom.GetMasterCodeName(f"{num}")

    return name
n = '005930'
name = get_name(int(n))
print(name)

