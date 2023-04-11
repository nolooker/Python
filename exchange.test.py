'''
한국수출입은행
제공 서비스) 현재환율 API
https://www.koreaexim.go.kr/site/program/financial/exchangeJSON
'''

import pandas as pd
import requests

#https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=AUTHKEY1234567890&searchdate=20180102&data=AP01


authkey = 'sfpGwEhbWejlYf8aFoPZzO65UKSGXmMu'
searchdate = '20220810'
data = 'AP01'

url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={}&searchdate={}&data={}'.format(authkey, searchdate, data)

response = requests.get(url)
r_data = response.json()
exchange = pd.DataFrame(r_data)
exchange

print(exchange)

# authkey	String(필수)	인증키	OpenAPI 신청시 발급된 인증키
# searchdate	String	검색요청날짜	ex) 2015-01-01, 20150101, (DEFAULT)현재일
# data	String(필수)	검색요청API타입	AP01 : 환율, AP02 : 대출금리, AP03 : 국제금리

#result 조회 결과
#'CUR_UNIT':'통화코드',
#'CUR_NM':'국가/통화명',
#'TTB':'전신환(송금)받으실때',
#'TTS':'전신환(송금)보내실때',
#'DEAL_BAS_R':'매매 기준율',
#'BKPR':'장부가격',
#'YY_EFEE_R':'년환가료율',
#'TEN_DD_EFEE_R':'10일환가료율',
#'KFTC_DEAL_BAS_R':'서울외국환중개 매매기준율',
#'KFTC_BKPR':'서울외국환중개 장부가격'

print(url)

def dataExtractor(searchdate, getAllData=False):
    parameters = '&searchdate=' + str(searchdate)

    if getAllData == False :

        parameters = '&searchdate=' + str(searchdate)

    newurl = url + parameters
    print(newurl)

    response = requests.get(url)
    content = response.content
    print(type(content))

# end def dataExtractor

print('크롤링 중입니다.')

start, end = 20220101,20221231  # 조사 시작, 조사 끝

totallist = list()

for searchdate in range(start, end):
    print( (searchdate))





