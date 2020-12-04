from collections import defaultdict
def minNumberOfChairs(S, E):
    # S and E of same size
    n = len(S)
    if n==0:
        return 0
    times = defaultdict(lambda: 0)
    
    for i in range(len(S)):
        for time in range(S[i], E[i]):
            times[time] += 1
    
    return max(times.values())

if __name__ == '__main__':
    print(minNumberOfChairs(S=[1, 2, 6, 5, 3], E=[5, 5, 7, 6, 8]))
    print(minNumberOfChairs(S=[1, 2, 10, 5, 5], E=[4, 5, 12, 9, 12]))
    
