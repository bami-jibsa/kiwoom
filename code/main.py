import sys
# from check_connect
# from get_code
# from get_name
# from check_connect
from last_price import last_price

from login import login

from pykiwoom import kiwoom

from condition_list import condition_list

from login_info import log_info

# kiwoom = kiwoom

input = sys.stdin.readline

print("1: 로그인 2: 로그인정보 3: 조건식검색 4: 종목 종가")

n = int(input())


if n == 1:
    #로그인
    login()

# if n == 2:
#     #로그인정보
#     if __name__ == "__main__":
#         log_ = log_info()

# if n == 3:
#     # 조건식 검색
#     cond_li = condition_list(4)

# if n == 4:
#     #종가
#     lst_prc = last_price()