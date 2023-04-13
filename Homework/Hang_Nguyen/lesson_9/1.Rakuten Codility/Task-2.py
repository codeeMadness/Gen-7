# https://drive.google.com/file/d/1FbGlgYd0cqLzcd-HI0ecKIPceGlULwDb/view?fbclid=IwAR2DUw7unGezSWCW4G8B5MJNWiGvY8j5u_adecnrxr_m0dqp_HexVcxdhi4

class Solution:
    def minimumLengthOfWinter(self, T):
        l, r = 0, len(T) - 1
        peakInWinter = -999999

        while l <= r:
            if T[l] < T[r]:
                length = r
                r -= 1
            else:
                peakInWinter = max(peakInWinter, T[l])
                l += 1

        return length

# TEST CASE
solution = Solution()

T = [5, -2, 3, 8, 6]
print(solution.minimumLengthOfWinter(T))

T = [-5, -5, -5, -42, 6, 12]
print(solution.minimumLengthOfWinter(T))

T = [0, 1, 2, 3, 4]
print(solution.minimumLengthOfWinter(T))

T = [3, 9, 0, 4, 8, 10]
print(solution.minimumLengthOfWinter(T))
