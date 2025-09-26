class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                c = -nums[i] - nums[j]
                if c in seen:
                    res.add((nums[i], c, nums[j]))
                seen.add(nums[j])
        return list(res)
                
