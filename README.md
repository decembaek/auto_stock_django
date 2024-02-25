# 작성 블로그
- 기획 및 계획 
https://wingyu-story.tistory.com/130
- 주식 종목 코드 및 섹터 데이터 가져오기 
https://wingyu-story.tistory.com/131
- DB 데이터 베이스 서버 구축하기
https://wingyu-story.tistory.com/132



# 투자 및 금융에 대한 프로젝트
1. 한국주식 정보 수집 (완료)
2. 한국 업종 및 관련 데이터 수집 (완료)
3. 주식 종목 코드 수집 (완료)
4. 주식 가격 데이터 수집 ()
- celery 비동기 구현 ()
- redis DB 구현 ()
5. 모의 투자 기능 개발 ()
6. 모의 투자 게임 기능 개발 () 
- 추후계획
1. 주식 과거 데이터 수집
2. 주식 백테스팅 제작
3. 백테스팅 기능 배포
4. 백테스팅 게임 제작
---------------------------------------
# 데이터 수집
- 주식종목코드
/data/stock_data.xlsx
- 업종섹터코드
/data/idxcode.xlsx
- 한국표준산업분류코드, 테마코드
/data/theme_code.xlsx
- 주식 실시간 데이터
한국투자증권 kis
- 주식 과거 데이터
미정.

---------------------------------------

# 데이터베이스 형태 
##  korea_stock 모델
### 모델 한글명 : 모델명 (현 상황) 작업여부
#### 업종 섹터 코드 : KisSectorModel (데이터 추가 완료) O
#### 표준산업분류코드, 테마코드 : KSICodeModel (데이터 추가 완료) O
#### 주식종목코드 모델 : StockCodeModel (데이터 추가 완료) O
#### 유저 모델 : User (모델 코딩 완료) O 
#### 주식정보 모델 : StockInfoModel (데이터 추가 예정) X
#### 주식가격 실시간 모델 : StockPriceRealtimeModel (미완성, 구조 고민 필요) X

---------------------------------------

### 추후 추가 모델 
1. 주식 Stock 년, 월, 일, 분 봉 기준으로 데이터 저장 모델
2. 벡테스팅 기록 모델
3. 모의투자 계좌 관리 모델
4. 유저 정보 모델

================================================
### celery 현재 사용 안함
## celery 명령어 
celery -A korea_stock worker --loglevel=info
## Redis Docker 구현 
docker run -d -p 6379:6379 redis

## 비동기 명령어 추가
python manage.py run_async_tasks
