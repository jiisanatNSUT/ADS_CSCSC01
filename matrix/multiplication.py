"""
Matrix chain multiplication

steps to solve the problem:

- Build a matrix dp[][] of size N*N for memoization purposes.
- Use the same recursive call as done in the above approach:
    -  When we find a range (i, j) for which the value is already calculated, return the minimum value for that range (i.e., dp[i][j]).
    - Otherwise, perform the recursive calls as mentioned earlier.
- The value stored at dp[0][N-1] is the required answer.

Time Complexity: O(N3)
Space: O(N2) 
"""


import sys
dp = [[-1 for i in range(100)] for j in range(100)]

def matrixChainMemoised(p, i, j):
	if(i == j):
		return 0
	
	if(dp[i][j] != -1):
		return dp[i][j]
	
	dp[i][j] = sys.maxsize
	
	for k in range(i,j):
		dp[i][j] = min(dp[i][j], matrixChainMemoised(p, i, k) + matrixChainMemoised(p, k + 1, j)+ p[i - 1] * p[k] * p[j])
	
	return dp[i][j]

def MatrixChainOrder(p,n):
	i = 1
	j = n - 1
	return matrixChainMemoised(p, i, j)

if __name__ == '__main__': 
    arr = [1, 2, 3, 4]
    n = len(arr)
    print("Minimum number of multiplications is",MatrixChainOrder(arr, n))
