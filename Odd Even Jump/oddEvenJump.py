def oddEvenJumps(A):
        if (A == None or len(A) == 0):
            return 0
        if (len(A) == 1):
            return 1

        result = 0
        array = A
        # Sort array to avoid sorting it each time

        for i in range(len(array)):
            invalid = False
            new_index = i
            jump = 0
            number = array[i]
            while not invalid:
                jump += 1
                if (jump % 2) == 0:
                    invalid, new_index = evenJump(
                        number, array, array[new_index:], new_index)
                else:
                    invalid, new_index = oddJump(
                        number, array, array[new_index:], new_index)
                
                # print('n_i, num', new_index, number)
            if new_index == len(array) - 1:
                result += 1

        return result

def oddJump(number, array, array_to_sort, prev_index):
    sorted_array = sorted(array_to_sort)
    invalid = False
    # Binary search to get the number index on sorted
    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        index = low + (high - low) // 2

        if sorted_array[index] == number:
             break
        elif sorted_array[index] < number:
            low = index + 1
        else:
            high = index - 1

    # Now that we have the number index, we will search for the smallest element
    # that is larger than the number by increasing the index until the number
    # is different
    replace = number

    while replace == number:
        if (index>=len(sorted_array)):
            return (True, prev_index)
        try:
            replace = sorted_array[index+1]
            index += 1
        except:
            invalid = True
            break

    try:
        new_index = array.index(replace)
    except:
        new_index = prev_index

    return (invalid, new_index)


def evenJump(number, array, array_to_sort, prev_index):
    sorted_array = sorted(array_to_sort)
    invalid = False
    # Binary search to get the number index on sorted
    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        index = low + (high - low) // 2
        if sorted_array[index] == number:
             break
        elif sorted_array[index] < number:
            low = index + 1
        else:
            high = index - 1

    # Now that we have the number index, we will search for the largest element
    # that is smaller than the number by decreasing the index until the number
    # is different
    replace = number
    while replace == number:
        if(index <= 0):
            return (True, prev_index)
        try:
            replace = sorted_array[index-1]
            index -= 1
        except:
            invalid = True
            break


    if(not invalid):
        new_index = array.index(replace)
        # print(new_index)
    else:
        new_index = prev_index

    return (invalid, new_index)


if __name__ == '__main__':
    print(oddEvenJumps([10, 13, 12, 14, 15]))
    print(oddEvenJumps([2, 3, 1, 1, 4]))
    print(oddEvenJumps([5, 1, 3, 4, 2]))
