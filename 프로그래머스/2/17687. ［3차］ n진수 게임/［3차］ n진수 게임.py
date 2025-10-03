def solution(n, t, m, p):
    answer = ''
    # 게임 회전 수 
    last = m*(t-1)+p
    temp = ''
    for i in range(last):
        if len(temp)>= last:
            break
        temp+= make_n(i, n)
    for i in range(t):
        val = (p-1) + i*m
        answer += temp[val]
    return answer

# 10 -> n진법 
def make_n(num, n):
    if num == 0:
        return '0'
    num2n = ''
    while num>0:
        temp = num%n
        if temp < 10:
            num2n += str(temp)
        else:
            num2n += chr(temp-10+65) # A의 아스키코드 값 65 
        num//=n
    return num2n[::-1]
        
        