class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0,len(nums)):
            j = i+1
            for var in range(j,len(nums)):
                if nums[i] + nums[var] == target:
                    return [i,var]

'''
test case:
[2,7,11,15]
26

result [2,3]
'''