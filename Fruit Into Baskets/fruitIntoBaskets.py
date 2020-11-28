def totalFruit(tree):
    # types = set(len(tree))
    # count = dict()
    # for type in types:
    #     count[type] = types.count(type)
    
    # basket[1]
    # tree.sort()
    
    # type1 = -1
    # type2 = -1
    
    # type1_amount = -1
    # type2_amount = -1
    
    # pointer1 = -1
    # pointer2 = -1
    
    # basket1 = 0
    # basket2 = 0
    
    # for i in range(len(tree)):
    #     # print("i:", i)
    #     # print("type1, type2:", type1, type2)
    #     if not (tree[i] == type1 or tree[i] == type2):
    #         # print('i in not:',i)
    #         type_min = min(type1_amount, type2_amount)
    #         if type_min == type1_amount:
    #             type1 = tree[i]
    #             type1_amount = 1
    #             pointer1 = i
    #         else:
    #             type2 = tree[i]
    #             type2_amount = 1
    #             pointer2 = i
        
    #     else:
    #         max_pointer = max(pointer1, pointer2)
    #         if pointer1 == max_pointer:
    #             pointer1 = i
    #         else:
    #             pointer2 = i
    #         if tree[i] == type1:
    #             type1_amount += 1
    #         else:
    #             type2_amount += 1


        
    #     # if type1_amount > basket1:
    #     #     basket1 = type1_amount
    #     # elif type2_amount > basket2:
    #     #     basket2 = type2_amount
        

    # first_pointer = min(pointer1, pointer2)
    # second_pointer = max(pointer1,pointer2)
    
    # return len(tree[first_pointer:second_pointer + 1])
    
    if (tree is None or len(tree)):
        return 0
    
    old_type = -1
    new_type = -1
    old_amount = 0
    new_amount = 0
    max_fruits = 0
    amount_front_of_old = 0
    
    for fruit in tree:
        if not (fruit == old_type or fruit == new_type):
            # Update types
            old_type = new_type
            new_type = fruit
            # Update amounts
            old_amount = amount_front_of_old
            new_amount = 1

            amount_front_of_old = 1
        
        elif fruit == old_type:
            temp = old_type
            old_type = new_type
            new_type = temp
            
            temp = old_amount
            old_amount = new_amount
            new_amount = temp
            
            new_amount += 1
            
            amount_front_of_old = 1
            
        elif fruit == new_type:
            new_amount += 1
            amount_front_of_old += 1
        
        if old_amount + new_amount > max_fruits:
            max_fruits = old_amount + new_amount
    
    return max_fruits    
    
        
        
if __name__ == '__main__':
    print(totalFruit([1,2,1]))
    print(totalFruit([0,1,2,2]))
    print(totalFruit([1, 2, 3, 2, 2]))
    print(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
                    #  [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    
