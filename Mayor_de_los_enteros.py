"""Programa para calcular cual de los tres numeros enteros es mayor"""


print("-----------------------------------------------------")
print("----Programa para calcular cual # entero es mayor----")
print("-----------------------------------------------------")

# input
X=int(input("introdusca un valor para X:"))
Y=int(input("introdusca un valor para Y:"))
Z=int(input("introdusca un valor para Z:"))
# prossesing
if X > Y :
    if X > Z:
        msj = X
    else:
        msj = Z     
if Y > X :
    if Y > Z:
        msj = Y
    
    else: 
        msj = Z
if X == Y == Z:
    msj = "Los numeros son iguales"     

# output 
print("El numero mayor es " + str(msj))