# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeTheFive(self, n):
        # Initializing the last index as zero
        last_index = 0
        isNegative = n < 0
        number = str(n)
        #iterating each number to find the occurences, \
        # and to find if the number is greater than the next element \ 

        for num in range(1, len(number)):
            
            # Handling [case 1] and [case 2]
            if number[num-1] == '5':
                if (int(number[num]) > int(number[num-1])) or (isNegative and int(number[num]) < int(number[num-1])):
                    return number[:num-1] + number[num:]
                else:
                    last_index = num - 1
        
        # If digit is the last number (last occurence) in the string [case 3]
        if number[-1] == '5':
            last_index = len(number) - 1
        
        # print(number[last_index + 1:])

        res = number[:last_index] + number[last_index + 1:]
        return "-" + res if isNegative else res


# TEST CASE
solution = Solution()

print(solution.removeTheFive(15958))
print(solution.removeTheFive(-5859))
print(solution.removeTheFive(-5000))
print(solution.removeTheFive(0))
print(solution.removeTheFive(-1))