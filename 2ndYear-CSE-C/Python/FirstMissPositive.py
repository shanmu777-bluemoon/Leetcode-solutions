class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Place each number in its target index: nums[i] should be i + 1
        for i in range(n):
            # While the current number is in range [1, n] and not in its correct spot
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its target index
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # 2. Find the first index where the number is not i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # 3. If all numbers 1 to n are present, the missing one is n + 1
        return n + 1
