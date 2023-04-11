import pandas as pd
import requests

#https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=sfpGwEhbWejlYf8aFoPZzO65UKSGXmMu&searchdate=20180102&data=AP01

authkey = 'sfpGwEhbWejlYf8aFoPZzO65UKSGXmMu'
searchdate = '20221231'
data = 'AP01'

url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={}&searchdate={}&data={}'.format(authkey, searchdate, data)
print(url)


response = requests.get(url)
r_data = response.json()
exchange = pd.DataFrame(r_data)
print(exchange)

# 컬럼 정보
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


print(exchange.columns)

