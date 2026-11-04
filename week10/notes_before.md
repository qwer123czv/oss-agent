# week09/tools.py 함수 정리

`week09/tools.py`는 영화진흥위원회(KOBIS) 오픈 API의 **일별 박스오피스** 정보를 가져오는 도구 모음이다.

## 공통 설정

- `requests`로 HTTP 요청을 보낸다.
- API 키는 `secret.py`의 `API_KEY`에서 가져온다.
- `BASE_URL`: KOBIS 일별 박스오피스 조회 주소 (`searchDailyBoxOfficeList.json`)
- 두 함수 모두 `key`, `targetDt`(8자리 날짜)를 파라미터로 보내고, 10초 타임아웃을 건다.

## 함수 목록

### 1. `get_boxoffice_rank_1(data)`

그 날짜의 박스오피스 **1위 영화 제목**을 알려준다.

| 항목 | 내용 |
|---|---|
| 받는 것 | `data` (문자열) – 8자리 날짜. 예: `"20260824"` |
| 돌려주는 것 | (문자열) 1위 영화 제목. 예: `"오디세이"` |

동작: 박스오피스 목록(`dailyBoxOfficeList`)의 첫 번째 항목의 `movieNm`을 반환한다.

### 2. `get_movie_audience(date, title)` (과제)

주어진 날짜에 특정 영화의 **관객 수**를 알려준다.

| 항목 | 내용 |
|---|---|
| 받는 것 | `date` (문자열) – 8자리 날짜. 예: `"20260824"`<br>`title` (문자열) – 영화 제목. 예: `"오디세이"` |
| 돌려주는 것 | 목록에 있으면 관객 수(`audiCnt`), 없으면 안내 문자열 |

동작:
1. `raise_for_status()`로 HTTP 오류가 있으면 예외를 발생시킨다.
2. 박스오피스 목록을 돌며 `movieNm`이 `title`과 정확히 같은 영화를 찾는다.
3. 찾으면 `int(audiCnt)`를 반환하고, 없으면 `"'{title}' 은(는) {date} 순위에 없습니다."`를 반환한다.

## 참고: 눈에 띄는 점

- `get_boxoffice_rank_1`의 매개변수 이름이 `data`인데, 함수 안에서 응답 JSON도 `data`에 다시 담는다. 동작은 하지만 헷갈리기 쉬우므로 `date`로 바꾸는 편이 낫다.
- `get_boxoffice_rank_1`에는 `raise_for_status()`가 없어 HTTP 오류 처리가 `get_movie_audience`와 다르다.
- `get_movie_audience`의 docstring은 반환값을 문자열(`"12,345명"`)이라고 설명하지만, 실제로는 정수(`int`)를 반환한다. 영화를 찾지 못한 경우에는 문자열을 반환하므로 반환 타입이 섞여 있다.
- 영화 제목은 완전히 일치해야 찾는다(공백·표기 차이가 있으면 못 찾음).
