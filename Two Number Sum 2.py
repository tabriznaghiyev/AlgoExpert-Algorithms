array = [3, 5, -4, 8, 11, 1, -1, 6]
targetsum = 10


def trgt_sum(array, targetsum):
    for i in range(len(array) - 1):
        first = array[i]
        for j in range(i + 1, len(array)):
            second = array[j]
            if first + second == targetsum:
                return [first, second]
    return []


print(trgt_sum(array, targetsum))
