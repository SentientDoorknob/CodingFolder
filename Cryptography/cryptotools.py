ENG_IC = 0.0686
ENG_LETTER_FREQ = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074,]
ALPHABET = [chr(97 + i) for i in range(0,26)]
TRIGRAM_ORDER = ["the", "and", "tha", "ent", "ing", "ion", "tio", "for", "nde", "has", "nce", "edt", "tis", "oft", "sth", "men"]
TRIGRAM_FREQUENCIES = [0.035,0.015,0.011,0.0082,0.0065,0.0059,0.0059,0.00560,0.0055,0.0053,0.005,0.0046,0.0046,0.0043,0.0043,0.0043]

def trigrams(text):
    output = {}
    textLen = len(text)

    for i in range(0, textLen - 2):
        trigram = f"{text[i]}{text[i+1]}{text[i+2]}"
        try:
            output[trigram] += 1
        except:
            output[trigram] = 1

    output = dict(sorted(output.items(), key=lambda item: item[1], reverse=True))
    trigrams = list(output.keys())
    frequencies = list(output.values())

    print(trigrams)
    print(frequencies)

    return trigrams[0:16], frequencies[0:16]

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