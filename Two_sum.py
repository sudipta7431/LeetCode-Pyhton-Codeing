class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#        b = len(nums)
#        for i in range(b):
#            for j in range(1,b):
#                sum = nums[i] + nums[j]
#                if sum == target:
#                    return [i,j]

        myDict = dict()
        for i in range(len(nums)):
            rest_element = target - nums[i]
            num  = nums[i]
            if num in myDict:
                return [myDict[num],i]
            else:
                myDict[rest_element] = i
        
