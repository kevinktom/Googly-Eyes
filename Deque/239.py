"""
    Example:
     Input: nums = [9,10,9,-7,-4,-8,2,-6], 5
                                  ^
     deque = [1, 2, 3, 4]
     answer = []
     
    Time Complexity: O(n) - n being the number of elements in nums
    Space Complexity: O(n) - Would be O(n-k-1) for the results array
     
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Use deque so that we can pop left and right
        # Using monotonic queue for sliding window due to sorted constraint
        
        # Initialize the deque, storing indices sorted by largest value to smallest
        deque = collections.deque()
        results = []
        
        # Performs operations on the first window
        for i in range(k):
            # We only care to store the largest value in the first position and onward
            while deque and nums[i] >= nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            
        # Looping through the rest of the windows
        for i in range(k, len(nums)):
            # Add the previous window's max
            results.append(nums[deque[0]])
            # Removes indices that are not in the range of the current window
            if deque[0] < i - k + 1:
                deque.popleft()
            # Guarantee window is decreasing by removing the previous elements which are less than curent
            # Reinsuring that this is a monotonic deque
            while deque and nums[i] >= nums[deque[-1]]:
                deque.pop()
            deque.append(i)
        # Perform the operations for the last sliding window
        results.append(nums[deque[0]])
        return results