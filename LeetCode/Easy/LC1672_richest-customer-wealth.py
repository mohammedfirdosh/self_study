class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
      # https://leetcode.com/problems/richest-customer-wealth
    	return max(sum(accounts[i]) for i in range(len(accounts)))
