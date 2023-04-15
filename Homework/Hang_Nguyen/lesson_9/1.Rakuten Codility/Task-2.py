# https://drive.google.com/file/d/1FbGlgYd0cqLzcd-HI0ecKIPceGlULwDb/view?fbclid=IwAR2DUw7unGezSWCW4G8B5MJNWiGvY8j5u_adecnrxr_m0dqp_HexVcxdhi4

class Solution:
    def findWinter(self, T):
        res = len(T)
        l, r = 0, len(T) - 1
        highestWinter = T[l]
        while  l <= r :
            if T[l] < T[r]:
                r -= 1
                res -= 1
            else:
                highestWinter = max(highestWinter, T[l])
                l += 1
            
        l, r = r + 1, len(T) - 1
        while l <= r:
            if highestWinter > T[l]:
                res += 1
                l += 1
            else:
                r = -1

        return res

# TEST CASE
solution = Solution()

T = [5, -2, 3, 8, 6]
print(solution.findWinter(T))

T = [-5, -5, -5, -42, 6, 12]
print(solution.findWinter(T))

T = [0, 1, 2, 3, 4]
print(solution.findWinter(T))

T = [4, 9, 3, 8, 7, 6, 10]
print(solution.findWinter(T))
