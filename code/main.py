import sys

import pandas as pd

import datetime
from openpyxl import load_workbook
from login import login, Kiwoom2

# Kiwoom1 = Kiwoom1()

# Kiwoom2 = Kiwoom2()

# kiwoom = kiwoom

print("로그인하시겠습니까? 0/1")

n = int(input())

if __name__ == "__main__":
    if n:
        login()
    else:
        pass



input = sys.stdin.readline


def xl(type__, name, num, price):
    if type__:
        type__ = "매수"
    else:
        type__ = "매도"

    name = name
    now = datetime.datetime.now()
    fom_t =  now.strftime("%y.%m.%d.%H.%M")

    if price:
        new_data = {
            fom_t : [f"지정가-{type__}", name, num, price]
        }
    else:
        new_data = {
            fom_t : [f"시장가-{type__}", name, num, "--"]
        }

    # 새 데이터를 데이터프레임으로 변환
    new_df = pd.DataFrame.from_dict(new_data, orient='index', columns=['Value1', 'Value2', 'Value3', 'Value4', 'Value5', 'Value6', 'Value7'])

    # 기존 엑셀 파일 읽기
    file_path = 'output.xlsx'
    book = load_workbook(file_path)
    writer = pd.ExcelWriter(file_path, engine='openpyxl')
    writer.book = book

    # 기존 시트 데이터 불러오기
    existing_df = pd.read_excel(file_path, index_col=0)

    # 기존 데이터에 새 데이터 추가
    updated_df = pd.concat([existing_df, new_df])

    # 데이터를 엑셀 파일에 다시 저장
    updated_df.to_excel(writer, index=True, index_label='Key')

    # 파일 저장 및 닫기
    writer.save()
    writer.close()

    print("엑셀 파일에 데이터가 성공적으로 추가되었습니다.")


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
            from condition_list import condition_list
            print("몇번째 조건식?")
            print("('000', '새조건명'), ('001', '밥번자리'), ('002', '3봉이내 후행스팬 전환선 돌파'), ('003', 'macd'), ('004', 'rsi + macd')")
            c_num = int(input())
            cond_li = condition_list(c_num)
            print(cond_li)
        if n == 4:
            #종가

            from last_price import last_price
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
            from stock_buy import place_limit_buy_order
            print("지정가매수")
            print("name 파라미터 int로")
            name, code, num, price = map(int, input().split())
            place_limit_buy_order(name, code, num, price)
        if n == 2:
            from stock_buy import place_market_buy_order
            print("시장가매수")
            print("name 파라미터 int로")
            name, code, num = map(int, input().split())
            place_market_buy_order(name, code, num)
        if n == 3:
            from stock_sell import place_limit_sell_order
            ("지정가매도")
            print("name 파라미터 int로")
            name, code, num, price = map(int, input().split())
            place_limit_sell_order(name, code, num, price)        
        if n == 2:
            from stock_sell import place_market_sell_order
            print("시장가매도")
            print("name 파라미터 int로")
            name, code, num = map(int, input().split())
            place_market_sell_order(name, code, num)
    if k == 4:
        # 잔고 확인
        from jango import Kiwoom1
        print(f"총매입금액: {Kiwoom1.total_buy_money}원")
        print(f"총평가금액: {Kiwoom1.total_evaluation_money}원")
        print(f"총평가손익금액: {Kiwoom1.total_evaluation_profit_and_loss_money}원")
        print(f"총수익률: {Kiwoom1.total_yield}%")

def auto_start(num):
    for i in range(1, 4):
        from condition_list import condition_list
        from jango import Kiwoom1
        from stock_buy import place_market_buy_order
        from last_price import last_price

        cond_li = condition_list(num)
        buy_code = cond_li[i-1]

        qtt = ((int(Kiwoom1.total_evaluation_money) - int(Kiwoom1.total_buy_money))/3)/int(last_price(buy_code))

        for _ in range(3):
            place_market_buy_order(i, buy_code, (qtt/3))

print("자동(1)/수동(0)")    
if __name__ == "__main__":
    type_ = input()
    if not type_:
        print("조건식 번호")
        num = int(input())
        auto_start(num)
    else:
        start()