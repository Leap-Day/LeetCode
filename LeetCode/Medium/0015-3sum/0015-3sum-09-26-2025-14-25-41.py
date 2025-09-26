class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = 0
        r = 0


        for i in range(len(nums)):
            # Skip any start numbers that we've already done
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            # Search for pairs in the rest of the array
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: l += 1 # Skip repreat left numbers that came before
                    while nums[r] == nums[r + 1] and l < r: r -= 1 # Skip repeat right numbers that came before
                if nums[l] + nums[r] > -nums[i]: # 
                    r -= 1
                else:
                    if nums[l] + nums[r] < -nums[i]:
                        l += 1
        return res

            
            
                
