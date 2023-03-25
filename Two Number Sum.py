array = [3, 5, -4, 8, 11, 1, -1, 6]
targetsum = 10


def two_nmbr_sum(array, targetsum):
    numbers = {}
    for i in array:
        if targetsum - i in numbers:
            return [targetsum - i, i]
        else:
            numbers[i] = True
    return []


print(two_nmbr_sum(array, targetsum))
