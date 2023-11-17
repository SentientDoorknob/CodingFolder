from formulaShtuff import *

#text = "abcab a b"

text = """VVQGY TVVVK ALURW FHQAC MMVLE HUCAT WFHHI PLXHV UWSCI GINCM
UHNHQ RMSUI MHWZO DXTNA EKVVQ GYTVV QPHXI NWCAB ASYYM TKSZR
CXWRP RFWYH XYGFI PSBWK QAMZY BXJQQ ABJEM TCHQS NAEKV VQGYT
VVPCA QPBSL URQUC VMVPQ UTMML VHWDH NFIKJ CPXMY EIOCD TXBJW
KQGAN"""

text = text.replace(" ", "")
text = text.replace("\n", "")
text = text.lower()

print(text)
maxKeyLength = 50

differences = []

for i in range(1,maxKeyLength+1):
    print(f"\nKeyLength: {i}")
    cosets = splitCosets(i, text)

    sum = 0
    IC_sum = 0
    for coset in cosets:
        coset_IC = calculateIC(coset)
        sum += abs(ENG_IC - coset_IC)
        IC_sum += coset_IC
        #print(coset_IC)
    sum /= i
    IC_sum /= i
    print(f"Differrence = {sum} \n Average = {IC_sum}")
    differences.append(sum)

print(differences)
print(str(differences.index(min(differences))) + ", " + str(min(differences)))