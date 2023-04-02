# Time Complexity: O(logn) 
# Space Complexity: O(1) 
class Solution(object):
    def searchUnbounded(self, nums, target):
       
        low = 0
        high = 1
        while (nums[low] <= target):
            index = self.binarySearch(nums, low, high, target)
            if (index == -1):
                low = high
                high *= 2
            else:
                return index
        return -1

    def binarySearch(self, arr, l, r, x):

        while (l <= r):  
            mid = l + int((r - l) / 2)

            if (x == arr[mid]):  
                return mid

            elif (x < arr[mid]):
                r = mid - 1

            else:
                l = mid + 1

        return -1