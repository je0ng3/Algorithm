def solution(numbers):
    answer = []
    for num in numbers:
        if num%2==0:
            answer.append(num+1)
        else:
            binary = '0' + bin(num)[2:]
            for i in range(len(binary)-2, -1, -1):
                if binary[i]=='0':
                    nxt = binary[:i]+'10'+binary[i+2:]
                    break
            answer.append(int(nxt, 2))
    return answer