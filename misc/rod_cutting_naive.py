# A recursive solution for Rod cutting problem

"""
Time Complexity: O(2^n)
Space Complexity: O(n)
"""

def cutRod(price, index, n):
	
	# base case
	if index == 0:
		return n*price[0]
	
	# At any index we have 2 options either
	# cut the rod of this length or not cut 
	# it
	notCut = cutRod(price,index - 1,n)
	cut = float("-inf")
	rod_length = index + 1

	if (rod_length <= n):
		
		cut = price[index]+cutRod(price,index,n - rod_length)

	return max(notCut, cut)

arr = [ 1, 5, 8, 9, 10, 17, 17, 20 ]
size = len(arr)
print("Maximum Obtainable Value is ",cutRod(arr, size - 1, size))
