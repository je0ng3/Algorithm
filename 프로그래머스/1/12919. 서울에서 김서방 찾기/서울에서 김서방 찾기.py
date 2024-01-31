def solution(seoul):
    answer = ''
    if "Kim" in seoul:
        answer = f"김서방은 {seoul.index('Kim')}에 있다"
    return answer