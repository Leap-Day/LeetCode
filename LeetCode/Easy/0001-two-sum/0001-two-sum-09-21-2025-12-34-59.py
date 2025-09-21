class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            # Add the current number to the dicionary with its index as the value
            seen[nums[i]] = i
        