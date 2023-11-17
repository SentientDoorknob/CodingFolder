from formulaShtuff import *

ENG_IC = 0.0686

def getEstimatedKeywordLength(text, maxKeyLength):
    differences = []
    smallestDifference = 1
    index = 0

    for i in range(1,maxKeyLength+1):
        cosets = splitCosets(i, text)

        IC_sum = 0
        for coset in cosets:
            coset_IC = calculateIC(coset)
            IC_sum += coset_IC

        IC_sum /= i
        dif = abs(ENG_IC - IC_sum)
        if dif < smallestDifference : smallestDifference = dif; index = i

        differences.append(dif)

    return index, differences
        