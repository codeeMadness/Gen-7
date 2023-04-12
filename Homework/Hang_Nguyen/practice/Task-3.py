# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeTheFive(self, n):
        n_str = str(n)
        position_5 = []
        for i in range(len(n_str)):
            if n_str[i] == '5':
                position_5.append(i)

        if len(position_5) == 0: return n

        maxNum = -9999999999999
        for position in position_5:
            new_num = int(n_str[:position] + n_str[position+1:]) * 1
            maxNum = max(maxNum, new_num)
        
        return maxNum
        


# TEST CASE
solution = Solution()

print(solution.removeTheFive(15958))
print(solution.removeTheFive(-5859))
print(solution.removeTheFive(-5000))
print(solution.removeTheFive(0))
print(solution.removeTheFive(-1))