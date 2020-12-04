from collections import defaultdict
def minNumberOfChairs(S, E):
    # S and E of same size
    n = len(S)
    if n==0:
        return 0
    attendees = defaultdict(lambda: 0)
    
    
    