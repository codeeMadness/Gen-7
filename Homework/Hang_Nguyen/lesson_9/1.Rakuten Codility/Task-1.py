# https://drive.google.com/file/d/1FbGlgYd0cqLzcd-HI0ecKIPceGlULwDb/view?fbclid=IwAR2DUw7unGezSWCW4G8B5MJNWiGvY8j5u_adecnrxr_m0dqp_HexVcxdhi4

class Solution:
    def minimumCoinsAltered(self, coins):
        count = 0
        i, n = 0, len(coins)
        while i <= n-3:
            left, middle, right = coins[i], coins[i+1], coins[i+2]
            if left == middle and middle == right:
                middle = 1 if left == 0 else 0
                count += 1
            elif left == middle or middle == right:
                left == right
                count += 1
            i += 1
        return count

# TEST CASE
solution = Solution()

A = [1, 0, 1, 0, 1, 1]
print(solution.minimumCoinsAltered(A))

A = [1, 1, 0, 1, 1]
print(solution.minimumCoinsAltered(A))

A = [0, 1, 0]
print(solution.minimumCoinsAltered(A))

A = [0, 1, 1, 0]
print(solution.minimumCoinsAltered(A))

A = []
print(solution.minimumCoinsAltered(A))
