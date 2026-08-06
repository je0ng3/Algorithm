n = int(input()) # 식당의 수
nums = list(map(int, input().split())) # 각 식당의 고객 수 
a, b = map(int, input().split()) # 팀장과 팀원이 검사할 수 있는 최대 고객 수 

# 한 가게당 팀장 무조건 한명, 팀원 0~여러명 가능
# 필요한 검사자 수의 최솟값
answer = n # 팀장 n명
for num in nums:
    num-=a
    if num>0:
        answer += (num+b-1)//b

print(answer)