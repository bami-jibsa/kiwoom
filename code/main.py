import sys


from login import login, Kiwoom2

# Kiwoom1 = Kiwoom1()

# Kiwoom2 = Kiwoom2()

# kiwoom = kiwoom

print("로그인하시겠습니까? 0/1")

n = int(input())

if __name__ == "__main__":
    if n:
        login()

from last_price import last_price

from pykiwoom import kiwoom

from condition_list import condition_list

from login_info import log_info

from jango import Kiwoom1

from stock_buy import place_limit_buy_order, place_market_buy_order

from stock_sell import place_limit_sell_order, place_market_sell_order

from get_name import get_name

input = sys.stdin.readline


def start():
    print("1: 로그인 안됨2: 정보 3: 매매 4: 잔고")
    k = int(input())
    if k == 1:
        #로그인
        print("위치 이전시킴")
    if k == 2:
        #정보
        print("0: 처음으로 1: 로그인정보 2: 조건식검색 3: 종가")
        n = int(input())
        if n == 0:
            start()
        if n == 2:
            #로그인정보
                log_info = log_info
        if n == 3:
            # 조건식 검색
            print("몇번째 조건식?")
            print("('000', '새조건명'), ('001', '밥번자리'), ('002', '3봉이내 후행스팬 전환선 돌파'), ('003', 'macd'), ('004', 'rsi + macd')")
            c_num = int(input())
            cond_li = condition_list(c_num)
            print(cond_li)
        if n == 4:
            #종가
            print("주식번호")
            lp_num = int(input())
            lst_prc = last_price(lp_num)
            print(lst_prc)
    if k == 3:
        print("0: 처음으로 1: 지정가매수 2: 시장가매수 3: 지정가매도 4: 시장가매도")
        n = int(input())
        if n == 0:
            start()
        if n == 1:
            ("지정가매수")
            print("name 파라미터 int로")
            name, code, num, price = map(int, input().split())
            place_limit_buy_order(name, code, num, price)
        if n == 2:
            print("시장가매수")
            print("name 파라미터 int로")
            name, code, num = map(int, input().split())
            place_market_buy_order(name, code, num)
        if n == 3:
            ("지정가매도")
            print("name 파라미터 int로")
            name, code, num, price = map(int, input().split())
            place_limit_sell_order(name, code, num, price)        
        if n == 2:
            print("시장가매도")
            print("name 파라미터 int로")
            name, code, num = map(int, input().split())
            place_market_sell_order(name, code, num)
    if k == 4:
        # 잔고 확인
        print(f"총매입금액: {Kiwoom1.total_buy_money}원")
        print(f"총평가금액: {Kiwoom1.total_evaluation_money}원")
        print(f"총평가손익금액: {Kiwoom1.total_evaluation_profit_and_loss_money}원")
        print(f"총수익률: {Kiwoom1.total_yield}%")

def outo_start(num):
    cond_li = condition_list(num)
    
print("자동(1)/수동(0)")    
if __name__ == "__main__":
    type_ = input()
    if type_:
        pass
    else:
        start()