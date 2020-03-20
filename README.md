# <한국직업전문학교 무재칠시 프로젝트> With 
#### Project_KBO_Predict 
KBO의 경기결과를 세이버메트릭스로 예측하는 프로젝트

# 파일설명
Crawling.ipynb: 필요한 자료를 csv파일 형태로 크롤링
DataPreprocessing.ipynb: csv파일의 전처리
ModelSelection.ipynb: 어떤 알고리즘으로 학습할 것인지 테스트하기
MachineLearning.ipynb: 실제 기계학습
SearchList.py :뷰티풀수프 활용한 크롤링 모듈
BaseballGameResult.py: score를 승무패 혹은 승1패로 바꿔주는 모듈 
승1패는 스포츠복권의 방식으로 1점차승부나 무승부를 1로 처리하는 것

# Data source
선발선수/경기결과: http://www.statiz.co.kr/boxscore.php?       
WAR: http://www.statiz.co.kr/stat.php?      

# 사용데이터
각 경기 홈팀과 원정팀의 최근(직전 달)WAR

# 결론
승무패 정확도는 로지스틱 모델을 사용시 55% 이상이었다

### 승무패
<img src='https://github.com/Woosub-Kim/Project_KBO_Predict/blob/master/KBO.PNG' />

### 승1패
<img src='https://github.com/Woosub-Kim/Project_KBO_Predict/blob/master/KBO2.PNG' />

무승부와 1점승부를 예측하는 것은 불가능하므로 이러한 방식으로 스포츠복권에서 유의미한 적중률을 기대하긴 어려워보인다.    
다만 찍어서 맞추는 것 이상의 적중률은 기대할 수 있다

###### 한국직업전문학교 무재칠시 링크
|설명|링크|
|----|----|
|KBO경기 예측| https://github.com/Woosub-Kim/Project_KBO_Predict |            
|MLB경기 예측| https://github.com/Woosub-Kim/project_MLB_predict |                           
|NBA경기 예측| https://github.com/Woosub-Kim/project_NBA_predict |                    
|API| https://github.com/Woosub-Kim/sports_predict_api |                  
|WEB| https://github.com/namwon94/Project_Baseball |                         


