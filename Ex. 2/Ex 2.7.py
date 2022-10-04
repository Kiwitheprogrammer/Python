#dardo
print("Digite as tres distancias:")
d1 = int(input(""))
d2 = int(input(""))
d3 = int(input(""))

maior = d1
if d2 > maior:
    maior = d2
if d3 > maior:
    maior = d3
print(f"MAIOR DISTANCIA = {maior}")