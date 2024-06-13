n = int(input())
f = int(input())

# n의 마지막 두 자리를 00으로 바꾼 값 계산
base = n - (n % 100)

# 00부터 99까지 반복하여 base + i가 f로 나누어 떨어지는지 확인
for i in range(100):
    if (base + i) % f == 0:
        print(f"{i:02d}")
        break
