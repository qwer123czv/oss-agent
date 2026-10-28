"""tools.py - 박스오피스 정보를 가져오는 도구 모음"""
import requests
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/"
            "rest/boxoffice/searchDailyBoxOfficeList.json")

def get_boxoffice_rank_1(data): 
    """
    그 날짜의 박스오피스 1위 영화 제목을 알려준다.
    
    받는 것 : data(문자열) - 8자리 날짜. 예: "20260824"
    돌려주는 것: (문자열) 1위 영화 제목. 예 : "오디세이"
    """
    params = {"key": API_KEY, "targetDt": data}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data['boxOfficeResult']['dailyBoxOfficeList']
    return movies[0]['movieNm']

# 과제 
def get_movie_audience(date, title):
    """
    주어진 날짜와 영화 제목의 관객 수를 알려준다.

    받는 것: date(날짜 문자열) - 8자리 날짜. 예: "20260824"
              title(문자열) - 영화 제목. 예: "오디세이"
    돌려주는 것: (문자열) 관객 수. 예: 12,345명
    """
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

    for movie in movies:
        if movie["movieNm"] == title:
            return int(movie["audiCnt"])

    return f"'{title}' 은(는) {date} 순위에 없습니다."