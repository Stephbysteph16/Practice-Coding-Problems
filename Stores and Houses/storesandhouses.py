import sys

# O(n^2)
def storeshouses(houses, stores):
    result = [0] * len(houses)
    i=0
    for house in houses:
        min_store = -1
        for store in stores:
            if min_store == -1:
                min_store = abs(store - house)
                result[i] = store
            elif (abs(store - house) == min_store):
                result [i] = min(result[i], store)
            elif (abs(store - house) < min_store):
                min_store = abs(store - house)
                result[i] = store
        i = i + 1
    return result

if __name__ == '__main__':
    houses = [5, 10, 17]
    stores = [1, 5, 20, 11, 16]
    print(storeshouses(houses,stores))
