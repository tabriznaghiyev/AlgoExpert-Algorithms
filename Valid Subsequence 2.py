
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def checker(array,sequence):
    arIDX=0
    seqIDX=0
    while arIDX < len(array) and seqIDX < len(sequence):
        if array[arIDX] == sequence[seqIDX]:
            seqIDX+=1
        arIDX+=1
    return seqIDX==len(sequence)

print(checker(array,sequence))