class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            if (curSum > maxSum or curSum < 0 ):
                maxSum = curSum
        return maxSum
#SauravHathi
# https://leetcode.com/problems/maximum-subarray/
