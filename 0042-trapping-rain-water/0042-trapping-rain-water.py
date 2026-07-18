class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        maxi = height.index(max(height))

        left_max = 0
        for i in range(0, maxi):
            left = height[i]
            if left>left_max:
                left_max = left
            else: 
                answer += left_max-left
        
        right_max = 0
        for i in range(len(height)-1, maxi, -1):
            right = height[i]
            if right>right_max:
                right_max = right
            else:
                answer += right_max-right
        
        return answer