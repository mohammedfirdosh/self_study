# 215: https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
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
        data_len = len(nums)

        nums = [-ii for ii in nums]
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)
        """
