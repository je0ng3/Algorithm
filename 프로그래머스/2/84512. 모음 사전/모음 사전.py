# _ _ _ _ _
# 0<=n<=5
# 5번째 문자 n번 변경 -> n + 1(공백일 경우) = n+1
# 4번째 문자 n번 변경 -> n + 5^1(5번째 올 수 있는 개수) + 1 = n+6
# 3번째 문자 n번 변경 -> n + 5^2 + 5^1 + 1 = n+31
# 2번째 문자 n번 변경 -> n + 5^3 + 5^2 + 5^1 + 1 = n+156
# 1번째 문자 n번 변경 -> n + 5^4 + 5^3 + 5^2 + 5^1 + 1 = n+781

def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    check = [781, 156, 31, 6, 1]
    for i, w in enumerate(word):
        idx = alpha.index(w) # w앞에 있는 문자 수
        # 앞에 있는 문자로 시작하는 단어 건너뛰기
        answer += idx*check[i]
        # 현재 단어 등재
        answer += 1
    return answer