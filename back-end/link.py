from encodage import*
from Stega import *

def encoding_link(path, message, key):
    main(path, message = message, key = key)

def decoding_link(path, message, key):
    return main(path,key=key)