class Solution:
    def numberOfRounds(self, start, end):
        def getMinutes(s):
            return 60 * int(s[:2]) + int(s[3:])

        start = getMinutes(start)
        finish = getMinutes(end)
        if finish < start:
            finish += 60 * 24

        return max(0, finish // 15 - (start + 14) // 15)

# TEST CASE
solution = Solution()

start, end = '12:01', '12:44'
print(solution.numberOfRounds(start, end))

start, end = '20:00', '06:00'
print(solution.numberOfRounds(start, end))

start, end = '00:00', '23:59'
print(solution.numberOfRounds(start, end))

start, end = '12:03', '12:03'
print(solution.numberOfRounds(start, end))

start, end = '12:01', '12:02'
print(solution.numberOfRounds(start, end))
