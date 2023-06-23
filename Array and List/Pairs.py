'''
Write a function to find all pairs of an integer array
whose sum is equal to a given number. Do not consider commutative pairs.
'''


def pair_sum(myList, sum) -> list:
    pairs = list()
    for i in range(0, len(myList) - 1):
        for j in range(1, len(myList)):
            if myList[i] + myList[j] == sum:
                element = str(myList[i]) + '+' + str(myList[j])
                if element in pairs:
                    continue
                else:
                    pairs.append(element)

    return pairs


print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
