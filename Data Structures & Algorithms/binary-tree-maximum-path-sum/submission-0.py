class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float("-inf")

        def depthFirstSearch(node):
            nonlocal result
            if not node:
                return 0

            leftMax = max(depthFirstSearch(node.left), 0)
            rightMax = max(depthFirstSearch(node.right), 0)

            result = max(result, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)

        depthFirstSearch(root)
        return result