from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        for i in range(len(nums) - 1,-1, -1):
            print(i, nums[i])
            if (i + nums[i] >= goal):
                goal = i
        return True if goal == 0 else False



nums = [3,2,2,0,4]
obj = Solution()
print(obj.canJump(nums))