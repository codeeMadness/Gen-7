class Solution:
    def maxDistance(self, arr, l, r):
        stop = 1
        while l > 0 and stop == 1:
            if arr[l] < arr[l-1]:
                l -= 1
            else:
                stop = 0

        stop = 1
        while r < len(arr) - 1 and stop == 1:
            if arr[r] < arr[r+1]:
                r += 1
            else:
                stop = 0
        
        return abs(r-l) + 1


#TEST CASE
solution = Solution()

arr = [2,6,8,5]
l = r = 0
print(solution.maxDistance(arr, l, r))

arr = [2,6,8,5]
l, r = 2, 1
print(solution.maxDistance(arr, l, r))