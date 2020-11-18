# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#NOTES:
#BST left side is always smaller
#BST right side is always bigger
#All node values are unique
#Recursive approach
#If current node is not in range, then stop checking one of the sides

#PSEUDO CODE - Brute Force:
#Base Case:
    #return 0 if node is null
#total variable = 0
#if node value is in range, add to total variable
#return total varaible + (recursive call on children)

#Optimization:
#if current node is lower than the low, skip everything on the left
#if current node is higher than the high, skip everything on the right
    

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        total = 0
        if low <= root.val <= high:
            total += root.val
        if root.val > low:
            total += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            total += self.rangeSumBST(root.right, low, high)
        return total