class Solution(object):
    def pivotIndex(self, nums):
        
        total = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1       

sol = Solution()
print(sol.pivotIndex([1,7,3,6,5,6])) 