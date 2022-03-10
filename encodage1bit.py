import base64
from hashlib import sha256

def text_to_binary(text): #Convertir texte en binaire
    bits = []
    for lettre in text:
        tmp = bin(ord(lettre))[2:]
        for bit in range(8 - len(tmp)):
            tmp = '0' + tmp
        for bit in tmp:
            bits.append(int(bit))
    return bits #List [0, 1, 1, ...]

def binary_to_text(binary): #Convertir binaire en texte
    text, tmp = "", ""
    for bit in range(len(binary)):
        tmp += str(binary[bit])
        if bit % 8 == 7:
            text += chr(int(tmp, 2))
            tmp = ""
    return text

def number_to_binary(number, bits = 24): #Par défault la longueur max du texte est donc de 2^24 caractères
    numberBinary = [int(i) for i in bin(number)[2:]]
    for i in range(bits - len(numberBinary)):
        numberBinary.insert(0, 0)
    return numberBinary

def binary_to_number(binary):
    strBase2 = ""
    for bit in binary:
        strBase2 += str(bit)

    return int(strBase2, 2)


def XOR(bloc, key):
    #bloc: [0, 1, 0, ...], peut etre ciphertext ou plaintext en binaire
    #key: str normal text

    sha = sha256() #On convertit la clef en SHA256
    sha.update(bytes(key, "ascii"))
    key = base64.b16encode(sha.digest())

    binaryKey, x = [], 0

    for hex in range(0, len(key), 2):#On convertit la clef en binaire
        tmp = text_to_binary(chr(int(key[hex:hex+2], 16)))[0]
        binaryKey.append(tmp)

    for i in range(len(bloc)): #XOR entre la clef et le bloc
        bloc[i] = binaryKey[x] ^ bloc[i]
        x += 1

        if x > len(binaryKey) - 1:
            x = 0

    return binary_to_text(bloc)

"""
block = text_to_binary("Hello World!")

test = XOR(block, "Steganography")

var = XOR(test, "Steganography")

print(binary_to_text(var))
"""