import sys
sys.path.append("C:\\Users\\justa\\Documents\\Coding\\Public\\CodingFolder\\Cryptography")

import cryptotools as ct

square = ["AFLQV", "BGMRW", "CHNSX", "DIOTY", "EKPUZ"]
ciphertext = "33512 53443 21114 22523 14422 53534 11352 24224 21253 45425 55213 44224 14432 15321 21343 33515 21221 51325 42221 33242 24143 42554 35133 25524 14432 12435 41215 54125 34312 11542 35341 12414 43214 11535 43255 52155 54322 11415 21432 55521 34542 14224 14424 22421 15214 41411 14543 53411 41251 51454 51423 51142 21143 22215 35333 35132 25531 51415 51143 45542 24144 22143 25552 13454 21413 52534 42114 23533 51213 34132 35512 11535 15144 23221 14114 21135 33213 53421 25342 42511 21334 13235 51332 13442 33151 53523 21151 12414 55413 21434 34215 54235 55353 41442 21422 42154 35323 22154 42253 53442 35422 42154 25425 13225 53151 41551 25343 51555 21154 23541 15353 33542 21242 51154 14334 11425 23342 23515 21322 15442 25353 44235 23354 32115 34351 55313 42422 42153 35353 11114 15212 21415 42353 54314 32131 45332 21423 52325 43211 44414 51143 45525 42251 12114 11514 23553 21322 52143 21422 41442 24214 43513 32552 41443 21421 52521 55423 51521 14322 51121 11353 32135 22422 41442 43143 21321 22351 52425 33112 13222 21114 12154 25143 23251 11253 45421 14342 13221 54422 53534 25111 43421 45412 13411 25432 15313 11253 42111 11253 43513 15114 21442 21422 42115 21141 52114 55432 11542 25112 13321 34421 14235 41131 55424 14112 11434 55253 42232 13213 44225 14324 12135 41322 14424 35342 12155 42355 32154 35344 32534 54215 54235 53145 43124 25332 54225 11335 15513 42511 41154 13114 23555 25143 43522 42242 15435 32322 15442 25353 44235 41153 54221 54422 54225 54143 43435 42322 14224 25335 52111 42153 55121 43211 55142 24253 42344 21241 44321 53132 53242 42352 32142 24211 52542 44141 13351 24354 12142 24144 25351 23144 22421 15253 42321 34351 32324 21432 55521 34542 14235 25345 41525 33253 41442 21242 53325 54351 33255 54353 44325 34542 13315 15352 32115 11423 53221 14432 14224 21322 55315 14155 11432 35342 12524 14432 11141 21344 25121 14151 15413 15144 22534 23254 21434 55254 25435 34421 42534 11331 43451 41152 15425 35131 12542 21331 12554 35133 25534 35425 32114 15423 53235 11212 54225 24144 32111 24354 43424 25334 22421 32214 24221 15112 21535 33412 53431 21154 23534 11143 45542 15252 15542 35152 11411 35344 42542 24242 53324 21251 14321 15511 43423 15514 42542 24332 11434 55312 12141 11111 45125 34234 22414 42422 42155 21144 22414 34554 22421 14424 22133 41422 15542 24212 24224 14553 43542 24253 42342 35553 54425 42242 42533 24212 51115 25232 44242 24144 24224 21152 12511 34354 22425 34235 43534 54321 31125 43212 53442 24212 14325 55213 45421 53134 21411 25413 52534 42215 53513 42423 52425 33422 42115 21553 52111 34354 23421 21554 23553 21143 45141 15353 52221 43213 44224 21111 31141 25542 53534 35222 42511 25344 33532 43213 32134 42443 51332 55112 14321 15213 25155 14331 42321 24251 11521 41134 21442 25353 41434 55443 51332 55552 11142 15355 12425 11542 41434 54213 52221 32215 44225 35342 42124 14114 22415 21144 22134 21554 23522 25152 13321 53134 22542 25111 43421 33414 25142 24152 11442 24215 41434 34354 21422 22351 55522 35153 32142 35421 43231 42354 22421 41152 11111 13344 22532 24211 42315 21211 14235 33515 52133 14345 51125 44253 23254 35344 22534 13214 23524 14151 41111 24253 31434 55423 55313 25325 53351 21432 55521 34542 13351 32255 31514 15513 31311 42532 14115 35422 15442 21551 44214 32325 43511 4211"
ciphertext = ciphertext.replace(" ", "").replace("\n", "")

cipherlength = len(ciphertext)
output = ""

print(ciphertext)

def getLetter(numA, numB):
    numA -= 1; numB -= 1
    letter = square[numA][numB]
    return letter

iterate = [i for i in range(cipherlength) if i % 2 == 0]

for i in iterate:
    index1 = int(ciphertext[i])
    index2 = int(ciphertext[i+1])
    letter = getLetter(index1, index2)
    output += letter
    #print(f"{index1}, {index2} : {letter}")


print(output)