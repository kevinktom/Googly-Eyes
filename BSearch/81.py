"""
    NOTES:
        -Has to be bsearch for logn time complexity
        -Sorted order, so compare left and right sides of partial arrays to determine which to bsearch
    PseudoCode:
        -Declare a middle idx to split the array
        -Base Case: 
            -if element at middle idx is the target: return true
            -if array is empty: return false
        -first = first element
        -second = element before the pivot
        -if pivot >= first:
            if target is also in the range:
                return bsearch first and pivot
            else:
                return bsearch pivot and right side
        -else:
            if target is in the range of the right side:
                return bsearch pivot to right
            else:
                return bsearch left side
                
    Approach Refined for edge cases:
        -Do bsearch
        -Check first and last values if they equal to target
        -Add an additional else for edge cases where there are lots of multiple duplicates
    
    Time Complexity: 
        -Worst Case: O(n) (every element is the duplicated except one which is the target)
        -On Average: O(logn)
    Space Complexity:
        -Worst Case Scenario: O(n) due to the nature of recursion
        -Best Case Scenario: O(1) if done iteratively
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        pivot = len(nums)//2
        pivot_value = nums[pivot]
        if pivot_value == target or target == nums[0] or target == nums[-1]:
            return True
        if pivot_value > nums[0]:
            if nums[0] <= target < pivot_value:
                return self.search(nums[0:pivot], target)
            else:
                return self.search(nums[pivot+1:], target)
        elif pivot_value < nums[0]:
            if pivot_value < target <= nums[-1]:
                return self.search(nums[pivot+1:], target)
            else:
                return self.search(nums[0:pivot], target)
        else:
            return self.search(nums[1:-1], target)