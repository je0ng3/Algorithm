color = ["black", "brown", "red", "orange", "yellow", "green", "blue",
         "violet", "grey", "white"]
a = input()
b = input()
c = input()
answer = color.index(a) * 10
answer += color.index(b)
answer *= pow(10, color.index(c))
print(answer)