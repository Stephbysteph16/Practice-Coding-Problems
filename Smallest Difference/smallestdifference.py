import sys


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	arrayOne.sort()
	arrayTwo.sort()
	solve = [int] * 2
	closest = sys.maxsize

	# for num_1 in arrayOne:
	# 	for num_2 in arrayTwo:
	# 		abs_diff = abs(num_1 - num_2)
	# 		if abs_diff < closest:
	# 			closest = abs_diff
	# 			solve[0] = num_1
	# 			solve[1] = num_2

	one_pointer = 0
	two_pointer = 0

	while (one_pointer < len(arrayOne)) and (two_pointer < len(arrayTwo)):
		one = arrayOne[one_pointer]
		two = arrayTwo[two_pointer]

		result = abs(one-two)
		if result == 0:
			solve[0] = one
			solve[1] = two
			break
		if result < closest:
			closest = result
			solve[0] = one
			solve[1] = two

		if one < two:
			one_pointer += 1
		else:
			two_pointer += 1

	return solve
