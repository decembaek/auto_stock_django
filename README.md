# 투자 및 금융에 대한 프로젝트
1. 한국주식 정보 수집
2. 한국 업종 및 관련 데이터 수집
3. 주식 투자 정보 수집
4. 주식 백테스팅 제작
5. 백테스팅 기능 배포
6. 백테스팅 게임 제작

# 데이터 수집
## 주식종목코드
/data/stock_data.xlsx
## 업종섹터코드
/data/idxcode.xlsx
## 한국표준산업분류코드, 테마코드
/data/theme_code.xlsx
## 주식 실시간 데이터
한국투자증권 kis
## 주식 과거 데이터
미정.


# 데이터베이스 형태 
##  korea_stock 모델
### 모델 한글명 : 모델명 (현 상황) 작업여부
업종 섹터 코드 : KisSectorModel (데이터 추가 완료) O
표준산업분류코드, 테마코드 : KSICodeModel (데이터 추가 완료) O
주식종목코드 모델 : StockCodeModel (데이터 추가 완료) O
주식정보 모델 : StockInfoModel (데이터 추가 예정) X
주식가격 실시간 모델 : StockPriceRealtimeModel (미완성, 구조 고민 필요) X
### 추후 추가 모델 
주식 Stock 년, 월, 일, 분 봉 기준으로 데이터 저장 모델
벡테스팅 기록 모델
모의투자 계좌 관리 모델
유저 정보 모델
