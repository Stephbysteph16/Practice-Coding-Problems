def minDaysToBloom(roses, m , k):
    flowers = 0
    days = 0
    bouquets = 0
    running = 0

    if k*m > len(roses):
            return -1

    while bouquets < m:
        bouquets = 0
        running = 0
        days += 1

        for rose in roses:
            if rose <= days:
                running += 1
                # print("rose, running, days:", rose, running, days)
                # print("bouquets:", bouquets)
                if running == k:
                    # print("rose, running, days:", rose, running, days)
                    # print("bouquets:", bouquets)
                    bouquets += 1
                    running = 0
            else:
                running = 0

    return days


if __name__ == '__main__':
    # print(minDaysToBloom([1, 2, 4, 9, 3, 4, 1], 2, 2))
    # print(minDaysToBloom([1, 10, 3, 10, 2], 3, 2))
    print(minDaysToBloom([7,7,7,7,12,7,7], 2 , 3))
    
