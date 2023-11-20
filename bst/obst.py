# Optimal Binary Search Tree with recursion and memoization

def optCost_memoized(freq, i, j):
	# Reuse cost already calculated for the subproblems. 
	# Since we initialize cost matrix with 0 and fredquency for a tree of one node,
	# it can be used as a stop condition
	if cost[i][j]:
		return cost[i][j]

	# Get sum of freq[i], freq[i+1], ... freq[j]
	fsum = Sum(freq, i, j)

	# Initialize minimum value
	Min = 999999999999

	# One by one consider all elements as
	# root and recursively find cost of
	# the BST, compare the cost with min
	# and update min if needed
	for r in range(i, j + 1):
		c = (optCost_memoized(freq, i, r - 1) + optCost_memoized(freq, r + 1, j))
		c += fsum
		if c < Min:
			Min = c
			# replace cost with new optimal calc
			cost[i][j] = c

	# Return minimum value
	return cost[i][j]


# The main function that calculates minimum
# cost of a Binary Search Tree. It mainly
# uses optCost() to find the optimal cost.
def optimalSearchTree(keys, freq, n):
	# Here array keys[] is assumed to be
	# sorted in increasing order. If keys[]
	# is not sorted, then add code to sort 
	# keys, and rearrange freq[] accordingly.
	return optCost_memoized(freq, 0, n - 1)


# A utility function to get sum of
# array elements freq[i] to freq[j]
def Sum(freq, i, j):
	s = 0
	for k in range(i, j + 1):
		s += freq[k]
	return s


if __name__ == '__main__':
	keys = [10, 12, 20]
	freq = [34, 8, 50]
	n = len(keys)
	
	# cost[i][j] = Optimal cost of binary search
	# tree that can be formed from keys[i] to keys[j].
	# cost[0][n-1] will store the resultant cost
	cost = [[0 for x in range(n+1)] for y in range(n+1)]

	# For a single key, cost is equal to
	# frequency of the key
	for i in range(n):
		cost[i][i] = freq[i]

	print("Cost of Optimal BST is", optimalSearchTree(keys, freq, n))
