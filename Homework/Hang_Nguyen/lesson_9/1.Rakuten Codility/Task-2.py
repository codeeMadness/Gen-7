# https://drive.google.com/file/d/1FbGlgYd0cqLzcd-HI0ecKIPceGlULwDb/view?fbclid=IwAR2DUw7unGezSWCW4G8B5MJNWiGvY8j5u_adecnrxr_m0dqp_HexVcxdhi4

class Solution:
    def minimumLengthOfWinter(self, T):
        peakInWinter = T[0]
        highestTemp = T[0]
        res = 0

        for temp in T:
            if temp <= peakInWinter:
                peakInWinter = highestTemp
                res += 1
            elif temp > highestTemp:
                highestTemp = temp
        return res

# TEST CASE
solution = Solution()

T = [5, -2, 3, 8, 6]
print(solution.minimumLengthOfWinter(T))

T = [-5, -5, -5, -42, 6, 12]
print(solution.minimumLengthOfWinter(T))

T = [0, 1, 2, 3, 4]
print(solution.minimumLengthOfWinter(T))