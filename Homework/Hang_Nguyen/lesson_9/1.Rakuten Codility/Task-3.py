# https://drive.google.com/file/d/1FbGlgYd0cqLzcd-HI0ecKIPceGlULwDb/view?fbclid=IwAR2DUw7unGezSWCW4G8B5MJNWiGvY8j5u_adecnrxr_m0dqp_HexVcxdhi4

class Tree:
    def __init__(self, x = 0 , left = None, right = None):
        self.x = x
        self.left = left
        self.right = right

class Solution:
    def longestDistinctPath(tree):
        if not tree:
            return -1
        pass


# TEST CASE
solution = Solution()

tree = Tree(1, Tree(2, Tree(1), Tree(2)), Tree(2, Tree(4), Tree(1)))
print(solution.longestDistinctPath(tree))

tree = Tree(1, None, Tree(2, Tree(1), Tree(1, Tree(4))))
print(solution.longestDistinctPath(tree))

tree = None
print(solution.longestDistinctPath(tree))

