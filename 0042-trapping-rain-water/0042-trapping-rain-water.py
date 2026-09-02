class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        # 가장 높은 곳
        maxi = height.index(max(height))

        # 왼쪽
        left = height[0]
        for i in range(maxi):
            if left>height[i]:
                rain += left-height[i]
            else:
                left = height[i]
        # 오른쪽
        right = height[-1]
        for i in range(len(height)-1, maxi, -1):
            if right>height[i]:
                rain += right-height[i]
            else:
                right = height[i]
        
        return rain