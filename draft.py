array = [3, 5, -4, 8, 11, 1, -1, 6]
targetsum = 10


def fnc(array, targetsum):
    numb = {}
    for i in array:
        if targetsum - i in numb:
            return [targetsum - i, i]
        else:
            numb[i] = True
    return []


print(fnc(array, targetsum))
