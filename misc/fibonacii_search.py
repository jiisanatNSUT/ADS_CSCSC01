"""
Fibonacci search

Algorithm:

Let arr[0..n-1] be the input array and the element to be searched be x.  

1. Find the smallest Fibonacci Number greater than or equal to n. Let this number be 
fibM [m’th Fibonacci Number]. Let the two Fibonacci numbers preceding it be 
fib1 [(m-1)’th Fibonacci Number] and fib2 [(m-2)’th Fibonacci Number].
2. While the array has elements to be inspected: 
    1. Compare x with the last element of the range covered by fib2
    2. If x matches, return index
    3. Else If x is less than the element, move the three Fibonacci variables 
    two Fibonacci down, indicating elimination of approximately rear two-third of the remaining array.
    4. Else x is greater than the element, move the three Fibonacci variables 
    one Fibonacci down. Reset offset to index. Together these indicate the elimination of 
    approximately front one-third of the remaining array.
4. Since there might be a single element remaining for comparison, check if fib1 is 1. 
If Yes, compare x with that remaining element. If match, return index.
"""

# Fibonacci search. 
from bisect import bisect_left 


def fibSearch(arr, x, n): 

	# Initialize fibonacci numbers 
	fib2 = 0 # (m-2)'th Fibonacci No. 
	fib1 = 1 # (m-1)'th Fibonacci No. 
	fibM = fib2 + fib1 # m'th Fibonacci 

	# fibM is going to store the smallest 
	# Fibonacci Number greater than or equal to n 
	while (fibM < n): 
		fib2 = fib1 
		fib1 = fibM 
		fibM = fib2 + fib1 

	# Marks the eliminated range from front 
	offset = -1

	# while there are elements to be inspected. 
	# Note that we compare arr[fib2] with x. 
	# When fibM becomes 1, fib2 becomes 0 
	while (fibM > 1): 

		# Check if fib2 is a valid location 
		i = min(offset+fib2, n-1) 

		# If x is greater than the value at 
		# index fib2, cut the subarray array 
		# from offset to i 
		if (arr[i] < x): 
			fibM = fib1 
			fib1 = fib2 
			fib2 = fibM - fib1 
			offset = i 

		# If x is less than the value at 
		# index fib2, cut the subarray 
		# after i+1 
		elif (arr[i] > x): 
			fibM = fib2 
			fib1 = fib1 - fib2 
			fib2 = fibM - fib1 

		# element found. return index 
		else: 
			return i 

	# comparing the last element with x 
	if(fib1 and arr[n-1] == x): 
		return n-1

	# element not found. return -1 
	return -1


arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100,235] 
n = len(arr) 
x = 235
ind = fibSearch(arr, x, n) 

if ind>=0: 
    print("Found at index:",ind) 
else: 
    print(x,"isn't present in the array"); 

