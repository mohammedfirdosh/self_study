class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1500291907/
        # 0ms 100%
        l_ptr, r_ptr = 0, len(numbers) -1
        while l_ptr < r_ptr:
            sum = numbers[l_ptr] + numbers[r_ptr]
            if sum == target:
                return [l_ptr + 1, r_ptr + 1]
            elif sum < target:
                l_ptr += 1
            else:
                r_ptr -= 1
       
