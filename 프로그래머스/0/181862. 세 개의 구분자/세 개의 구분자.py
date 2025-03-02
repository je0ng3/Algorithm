def solution(myStr):
    a = myStr.replace("a","*").replace("b","*").replace("c","*")
    b = a.split("*")
    answer = [i for i in b if i!=""]
    if answer == []:
        answer = ["EMPTY"]
    return answer