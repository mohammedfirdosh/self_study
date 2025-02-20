# 215: https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick select
        n = len(nums)
        k = n - k

        def quick_select(l, r):
            pivot, p = nums[r], l
            for ii in range(l, r):
                if nums[ii] <= pivot:
                    nums[p], nums[ii] = nums[ii], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quick_select(l, p - 1)
            elif p < k:
                return quick_select(p + 1, r)
            else:
                return nums[p]

        return quick_select(0, n - 1)

        """
        # min heap of size k
        # Time: O(n log k)
        # Space: O(k)

        min_heap = list()
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]
        """

        """
        data_len = len(nums)

        nums = [-ii for ii in nums]
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)
        """
