class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while(i < len(nums)):
            j = i + 1
            while(j < len(nums) and nums[i] == nums[j]):
                nums.pop(j)
            i = j
        return len(nums)