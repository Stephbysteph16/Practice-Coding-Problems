def spiralTraverse(array):
    # Write your code here.
	result = []
	n = len(array)
	m = len(array[0])

	start_row = 0
	start_col = 0
	end_row = n - 1
	end_col = m - 1

	while start_row <= end_row and start_col <= end_col:
		# Append the first row
		for col in range(start_col, end_col + 1):
			result.append(array[start_row][col])
		# Append the end col
		for row in range(start_row + 1, end_row + 1):
			result.append(array[row][end_col])
		# Append the bottom row
		for col in reversed(range(start_col, end_col)):
            # Special case to not have repeated values
			if start_row == end_row:
				break
			result.append(array[end_row][col])
		# Append start row
		for row in reversed(range(start_row + 1, end_row)):
            # Special Case to not have repeated values
			if start_col == end_col:
				break
			result.append(array[row][start_col])

		start_row += 1
		start_col += 1
		end_row -= 1
		end_col -= 1

	if start_row == end_row and start_col == end_col:
		result.append(array[start_row][end_col])
	return result


# def spiralRecursive(array, solving):
# 	# print(array)
# 	print(solving)
# 	# try:
# 	# 	n = len(array)
# 	# except:
# 	# 	print("a")
# 	# 	result = solving
# 	# 	return result
# 	# try:
# 	# 	m = len(array[0])
# 	# except:
# 	# 	print("b")
# 	# 	print(solving)
# 	# 	result = solving
# 	# 	return result

# 	if len(array) == 0 or len(array[0]) ==0:
# 		return solving
# 	if len(array) == 1 and len(array[0]) == 1:
# 		solution = [int]*1
# 		solution[0] = array[0][0]
# 		return solution

# 	n = len(array)
# 	m = len(array[0])

# 	solve = [int] * (n*2 + (m-2)*2)

# 	for i in range(n + n - 2):
# 		if i==0:
# 			for j in range(m):
# 				solve[j] = array[0][j]
# 		elif i < n-1:
# 			solve[m+i-1] = array[i][-1]
# 		elif i == (n-1):
# 			for j in range(m):
# 				solve[(n-2)+(m) + j] = array[-1][-(1+j)]
# 		elif i > n-1:
# 			index = 2*m + n - 2 + i - (n)
# 			solve[index] = array[-(i-(n-2))][0]

# 	new_spiral = [[0 for x in range(n-2)] for y in range(m-2)]

# 	for i in range (1,n-1):
# 		for j in range(1, n-1):
# 			new_spiral[i-1][j-1] = array[i][j]

# 	solving = solving + solve
# 	spiralRecursive(new_spiral, solving)
