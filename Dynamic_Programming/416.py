class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2
        num_len = len(nums)
        nums.sort(reverse=True)
        def current_sum(idx, current_value, memo = None):
            if memo is None:
                memo = {}
            if (idx, current_value) in memo:
                return memo[(idx, current_value)]
            if idx >= num_len:
                return False
            if current_value == target:
                return True
            if current_value > target:
                return False
            without_num = current_sum(idx + 1, current_value, memo)
            with_num = current_sum(idx + 1, current_value + nums[idx], memo)

            result = with_num or without_num
            memo[(idx, current_value)] = result
            return result
        return current_sum(0, 0)