sl, sr = input().split()
string = list(input())

alphal = [["q", "w", "e", "r", "t"], ["a", "s", "d", "f", "g"], ["z", "x", "c", "v"]]
alphar = [
    [0, 0, 0, 0, 0, "y", "u", "i", "o", "p"],
    [0, 0, 0, 0, 0, "h", "j", "k", "l"],
    [0, 0, 0, 0, "b", "n", "m"],
]


def find(a, b):
    x, y = 0, 0
    for idx, i in enumerate(b):
        if a in i:
            x = idx
            y = i.index(a)
            break
    return x, y


time = 0
while string:
    time += 1
    typing = string.pop(0)
    if any(typing in i for i in alphal):
        x1, y1 = find(sl, alphal)
        x2, y2 = find(typing, alphal)
        time += abs(x1 - x2) + abs(y1 - y2)
        sl = typing
    else:
        x1, y1 = find(sr, alphar)
        x2, y2 = find(typing, alphar)
        time += abs(x1 - x2) + abs(y1 - y2)
        sr = typing
print(time)
