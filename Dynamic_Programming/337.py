# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root, can_take=True, memo=None):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        """
            Pseudo code
                -base case if root is None then return 0
                -pass in second argument called can_take referring to if the current root val can be added
                -make four variables storing four recursive calls
                    -take left
                    -take right
                    -dont take left
                    -dont take right
                -two options
                    -current val added to dont take left + dont take right
                    -take left + take right
                -find max of those two options, and return it
            
            Time Complexity: O(2^n)
            Space Compleixty: O(n)

            Can be improved to O(n)
        """
        if memo is None:
            memo = {}
        if not root:
            return 0
        if (root, can_take) in memo:
            return memo[(root, can_take)]
        left_not_taken = self.rob(root.left, True, memo)
        right_not_taken = self.rob(root.right, True, memo)
        if can_take:
            left_taken = self.rob(root.left, False, memo)
            right_taken = self.rob(root.right, False, memo)
            total_taken = root.val + left_taken + right_taken
            total_not_taken = left_not_taken + right_not_taken
            result = max(total_taken, total_not_taken)
        else:
            result = left_not_taken + right_not_taken
        memo[(root, can_take)] = result
        return result