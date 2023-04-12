# https://drive.google.com/file/d/1FbGlgYd0cqLzcd-HI0ecKIPceGlULwDb/view?fbclid=IwAR2DUw7unGezSWCW4G8B5MJNWiGvY8j5u_adecnrxr_m0dqp_HexVcxdhi4

class Solution:
    def findWinter(self, T):
        res = 0
        l, r = 0, len(T) - 1
        return res

# TEST CASE
solution = Solution()

T = [5, -2, 3, 8, 6]
print(solution.findWinter(T))

T = [-5, -5, -5, -42, 6, 12]
print(solution.findWinter(T))

