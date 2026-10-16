PRIORITY_ORDER = {"HIGH": 0, "MID": 1, "LOW": 2}

# (제목, 우선순위, 완료 여부)
TODOS = [
    ("주간 보고서 초안 작성", "HIGH", False),
    ("회의 자료 작성", "MID", False),
    ("책상 정리", "LOW", False),
    ("이메일 답장", "HIGH", True),
]


def pending_by_priority(todos):
    pending = [todo for todo in todos if not todo[2]]
    return sorted(pending, key=lambda todo: PRIORITY_ORDER[todo[1]])


def main():
    for title, priority, _ in pending_by_priority(TODOS):
        print(f"{title}({priority})")


if __name__ == "__main__":
    main()
