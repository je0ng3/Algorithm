class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        max_i = height.index(max(height))
        
        # 왼쪽 탐색
        maxi = 0
        for h in height[:max_i]:
            if h>maxi:
                maxi = h
            else:
                answer += maxi-h

        # 오른쪽 탐색
        maxi = 0
        for h in (height[max_i+1:len(height)])[::-1]:
            if h>maxi:
                maxi = h
            else:
                answer += maxi-h

        return answer