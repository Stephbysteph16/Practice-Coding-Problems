def threeNumberSum(array, targetSum):
    # Write your code here.

	array.sort()
	nums = {}
	solve = list()

	for i in range(len(array) - 1):
		num = array[i]
		left_pointer = 0
		right_pointer = 0
        new_arr = array[i:]
        
        for number in array[i:]:
			left = new_arr[1 + left_pointer]
			right = new_arr[-(1+ right_pointer)]
			
			if left == right:
				break
		
			potential = left + right + num

			if potential == targetSum:
				solve.append((num,left,right))
				left_pointer += 1
			elif potential > targetSum:
				right_pointer += 1
			else:
				left_pointer += 1
	return solve
				
