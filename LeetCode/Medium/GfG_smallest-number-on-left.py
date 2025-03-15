# https://www.geeksforgeeks.org/problems/smallest-number-on-left3403/0
# User function Template for Python3

class Solution:
    def leftSmaller(self, n, a):
        # code here
        st = []
        result = []
        for idx in range(n):
            if idx == 0:
                result.append(-1)
            else:
                while st and st[-1] >= a[idx]:
                    st.pop()
                if st:
                    result.append(st[-1])
                else:
                    result.append(-1)

            st.append(a[idx])            
        return result 
                

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
        print("~")
# } Driver Code Ends
