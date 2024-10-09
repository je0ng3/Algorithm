str = input()
answer = ""
for i in range(len(str)):
    if str[i].isupper():
        answer+=str[i].lower()
    else:
        answer+=str[i].upper()
print(answer)