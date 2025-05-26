# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #ensures that there are still values left to search in the tree
        while root is not None:
            #if the val is equal to the current one its on return the root
            if val == root.val:
                return root
            #if the value is smaller it will be on the left
            elif val < root.val:
                root = root.left
            #otherwise the value is larger and will be on the right
            else: 
                root = root.right
        #if the value is not in the tree
        return None

        
