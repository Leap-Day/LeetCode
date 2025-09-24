class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        cur = 0

        for x in numSet:
            if (x - 1) not in numSet:
                while x in numSet:
                    cur += 1
                    x += 1
                longest = max(cur, longest)
                cur = 0
    
        return longest