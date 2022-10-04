#Coordenadas

x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))

if x > 0:
    if y > 0:
        print("Q1")
    if y < 0:
        print("Q4")
if x < 0:
    if y > 0:
        print("Q2")
    if y < 0:
        print("Q3")