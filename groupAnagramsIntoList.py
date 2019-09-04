'''
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        
        for stringItem in strs:
            myDict[str(sorted(stringItem))].append(stringItem)
        resultSet = list(myDict.values())
        
        return resultSet
            