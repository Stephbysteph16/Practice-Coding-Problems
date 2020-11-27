from collections import defaultdict

def decreasingSubsequences(array):
    increasing = False
    subsequences = []
    taken = defaultdict()
    
    for i in range(len(array)):
        taken[i] = False
    
    for i in range(len(array)):
        if taken[i]:
            continue
        else:
            taken[i] = True
            possible = []
            last = array[i]
            possible.append(array[i])
            for j in range(i+1, len(array)):
                if array[j] < last and taken[j] == False:
                    possible.append(array[j])
                    last = array[j]
                    taken[j] = True
            
            subsequences.append(possible)
            
    print(subsequences)
    return len(subsequences)

if __name__ == '__main__':
    print(decreasingSubsequences([5, 2, 4, 3, 1, 6]))
    
    print(decreasingSubsequences([2, 9, 12, 13, 4, 7, 6, 5, 10]))
    
    print(decreasingSubsequences([1, 1, 1]))
    
