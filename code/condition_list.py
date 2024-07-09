from pykiwoom.kiwoom import *

# 로그인
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

def condition_list(num):
    # 조건식을 PC로 다운로드
    kiwoom.GetConditionLoad()

    # 전체 조건식 리스트 얻기
    conditions = kiwoom.GetConditionNameList()

    # 0번 조건식에 해당하는 종목 리스트 출력
    condition_index = conditions[num][0]
    condition_name = conditions[num][1]
    codes = kiwoom.SendCondition("4000", condition_name, condition_index, 0)

    return codes
#[('000', '새조건명'), ('001', '밥그릇 4번자리'), ('002', '3봉이내 후행스팬 전환선 돌파'), ('003', 'macd'), ('004', 'rsi + macd')]
# condition_list()
a = condition_list(4)

print (a)