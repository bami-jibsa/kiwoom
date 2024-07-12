# from check_connect
# from get_code
# from get_name
# from check_connect
from last_price import last_price

from login import login

from pykiwoom import kiwoom

from condition_list import condition_list

from login_info import log_info

kiwoom = kiwoom

#로그인
login()

#로그인정보
if __name__ == "__main__":
    log_ = log_info()

# 조건식 검색
cond_li = condition_list(4)

#종가
lst_prc = last_price()