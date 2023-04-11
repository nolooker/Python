# 인터넷 url 에서 데이터를 읽어 들이는 라이브러리중의 하나
import requests
from itertools import count

'''
 서울시 공공 자전거 이용 정보(일별)
'''

accessToken = '6f584748446e6176393266465a775a'  # 인증키

totallist = list() # 모든 데이터가 저장될 list
pageSize = 1000 # 한 번에 읽어올 데이터 개수

print('크롤링이 시작 되었습니다. 잠시만 기다려 주세요')

startYear, endYear = 2022,2023
for year in range(startYear,endYear):
    startMonth, endMonth = 10,11
    for month in range(startMonth, endMonth):
        startDay, endDay = 1,3
        for day in range(startDay, endDay):

            search_date = (str(year) + str(month).zfill(2) + str(day).zfill(2))
            # print(search_date) #검색 년월일자

            for pageNumber in count(): # while True 구문과 유사한 개념의 문법
                print(pageNumber)
                beginRow = str(pageNumber * pageSize + 1)
                endRow = str((pageNumber+1) * pageSize)

                url = 'http://openapi.seoul.go.kr:8088/' + accessToken + '/json/tbCycleRentUseDayInfo/' + beginRow + '/' + endRow + '/' + search_date

                # print(url)

                message = '일자 : ' + search_date + ', 범위 : ' + beginRow + '~' + endRow
                print(message)

                response = requests.get(url) # response : 응답 객체
                # print(dir(response))

                content = response.content
                # print(type(content)) # byte 타입

                jsondata = response.json() # json 형식으로 변환
                # print(jsondata)
                # print('-'*30)

                try:
                    datalist = jsondata['cycleRentUseDayInfo']['row']
                    # print(len(datalist))
                    for data in datalist:
                        totallist.append(data)

                except Exception as err:
                    print('더 이상 데이터가 없어 오류가 발생하였습니다.')
                    print(err)
                    break

                # if pageNumber == 1 :
                #     break

        # end for day
    # end for month
# end for year

print('크롤링이 종료 되었습니다.')

print(totallist)

import pandas as pd

filename = './../data/cycleRentUseDayInfo.csv'
myframe = pd.DataFrame(totallist)
myframe.to_csv(filename)
print(filename + ' 파일이 저장되었습니다.')

