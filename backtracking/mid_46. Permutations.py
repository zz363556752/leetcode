'''

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
#my slow solution
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for idx in range(len(nums)):
            tmp = []
            for per in ans:
                for i in range(idx + 1):
                    curr = copy.deepcopy(per)
                    curr.insert(i, nums[idx])
                    tmp.append(curr)
            ans = tmp
            # ans = [per.insert(i, nums[idx]) for per in ans for i in range(idx + 1)]
        return ans
        
        class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for idx in range(len(nums)):
            ans = [per[:i] + [nums[idx]] + per[i:] for per in ans for i in range(len(per) + 1)]     # insert this way, no need deepcopy and insert
        return ans
