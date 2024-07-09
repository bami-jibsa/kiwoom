from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

def place_limit_buy_order(order_name, stock_code, order_quantity, order_price):
    try:
        result = kiwoom.SendOrder(
            rqname=f"{order_name} 지정가 매수",  # 요청 이름
            screen="1000",  # 화면번호
            acc_no=stock_account,  # 계좌번호
            order_type=1,  # 주문 유형 1:매수 2:매도 3:매수취소 4:매도취소 5:매수정정 6:매도정정
            code=stock_code,  # 종목 코드
            quantity=order_quantity,  # 주문 수량
            price=order_price,  # 주문 단가
            hoga_gb="00",  # 00 지정가, 03 시장가
            org_order_no=""  # 원주문 번호로 정정 시 사용
        )
        if result == 0:
            print(f"{order_name} 지정가 매수 주문이 성공적으로 접수되었습니다.")
        else:
            print(f"{order_name} 지정가 매수 주문이 실패했습니다. 에러 코드: {result}")
    except Exception as e:
        print(f"오류 발생: {e}")

def place_market_buy_order(order_name, stock_code, order_quantity):
    try:
        result = kiwoom.SendOrder(
            rqname=f"{order_name} 시장가 매수",  # 요청 이름
            screen="1001",  # 화면번호
            acc_no=stock_account,  # 계좌번호
            order_type=1,  # 주문 유형 1:매수 2:매도 3:매수취소 4:매도취소 5:매수정정 6:매도정정
            code=stock_code,  # 종목 코드
            quantity=order_quantity,  # 주문 수량
            price=0,  # 주문 단가
            hoga_gb="03",  # 00 지정가, 03 시장가
            org_order_no=""  # 원주문 번호로 정정 시 사용
        )
        if result == 0:
            print(f"{order_name} 시장가 매수 주문이 성공적으로 접수되었습니다.")
        else:
            print(f"{order_name} 시장가 매수 주문이 실패했습니다. 에러 코드: {result}")
    except Exception as e:
        print(f"오류 발생: {e}")

# 사용 예시
# place_limit_buy_order("삼성전자", "005930", 10, 60000)
# place_market_buy_order("삼성전자", "005930", 10)
