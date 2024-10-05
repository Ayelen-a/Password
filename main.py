

import random

cs = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

p1 = int(input("¿De que longitud quiere su contraseña?"))

contrasena = ""

for i in range(p1):
    contrasena += random.choice(cs)                    

print (contrasena)    
