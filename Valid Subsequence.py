array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


def checker(array, sequence):
    seqID = 0
    for i in array:
        if seqID == len(sequence):
            break
        if sequence[seqID] == i:
            seqID += 1
    return seqID==len(sequence)

print(checker(array,sequence))
