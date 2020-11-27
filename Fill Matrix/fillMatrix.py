import itertools
def fillMatrix(matrix):
    n = len(matrix)
    magic = n*(n**2 + 1)/2
    
    numbers = list(range(1,n*n))
    
    result = [seq for i in range(len(numbers), 0, -1)
              for seq in itertools.combinations(numbers, i) if sum(seq) == magic]
    print(result)
    
if __name__ == '__main__':
    
    fillMatrix(matrix)
    