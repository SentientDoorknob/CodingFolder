ENG_IC = 0.0686

def frequency(text, alphabetLen = 26):
    output = [0 for i in range(0, alphabetLen)]
    for char in text:
        output[ord(char)-97] += 1
    return output

def calculateIC(text, alphabetLen=26):
    textFreq = frequency(text, alphabetLen)
    textLen = len(text)
    
    #print(textFreq, textLen)

    sum = 0 
    for freq in textFreq:
        sum += freq * (freq - 1)

    IC = sum / (textLen * (textLen - 1))
    return IC

def splitCosets(keyLength, text):
    output = [[] for i in range(0,keyLength)]

    pos = 0
    for char in text:
        output[pos % keyLength].append(char)
        pos += 1

    for i in range(0,len(output)):
        output[i] = "".join(output[i])

    return output