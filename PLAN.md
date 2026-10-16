# app.py 계획

## Context
AGENTS.md: 할 일을 우선순위 순서로 보여 주는 Python 터미널 앱. 현재 프로젝트에는 AGENTS.md 외에 파일이 없어 app.py는 새로 만든다.

## 읽은 파일
- AGENTS.md (유일한 기존 파일; app.py·테스트·데이터 파일 없음)

## 만들거나 수정할 파일
- 새로 만들기: app.py (단일 파일, 표준 라이브러리만 사용)
- 수정 없음. 그 외 파일은 만들지 않음 (AGENTS.md "변경 범위")

## 구현할 함수
- `load_todos()` / `save_todos()`: JSON 파일 읽기·쓰기 (파일이 없으면 빈 목록)
- `add_todo(todos, title, priority)`: 할 일 추가
- `sort_by_priority(todos)`: 우선순위 순 정렬 (같으면 입력 순서 유지)
- `show_todos(todos)`: 정렬된 목록을 번호와 함께 출력
- `main()`: 메뉴 루프 (보기 / 추가 / 종료)

## 실행할 확인 명령
- `uv --version`
- `uv run python --version`
- `uv run app.py` 실행 후 우선순위가 다른 할 일 3개를 추가하고, 높은 순서대로 표시되는지 확인
- 종료 후 `uv run app.py`를 다시 실행해 데이터가 유지되는지 확인
- 표준 라이브러리만 쓰므로 `uv add`/`uv pip install`은 하지 않음 (pyproject.toml도 만들지 않음)

## 결정이 필요한 질문
1. 우선순위 표현: 숫자(1=높음)와 높음/중간/낮음 중 무엇을 쓸까요?
2. 저장: 재실행 시 데이터를 유지할까요(JSON 파일 추가), 메모리에만 둘까요? 파일을 추가하면 AGENTS.md의 "파일 추가는 꼭 필요할 때만"과 부딪힙니다.
3. 기능 범위: 보기·추가만 할까요, 완료 처리·삭제도 넣을까요?
4. 입력 방식: 대화형 메뉴와 명령줄 인자(`uv run app.py add ...`) 중 어느 쪽인가요?
