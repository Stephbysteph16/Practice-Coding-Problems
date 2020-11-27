def minDaysToBloom(roses, m , k):
    flowers = 0
    days = 0
    bouquets = 0
    running = 0

    if k*m > len(roses):
        return -1
    
    # # Too slow
    # while bouquets < m:
    #     bouquets = 0
    #     running = 0
    #     days += 1

    #     for rose in roses:
    #         if rose <= days:
    #             running += 1
    #             if running == k:
    #                 bouquets += 1
    #                 running = 0
    #         else:
    #             running = 0

    # Implementing binary search
    
    left = min(roses)
    right = max(roses)
    optimal = max(roses)
    
    while left <= right:
        days = int((left+right)/2)
        bouquets = 0
        running = 0
        
        for rose in roses:
            if rose <= days:
                running += 1
                if running == k:
                    bouquets += 1
                    running = 0
            else:
                running = 0
        if bouquets == m:
            if days < optimal:
                optimal = days
        if bouquets < m:
            left = days + 1
        else:
            right = days - 1
    
    return optimal


if __name__ == '__main__':
    print(minDaysToBloom([1, 2, 4, 9, 3, 4, 1], 2, 2))
    print(minDaysToBloom([1, 10, 3, 10, 2], 3, 2))
    print(minDaysToBloom([7,7,7,7,12,7,7], 2 , 3))
    
