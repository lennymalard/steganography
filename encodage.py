import base64
from hashlib import sha256

def text_to_binary(text): #Convertir texte en binaire
    bits = ""
    for lettre in text:
        tmp = str(bin(ord(lettre))[2:])
        for bit in range(8 - len(tmp)):
            tmp = '0' + tmp
        bits += tmp
    return bits

def binary_to_text(binary): #Convertir binaire en texte
    text, tmp = "", ""
    for bit in range(len(binary)):
        tmp += str(binary[bit])
        if bit % 8 == 7:
            text += chr(int(tmp, 2))
            tmp = ""
    return text

def number_to_binary(number, bits = 24): #Par défault la longueur max du texte est donc de 2^24 caractères
    numberBinary = str(bin(number)[2:])
    for i in range(bits - len(numberBinary)):
        numberBinary = '0' + numberBinary
    return numberBinary

def binary_to_number(binary):
    return int(binary, 2)


def XOR(bloc, key):
    #bloc: [0, 1, 0, ...], peut etre ciphertext ou plaintext en binaire
    #key: str normal text

    sha = sha256() #On convertit la clef en SHA256
    sha.update(bytes(key, "ascii"))
    key = base64.b16encode(sha.digest())

    binaryKey, cipher, x = [], "", 0

    for hex in range(0, len(key), 2):#On convertit la clef en binaire
        tmp = text_to_binary(chr(int(key[hex:hex+2], 16)))[0]
        binaryKey.append(tmp)

    for i in range(len(bloc)): #XOR entre la clef et le bloc
        cipher += str(int(binaryKey[x]) ^ int(bloc[i]))
        x += 1
        if x > len(binaryKey) - 1:
            x = 0

    return binary_to_text(cipher)
