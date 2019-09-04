class Solution:
    def maxArea(self, height):
        '''
        Holders for result maximum area, starting index pointer and ending index pointer
        '''
        maxArea = 0
        start = 0
        end = len(height)-1
        #print(end)

        '''
        Begin from first and last nodes, compute the area, 
        compare with maximum and change the pointers according to heights
        '''
        while start < end :
            area = (end-start) * min(height[end], height[start])
            
            if area > maxArea:
                maxArea = area
            
            if height[start] < height[end]:
                start += 1
            else:
                end -=1
        
        return maxArea

#test case
#Expected Result: 49
if __name__ == '__main__':
    testArray = [1,8,6,2,5,4,8,3,7]
    s = Solution() 
    areaCompute = s.maxArea(testArray)
    print(areaCompute)