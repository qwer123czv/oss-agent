# boxoffice — KOBIS 박스오피스 조회 스킬

## 하는 일
영화진흥위원회(KOBIS) 일별 박스오피스에서 특정 날짜의 1위부터 3위까지 영화 제목을 알려준다. 박스오피스 상위 몇 편을 물을 때 사용한다.

## 들어 있는 파일
- .claude/skills/boxoffice/SKILL.md
- .claude/skills/boxoffice/scripts/boxoffice.py
- .claude/skills/boxoffice/LICENSE

## 필요한 것
- Python, requests 패키지(직접 쓸 것: 스킬 폴더 말고도 있어야 하는 파일과 패키지)
- top3.py (조회 함수)
- secret.py (KOBIS 키 API_KEY)
## 설치
- .claude/skills 에 boxoffice 폴더를 둘 것.
- Claude Code 에서 하는 것.
- 스크립트의 출력만 근거로 답한다.
- 자료가 없다는 안내가 나오면 그대로 전한다.

## 바깥으로 요청하는 곳
- 영화진흥위원회 KOBIS "https://www.kobis.or.kr"

## 키
- 자기 키를 secret.py 에 넣을 것.

## 권한
- allowed-tools는 없음
- 실행 전 셸 명령 실행 허락을 물음.

## 라이선스
- MIT LICENSE
- 라이선스 위치 
     .claude\skills\boxoffice\LICENSE
