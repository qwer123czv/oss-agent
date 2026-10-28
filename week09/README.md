# week09 - 박스오피스 조회

## 무엇을 하는 코드인가
영화진흥위원회(KOBIS) 오픈 API로 일별 박스오피스를 조회합니다.
- `get_boxoffice_rank_1(date)`: 그 날짜의 1위 영화 제목
- `get_movie_audience(date, title)`: 그 날짜에 특정 영화의 하루 관객 수

## 설치
```
pip install -r requirements.txt
```
같은 폴더에 `secret.py` 를 만들고 KOBIS API 키를 넣습니다.
```python
API_KEY = "발급받은_키"
```

## 실행
```
python main.py
```
