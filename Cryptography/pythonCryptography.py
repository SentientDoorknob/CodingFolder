inputs = [13,68,79,141,33,27,111,127,25,54,0,124,110,209,269,41,19,135,57,46,1,40,40,0,129,3]
output = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
orderedalphabet = ["E","T","A","O","N","R","I","S","H","D","L","F","C","M","U","G","Y","P","W","B","V","K","J","X","Z","Q"]

totalOutput = {}

length = 1991

output = [(round(i/1991, 3) * 100) for i in inputs]

alphabet = [x for _, x in sorted(zip(output, alphabet))]
output.sort()

output.reverse()
alphabet.reverse()

orderedalphabet = [x for _, x in sorted(zip(alphabet, orderedalphabet))]

print(orderedalphabet)
print(alphabet)

key = "".join(orderedalphabet)
print(key)

