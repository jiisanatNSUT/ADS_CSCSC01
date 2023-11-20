"""
Least Common Subsequence

* Create a recursive function. Also create a 2D array to store the result of a unique state. 
* During the recursion call, if the same state is called more than once, then we can directly 
return the answer stored for that state instead of calculating again.

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""


def lcs(X, Y, m, n, dp):

	if (m == 0 or n == 0):
		return 0

	if (dp[m][n] != -1):
		return dp[m][n]

	if X[m - 1] == Y[n - 1]:
		dp[m][n] = 1 + lcs(X, Y, m - 1, n - 1, dp)
		return dp[m][n]

	dp[m][n] = max(lcs(X, Y, m, n - 1, dp), lcs(X, Y, m - 1, n, dp))
	return dp[m][n]


X = "AGGTAB"
Y = "GXTXAYB"

m = len(X)
n = len(Y)
dp = [[-1 for i in range(n + 1)]for j in range(m + 1)]

print(f"Length of LCS is {lcs(X, Y, m, n, dp)}")

