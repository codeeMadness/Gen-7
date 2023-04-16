# https://drive.google.com/file/d/1FbGlgYd0cqLzcd-HI0ecKIPceGlULwDb/view?fbclid=IwAR2DUw7unGezSWCW4G8B5MJNWiGvY8j5u_adecnrxr_m0dqp_HexVcxdhi4

class Tree:
    def __init__(self, val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestDistinctPath(self, root):
        seen = {}

        def pathLength(node):
            if node is None or node.val in seen:
                return len(seen)
            seen[node.val] = node.val
            longest = max(pathLength(node.left), pathLength(node.right))
            del seen[node.val]
            return longest
            
        return pathLength(root)


# TEST CASE
solution = Solution()

tree = Tree(1, Tree(2, Tree(1), Tree(2)), Tree(2, Tree(4), Tree(1)))
print(solution.longestDistinctPath(tree))

tree = Tree(1, None, Tree(2, Tree(1), Tree(1, Tree(4))))
print(solution.longestDistinctPath(tree))

tree = None
print(solution.longestDistinctPath(tree))

