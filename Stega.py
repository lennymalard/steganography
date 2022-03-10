from PIL import Image
from encodage1bit import *


class Encode:
    def __init__(self, path, message):
        self.path = path #Chemin de l'image
        self.message = message #Message en texte (string)

        self.im = Image.open(path) #Ouverture de l'image
        self.pixels = self.im.load()
        self.width, self.height = self.im.size

    def edit_last_bit(self, number, bit): #Remplace le dernier bit de <number> par <bit>
        numberBase2 = number_to_binary(number, 8)
        del numberBase2[7]
        numberBase2.append(bit)
        byte = ""
        for bit in numberBase2:
            byte += str(bit)
        return int(byte, 2)

    def save_image(self): #Enregistre l'image
        self.im.save(self.path)

    def edit_pixels(self, base2List, x = 0, y = 0): #Ecris chaque bit dans <base2List> sur l'image
        tmp = list(self.pixels[x, y])
        for bit in range(len(base2List)):
            tmp[bit % 3] = self.edit_last_bit(tmp[bit % 3], base2List[bit])

            if bit % 3 == 2: #Toutes les 3 itérations, insère le pixel, charge le nouveau
                self.im.putpixel((x, 0), tuple(tmp)) #(n , 0) tuple de coordonnés pour insérer le pixel
                x += 1

                if x > self.width - 1:
                    x, y = 0, y + 1

                tmp = list(self.pixels[x, 0])
        self.im.putpixel((x, 0), tuple(tmp))
    def insert_number_of_caracter(self):  #Pour insérer la longueur du message
        lenTextBase2 = number_to_binary(len(self.message)) #Longueur en bytes du message, convertit en base2
        self.edit_pixels(lenTextBase2, x = 0)


    def insert_text(self): #Pour insérer le texte dans l'image
        message = text_to_binary(self.message)
        self.edit_pixels(message, x = 8)

class Decode:
    def __init__(self, path):
        self.path = path
        self.im = Image.open(path)
        self.pixels = self.im.load()
        self.width, self.height = self.im.size

    def read_last_bit(self, number): #Lire et renvoie le dernier bit de <number>
        return  bin(number)[-1]

    def read_pixels(self, lenText, x = 0, y = 0): #Lis le dernier de chaque pixel où l'ont a écrit dessus
        tmp = list(self.pixels[x, y])
        bits = []
        for bit in range(lenText):
            bits.append(int(self.read_last_bit(tmp[bit % 3])))

            if bit % 3 == 2:
                x += 1

                if x > self.width - 1:
                    x, y = 0, y + 1
                tmp = list(self.pixels[x, 0])
        return bits


    def read_number_of_caracter(self): #Lis le nombre de caractère du message
        """Pour lire la longueur du message"""
        bits = self.read_pixels(24)
        return binary_to_number(bits)

    def read_text(self, longueur): #Lis les caractères du message
        bits = self.read_pixels(longueur * 8, x = 8)
        return bits

def main(path, message = False, key = False):
    if message != False:
        if key != False:
            message = XOR(text_to_binary(message), key)

        encoding = Encode(message = message, path = path)
        encoding.insert_number_of_caracter()
        encoding.insert_text()
        encoding.save_image()

    else:
        decoding = Decode(path = path)
        
        longueur  = decoding.read_number_of_caracter()
        text = decoding.read_text(longueur)
        if key != False:
            text = XOR(text, key)

        else:
            text = binary_to_text(text)
        print(text)


path, message = "/home/noah/Desktop/StegaNSI/chien.png", "Take... Take... Taking that crown from you"

main("/home/noah/Desktop/StegaNSI/chien.png", message = message)
main("/home/noah/Desktop/StegaNSI/chien.png")