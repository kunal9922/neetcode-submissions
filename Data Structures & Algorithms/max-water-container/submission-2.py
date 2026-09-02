class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force O(n^2)
        # maxWater = 0
        # for l in range(len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         width = r - l
        #         currMax = width * min(heights[l], heights[r])
        #         maxWater = max(currMax, maxWater)
        
        # return maxWater


        l = 0
        r = len(heights) - 1
        maxWater = 0
        while l < r:
            width = r - l
            currMaxWater = width * min(heights[l], heights[r])
            maxWater = max(maxWater, currMaxWater)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return maxWater


