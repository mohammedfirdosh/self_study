# 852 https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        s, e = 1, n - 2
        while s <= e:
            m = s + (e - s) // 2
            if arr[m - 1] < arr[m] > arr[m + 1]:
                return m
            elif arr[m - 1] > arr[m]:
                e = m - 1

            else:
                s = m + 1
        return -1


        """
        low, high = 0, len(arr) - 1

        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low
        """
