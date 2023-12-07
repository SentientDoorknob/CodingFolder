import sys
sys.path.append("C:\\Users\\justa\\Documents\\Coding\\Public\\CodingFolder\\Cryptography")

import cryptotools

def getEstimatedKeywordLength(text, maxKeyLength):
    differences = []
    index = 0

    # iterate over possible keyword lengths (assumptions)
    for i in range(1,maxKeyLength+1):
        cosets = cryptotools.splitCosets(i, text) # split into relevant cosets on assumed keyword length

        # take the average of the index of coinceidenceseses of each coset
        IC_sum = 0
        for coset in cosets:
            coset_IC = cryptotools.calculateIC(coset)
            IC_sum += coset_IC
        IC_sum /= i

        # create a list of the differences between IoC of english and that of cosets at assumed keyword length
        # correct keyword length should have a vaule of around 0.001 / 0.002
        # incorrect keyword length should have a value of around 0.01 / 0.02
        dif = abs(cryptotools.ENG_IC - IC_sum)
        differences.append(dif)

    return differences
        