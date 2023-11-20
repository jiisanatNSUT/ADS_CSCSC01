# A memoisation solution for Rod cutting problem

"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)+O(n)  
"""

def cutRoad(price,index,n,dp):

	# base case
	if(index == 0):
		return n*price[0]
	if(dp[index][n] != -1):
		return dp[index][n]
	
	# At any index we have 2 options either 
	# cut the rod of this length or not cut it
	notCut = cutRoad(price,index-1,n,dp)
	cut = -5
	rod_length = index + 1
	if(rod_length <= n):
		cut = price[index] + cutRoad(price,index,n-rod_length,dp)
	dp[index][n] = max(notCut,cut)
	return dp[index][n]

if __name__ == "__main__":
	arr = [1,5,8,9,10,17,17,20]
	size = len(arr)
	dp = []
	temp = []
	for i in range(0,size+1):
		temp.append(-1)
	for i in range(0,size):
		dp.append(temp)
	# print(dp)
	print("Maximum Obtainable Value is :",end=' ')
	print(cutRoad(arr,size-1,size,dp))
