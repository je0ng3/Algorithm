def solution(arr):
    answer = [0, 0]
    
    def compress(lst):
        if all(x == lst[0][0] for row in lst for x in row):
            answer[lst[0][0]]+=1
            return
        
        mid = len(lst)//2
        compress([row[:mid] for row in lst[:mid]])
        compress([row[mid:] for row in lst[:mid]])
        compress([row[:mid] for row in lst[mid:]])
        compress([row[mid:] for row in lst[mid:]])
    
    compress(arr)
    return answer