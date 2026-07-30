from collections import Counter

def solution(str1, str2):
    def make_set(s):
        s = s.lower()
        result = []
        for i in range(len(s)-1):
            pair = s[i:i+2]
            if pair.isalpha():
                result.append(pair)
        return result
    
    count1 = Counter(make_set(str1))
    count2 = Counter(make_set(str2))
    
    intersection = sum((count1&count2).values())
    union = sum((count1|count2).values())
    
    jaccard = 1 if union==0 else intersection/union
    return int(jaccard*65536)