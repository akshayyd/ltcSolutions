'''
#not all test cases pass- 310 out 0f 313 passed- O(n**3)
resultList = list()
        nums = sorted(nums)
        print(nums)
        for i in range(0,len(nums)):
            loopVar1 = i + 1
            for j in range(loopVar1, len(nums)):
                loopVar2 = j + 1
                for k in range(loopVar2, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        if [nums[i],nums[j],nums[k]] not in resultList:
                            resultList.append([nums[i], nums[j], nums[k]])
        return resultList

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
          
        s = sorted(nums) # O(nlogn)
        output = set()
        for k in range(len(s)):  #complete list
            target = -s[k]      #negate each element

            i,j = k+1, len(s)-1  # check from next element till the end of list 
             
            # i pointer from next element till half the list, j pointer  
            # from last element till half the list decremented
            while i < j:                                            
                sum_two = s[i] + s[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    output.add((s[k],s[i],s[j]))
                    i += 1
                    j -= 1
        return output