def isMonotonic(array):
    # Write your code here.
    decreasing = False
    increasing = False
    
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
			increasing = True
			if decreasing:
				return False
        if array[i] > array[i+1]:
			decreasing = True
			if increasing:
				return False
	
	return True
