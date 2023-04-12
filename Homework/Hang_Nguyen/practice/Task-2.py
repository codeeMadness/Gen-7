# https://stackoverflow.com/questions/73981277/how-to-move-left-and-right-through-characters-of-a-string-counting-whenever-a-s

class Solution:
    def numberCameraPass(self, s):
        res = 0
        cameraCnt = 0
        for c in s:
            if c == '.':
                cameraCnt += 1
            elif c == '<':
                res += cameraCnt
        
        cameraCnt = 0
        for c in reversed(s) :
            if c == '.':
                cameraCnt += 1
            elif c == '>':
                res += cameraCnt
        return res

# TEST CASE
solution = Solution()

s = '.>...'
print(solution.numberCameraPass(s))

s = '.>.<.>'
print(solution.numberCameraPass(s))

s = '>>>.<<<'
print(solution.numberCameraPass(s))