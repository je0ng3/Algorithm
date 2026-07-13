message = input()
key = input()

# Please write your code here.
ALPHABET = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")

# step1.
# 키 -> 5x5표 변환
# 행 키우고 열 키우며 진행
# 키 값으로 채움. 이전에 등장한 알파벳은 무시
# 남는 칸은 등장하지 않은 알파벳 채워넣음
key_map = [[] for _ in range(5)]
key_set = set()
r = 0
for k in key:
    if k not in key_set:
        key_set.add(k)
        if len(key_map[r])==5:
            r+=1
        key_map[r].append(k)
left = [a for a in ALPHABET if a not in key_set]
for l in left:
    if len(key_map[r])==5:
        r+=1
    key_map[r].append(l)

# step2.
# 메세지를 두 글자씩 나눔
# 두 글자가 연속되는 문자면, 그중 가장 앞에 있는 쌍 사이에 x를 넣고, 뒤쪽은 새롭게 쌍을 구성
# xx 일 시, q를 넣음
# 마지막에 한 글자가 남으면 x를 덧붙임
two_words = []
temp=''
for i, m in enumerate(message):
    if temp=='':
        temp+=m
    elif temp==m:
        if temp=='X':
            two_words.append(temp+'Q')
        else:
            two_words.append(temp+'X')
    else: # temp!=m
        two_words.append(temp+m)
        temp=''
if temp != '':
    # if temp=='X':
    #         two_words.append(temp+'Q')
    # else:
    two_words.append(temp+'X') # 마지막에는 그냥 X추가?

# stp3.
# 같은 행에 두 글자 존재 -> 오른 단어로 암호화
# 같은 열에 두 글자 존재 -> 아래 단어로 암호화
# 다른 행, 열에 존재 (r1, c1), (r2, c2) -> (r1, c2), (r2, c1)으로 암호화
answer = ''
for word in two_words:
    a, b = word[0], word[1]
    a_r, a_c, b_r, b_c = -1, -1, -1, -1
    for i, r in enumerate(key_map):
        if a in r:
            a_r = i
            a_c = r.index(a)
        if b in r:
            b_r = i
            b_c = r.index(b)
    if a_r==b_r: # case1
        answer+=key_map[a_r][(a_c+1)%5]
        answer+=key_map[b_r][(b_c+1)%5]
    elif a_c==b_c: # case2
        answer+=key_map[(a_r+1)%5][a_c]
        answer+=key_map[(b_r+1)%5][b_c]
    else:
        answer+=key_map[a_r][b_c]
        answer+=key_map[b_r][a_c]
print(answer)