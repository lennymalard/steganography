import base64
from hashlib import sha256

def text_to_binary(text): #Convertir texte en binaire
    bits = []
    for lettre in text:
        tmp = bin(ord(lettre))[2:]
        for bit in range(8 - len(tmp)):
            tmp = '0' + tmp
        bits.append([int(bit) for bit in tmp])
    return bits #list [[0, 1...], [1, 0...]

def binary_to_text(binary): #Convertir binaire en texte
    text = ""
    for byte in binary:
        tmp = ""
        for i in range(8):
            tmp += str(byte[i])
        text += chr(int(tmp, 2))
    return text


def XOR(bloc, key):
    #Bloc list [[0, 1...], [1, 0...]], key --> text
    #Le ciphertext ou le cleartext dépend
    #Key toujousr la clé de chiffrement en text
    sha = sha256() #On convertit la clef en SHA256
    sha.update(bytes(key, "ascii"))
    key = base64.b16encode(sha.digest())

    binaryKey, x = [], 0

    for hex in range(0, len(key), 2):#On convertit la clef en binaire
        tmp = text_to_binary(chr(int(key[hex:hex+2], 16)))[0]
        binaryKey.append(tmp)

    for i in range(len(bloc)): #XOR entre la clef et le bloc
        for k in range(8): #8 <=> len(bloc[i])
            bloc[i][k] = binaryKey[x][k] ^ bloc[i][k]
        x += 1

        if x > len(binaryKey) - 1:
            x = 0
    return bloc
"""
block = text_to_binary("Hello World!")

test = XOR(block, "Steganography")

var = XOR(test, "Steganography")

print(binary_to_text(var))
"""
