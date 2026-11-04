작성: Claude Code / 확인: (김원재)

# week09/tools.py 함수 정리

- 영화진흥위원회(KOBIS) 오픈 API의 일별 박스오피스 정보를 가져오는 도구 모음임

## 공통 설정

- `requests`로 HTTP 요청을 보냄
- API 키는 `secret.py`의 `API_KEY`에서 가져옴
- `BASE_URL`: KOBIS 일별 박스오피스 조회 주소(`searchDailyBoxOfficeList.json`)임
- 두 함수 모두 `key`, `targetDt`(8자리 날짜)를 파라미터로 보내고 타임아웃 10초를 걺

## 함수 목록

### 1. `get_boxoffice_rank_1(data)`

- 역할: 그 날짜의 박스오피스 1위 영화 제목을 알려줌
- 받는 것: `data`(문자열) – 8자리 날짜, 예: `"20260824"`
- 돌려주는 것: 1위 영화 제목(문자열), 예: `"오디세이"`
- 동작: `dailyBoxOfficeList`의 첫 번째 항목의 `movieNm`을 반환함

### 2. `get_movie_audience(date, title)` (과제)

- 역할: 주어진 날짜에 특정 영화의 관객 수를 알려줌
- 받는 것: `date`(문자열) – 8자리 날짜 / `title`(문자열) – 영화 제목
- 돌려주는 것: 찾으면 관객 수(`int(audiCnt)`), 없으면 `"'{title}' 은(는) {date} 순위에 없습니다."` 문자열
- 동작
  - `raise_for_status()`로 HTTP 오류 시 예외를 발생시킴
  - 목록을 돌며 `movieNm`이 `title`과 정확히 같은 영화를 찾음

## 눈에 띄는 점

- `get_boxoffice_rank_1`의 매개변수 `data`를 응답 JSON 변수로 다시 씀 → 동작은 하나 헷갈림
- `get_boxoffice_rank_1`에는 `raise_for_status()`가 없어 오류 처리가 두 함수 간 다름
- `get_movie_audience`의 docstring은 반환값을 문자열(`"12,345명"`)로 설명하나 실제로는 `int` 반환, 못 찾으면 문자열 반환 → 반환 타입이 섞임
- 제목이 완전히 일치해야만 찾음(공백·표기 차이 시 실패)

## 확인할 것

- docstring과 실제 반환 타입(`int` vs 문자열) 중 어느 쪽에 맞출지 결정
- `get_boxoffice_rank_1`에 HTTP 오류 처리와 매개변수 이름 정리(`data` → `date`)가 필요한지 검토
