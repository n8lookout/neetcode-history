# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        if not root:
            return result
            
        q = deque()
        q.append(root)

        while len(q) > 0:
            right_side = None
            for i in range(len(q)):
                current = q.popleft()
                if current:
                    right_side = current
                    q.append(current.left)
                    q.append(current.right)
            if right_side:
                result.append(right_side.val)

        return result

        