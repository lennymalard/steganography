from encodage import *
from Stega import *

def connection_encodage(path, message, key):
    main(path, message = message, key = key)

def connection_decodage(path, message, key):
    return main(path,key=key)
