"""
179: https://leetcode.com/problems/largest-number/

[3,30,34,5,9]
NUMS str: ['3', '30', '34', '5', '9']
NUMS sorted: ['9', '5', '34', '3', '30']
result: 9534330
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert each number to a string
        nums = list(map(str, nums))
        #print(f"NUMS str: {nums}")
        
        # Define a custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
        
        # Sort the numbers using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        #print(f"NUMS sorted: {nums}")

        # Join the sorted numbers into a single string
        result = ''.join(nums)
        #print(f"result: {result}")        
        
        # Handle the case where the result is '0'
        return '0' if result[0] == '0' else result        
