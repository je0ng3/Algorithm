def solution(name):
    answer = 0
    # 모든 문자 변형에 드는 시간
    for c in name:
        answer += min(ord(c)-ord('A'), ord('Z')-ord(c)+1)
    # 커서 이동에 드는 시간
    n = len(name)
    move = n-1 # 계속 전진
    for i in range(n): # 어느 구간에서 꺾는 것이 최적인지 파악
        # i 다음 위치부터, 연속된 'A' 구간의 끝 찾기
        j = i+1 
        while j<n and name[j]=='A':
            j += 1
        # A를 만났을 때 직진, 후진 중 더 적게 이동하는 것 선택
        move = min(
            move,
            i*2 + (n-j), # 전진 후 되돌아가기
            i + 2*(n-j) # 처음부터 후진
        )
    return answer + move