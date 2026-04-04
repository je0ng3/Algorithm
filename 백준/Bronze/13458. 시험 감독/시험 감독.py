n = int(input()) # 시험장 수 
a_list = list(map(int, input().split())) # 각 시험장에 있는 응시자 수
b, c = map(int, input().split())    # 총감독, 부감독의 감시 가능 수 

# 조건: 총감독은 1명만

count = 0
for a in a_list:
    aa = a-b
    count+=1
    if aa<=0:
        continue

    count += aa//c 
    count += 1 if aa%c>0 else 0

print(count)