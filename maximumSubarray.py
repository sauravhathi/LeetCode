class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = 0, -inf
        for i in nums:
            curSum = max(i, curSum + i)
            maxSum = max(maxSum, curSum)
        return maxSum
        
#SauravHathi
# https://leetcode.com/problems/maximum-subarray/
