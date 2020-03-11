# Project_KBO_Predict
KBO의 경기결과를 세이버메트릭스로 예측하는 프로젝트
Crawling.ipynb: 필요한 자료를 csv파일 형태로 크롤링
DataPreprocessing.ipynb: csv파일의 전처리
ModelSelection.ipynb: 어떤 알고리즘으로 학습할 것인지 테스트하기
MachineLearning.ipynb: 실제 기계학습

SearchList.py :뷰티풀수프 활용한 크롤링 모듈
BaseballGameResult.py: score를 승무패 혹은 승1패로 바꿔주는 모듈 
승1패는 스포츠복권의 방식으로 1점차승부나 무승부를 1로 처리하는 것

결론
승무패 정확도는 로지스틱 모델을 사용시 55% 이상이었다



다음 프로젝트를 위한 링크
https://www.basketball-reference.com/leagues/NBA_2019_advanced.html#advanced_stats::ws - winshare

http://insider.espn.com/nba/hollinger/statistics - per

https://stats.nba.com/teams/advanced/?sort=OFF_RATING&dir=-1 - offrtg/defrtg
