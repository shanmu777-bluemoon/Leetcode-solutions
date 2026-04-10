class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sort to handle duplicates easily
        nums.sort()
        
        def backtrack(start, current_subset):
            # Add a copy of the current subset to the result
            res.append(list(current_subset))
            
            for i in range(start, len(nums)):
                # If the current element is the same as the previous one, skip it
                # i > start ensures we don't skip the first occurrence in a recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include nums[i]
                current_subset.append(nums[i])
                # Move to the next element
                backtrack(i + 1, current_subset)
                # Backtrack: remove nums[i]
                current_subset.pop()
                
        backtrack(0, [])
        return res
