# # import datetime
# # from openpyxl import load_workbook
# # import os
# # import pandas as pd
# # # now = datetime.datetime.now()
# # # fom_t =  now.strftime("%y.%m.%d - %H.%M")

# # # print(fom_t)

# # # dir_path = 'xlsx'
# # # file_name = 'ty.xlsx'
# # # file_path = os.path.join(dir_path, file_name)


# # # # # 디렉토리가 존재하지 않으면 생성
# # # # if not os.path.exists(dir_path):
# # # #     os.makedirs(dir_path)

# # # wb = openpyxl.Workbook()
# # # ws = wb.active

# # # # 셀에 데이터 입력
# # # ws['A1'] = fom_t

# # # ws['B1'] = "aa"

# # # # 열 너비 조절 (A열과 B열의 너비를 20으로 설정)
# # # ws.column_dimensions['A'].width = 20
# # # ws.column_dimensions['B'].width = 30

# # # # 행 높이 조절 (1행의 높이를 40으로 설정)
# # # ws.row_dimensions[1].height = 40

# # # # 엑셀 파일 저장
# # # wb.save(file_path)

# # # print("엑셀 파일의 셀 크기가 조절되었습니다.")

# # # def xl(type__, name, num, price):
# # #     if type__:
# # #         type__ = "매수"
# # #     else:
# # #         type__ = "매도"

# # #     name = name
# # #     now = datetime.datetime.now()
# # #     fom_t =  now.strftime("%y.%m.%d.%H.%M")

# # #     if price:
# # #         new_data = {
# # #             fom_t : [f"지정가-{type__}", name, num, price]
# # #         }
# # #     else:
# # #         new_data = {
# # #             fom_t : [f"시장가-{type__}", name, num, "--"]
# # #         }

# # #     # 새 데이터를 데이터프레임으로 변환
# # #     new_df = pd.DataFrame.from_dict(new_data, orient='index', columns=['Value1', 'Value2', 'Value3', 'Value4', 'Value5', 'Value6', 'Value7'])

# # #     # 기존 엑셀 파일 읽기
# # #     file_path = 'output.xlsx'
# # #     book = load_workbook(file_path)
# # #     writer = pd.ExcelWriter(file_path, engine='openpyxl')
# # #     writer.book = book

# # #     # 기존 시트 데이터 불러오기
# # #     existing_df = pd.read_excel(file_path, index_col=0)

# # #     # 기존 데이터에 새 데이터 추가
# # #     updated_df = pd.concat([existing_df, new_df])

# # #     # 데이터를 엑셀 파일에 다시 저장
# # #     updated_df.to_excel(writer, index=True, index_label='Key')

# # #     # 파일 저장 및 닫기
# # #     writer.save()
# # #     writer.close()

# # #     print("엑셀 파일에 데이터가 성공적으로 추가되었습니다.")


# # def xl(type__, name, num, price):
# #     dir_path = 'xlsx'
# #     file_name = 'ty.xlsx'
# #     file_path = os.path.join(dir_path, file_name)


# #     if type__:
# #         type__ = "매수"
# #     else:
# #         type__ = "매도"

# #     name = name
# #     now = datetime.datetime.now()
# #     fom_t = now.strftime("%y.%m.%d.%H.%M")

# #     if price:
# #         new_data = {
# #             fom_t : [f"지정가-{type__}", name, num, price]
# #         }
# #     else:
# #         new_data = {
# #             fom_t : [f"시장가-{type__}", name, num, "--"]
# #         }

# #     # 새 데이터를 데이터프레임으로 변환
# #     new_df = pd.DataFrame.from_dict(new_data, orient='index', columns=['Value1', 'Value2', 'Value3', 'Value4'])

# #     # 기존 엑셀 파일 읽기
# #     book = load_workbook(file_path)
# #     writer = pd.ExcelWriter(file_path, engine='openpyxl')
# #     writer.book = book

# #     # 기존 시트 데이터 불러오기
# #     existing_df = pd.read_excel(file_path, index_col=0)

# #     # 기존 데이터에 새 데이터 추가
# #     updated_df = pd.concat([existing_df, new_df])

# #     # 데이터를 엑셀 파일에 다시 저장
# #     updated_df.to_excel(writer, index=True, index_label='Key')

# #     # 파일 저장 및 닫기
# #     writer.save()
# #     writer.close()

# #     print("엑셀 파일에 데이터가 성공적으로 추가되었습니다.")

# # xl(0, 3, 4, 2)




# import os
# import datetime
# from openpyxl import load_workbook
# import pandas as pd

# def xl(type__, name, num, price):
#     if type__:
#         type__ = "매수"
#     else:
#         type__ = "매도"

#     now = datetime.datetime.now()
#     fom_t = now.strftime("%y.%m.%d.%H.%M")

#     if price:
#         new_data = {
#             fom_t: [f"지정가-{type__}", name, num, price]
#         }
#     else:
#         new_data = {
#             fom_t: [f"시장가-{type__}", name, num, "--"]
#         }

#     # 새 데이터를 데이터프레임으로 변환
#     new_df = pd.DataFrame.from_dict(new_data, orient='index')

#     dir_path = 'xlsx'
#     file_name = 'ty.xlsx'
#     file_path = os.path.join(dir_path, file_name)

#     # 파일 경로 확인
#     if not os.path.exists(file_path):
#         print(f"Error: The file {file_path} does not exist.")
#         return

#     try:
#         # 기존 엑셀 파일 읽기
#         book = load_workbook(file_path)
#         writer = pd.ExcelWriter(file_path, engine='openpyxl')
#         writer.book = book

#         # 기존 시트 데이터 불러오기
#         existing_df = pd.read_excel(file_path, engine='openpyxl', index_col=0)

#         # 기존 데이터에 새 데이터 추가
#         updated_df = pd.concat([existing_df, new_df])

#         # 데이터를 엑셀 파일에 다시 저장
#         updated_df.to_excel(writer, index=True, index_label='Key')

#         # 파일 저장 및 닫기
#         writer.save()   
#         writer.close()

#         print("엑셀 파일에 데이터가 성공적으로 추가되었습니다.")
        
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # 함수 호출 예시
# xl(0, 3, 4, 2)
n = '123'

a = f"{n}"
print(type(a))
print(a)
a = int(a)
print(type(a))
print(a)