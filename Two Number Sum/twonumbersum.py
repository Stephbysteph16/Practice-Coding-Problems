from collections import defaultdict


def twoNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
# 	numbers = defaultdict(0)
# 	for number in array:
# 		numbers[array] += 1
	solve = list()
	for i in range(len(array)-1):
		for j in range(i+1, len(array)):
			if array[i] + array[j] > targetSum:
				break
			if array[i] + array[j] == targetSum:
				solve.append(array[i])
				solve.append(array[j])

	return solve
