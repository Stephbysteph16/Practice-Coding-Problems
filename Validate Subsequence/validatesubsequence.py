from collections import defaultdict


def isValidSubsequence(array, sequence):
    # Write your code here.
	# nums = defaultdict(int)
	i = 0
	for num in array:
		if num in sequence[i:]:
			i += 1

	if i == len(sequence):
		return True

	return False
