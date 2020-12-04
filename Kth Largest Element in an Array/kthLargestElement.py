import heapq

def kthLargestElement(array, k):
    # # trivial
    # array.sort()
    # return array[len(array) - k]
    
    # Solution with PQ
    heapq.heapify(array)
    klargests = heapq.nlargest(k, array)
    
    return klargests[k-1]


if __name__ == '__main__':
    print(kthLargestElement([3, 2, 1, 5, 6, 4], k = 2))
    print(kthLargestElement([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
