def moveElementToEnd(array, toMove):
    # Write your code here.
	n = len(array)
	
	for i in range(n-1):
		if array[i] != toMove:
			continue
		else:
			diffpointer = i+1
			for j in range(n-(i+1)):
				if array[(i+1) + j] != toMove:
					diffpointer = i+1 + j
			# temp = array[diffpointer]
			# array[diffpointer] = toMove
			# array[i] = temp
			array[i], array[diffpointer] = array[diffpointer], array[i]

	return array