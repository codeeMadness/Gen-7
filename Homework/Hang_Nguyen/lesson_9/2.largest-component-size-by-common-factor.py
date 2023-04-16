# https://leetcode.com/problems/largest-component-size-by-common-factor/
class Solution():
    def largestComponentSize(self, nums):
        return len(nums)

# TEST CASE
solution = Solution()

nums = [4,6,15,35]
print(solution.largestComponentSize(nums))
nums = [20,50,9,63]
print(solution.largestComponentSize(nums))
nums = [2,3,6,7,4,12,21,39]
print(solution.largestComponentSize(nums))