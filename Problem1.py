# Python3 implementation of the approach 
DIGITS = 4; MIN = 1000; MAX = 9999; 

# Function to return the minimum element 
# from the range [prev, MAX] such that 
# it differs in at most 1 digit with cur 
def getBest(prev, cur) : 

	# To start with the value 
	# we have achieved in the last step 
	maximum = max(MIN, prev); 

	for i in range(maximum, MAX + 1) : 
		cnt = 0; 

		# Store the value with which the 
		# current will be compared 
		a = i; 

		# Current value 
		b = cur; 

		# There are at most 4 digits 
		for k in range(DIGITS) : 

			# If the current digit differs 
			# in both the numbers 
			if (a % 10 != b % 10) : 
				cnt += 1; 

			# Eliminate last digits in 
			# both the numbers 
			a //= 10; 
			b //= 10; 

		# If the number of different 
		# digits is at most 1 
		if (cnt <= 1) : 
			return i; 

	# If we can't find any number for which 
	# the number of change is less than or 
	# equal to 1 then return -1 
	return -1; 

# Function to get the non-decreasing list 
def getList(arr, n) : 

	# Creating a vector for the updated list 
	myList = []; 
	
	# Let's assume that it is possible to 
	# make the list non-decreasing 
	possible = True; 

	myList.append(0); 

	for i in range(n) : 

		# Element of the original array 
		cur = arr[i]; 

		myList.append(getBest(myList[-1], cur)); 

		# Can't make the list non-decreasing 
		if (myList[-1] == -1) : 
			possible = False; 
			break; 

	# If possible then print the list 
	if (possible) : 
		for i in range(1, len(myList)) : 
			print(myList[i], end = " "); 
	else : 
		print("-1"); 

# Driver code 
if __name__ == "__main__" : 

	arr = [ 1095, 1094, 1095 ]; 
	n = len(arr); 

	getList(arr, n); 

# This code is contributed by AnkitRai01 
