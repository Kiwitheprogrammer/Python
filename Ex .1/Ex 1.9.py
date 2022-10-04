#medidas
a = float(input("Digite a medida A:"))
b = float(input("Digite a medida B:"))
c = float(input("Digite a medida C:"))


a_qua = a**2

a_tri = b*a/2

a_tra = ((a+b)*c)/2

print(f"AREA DO QUADRADO = {a_qua:.4f}")
print(f"AREA DO TRIANGULO = {a_tri:.4f}")
print(f"AREA DO TRAPEZIO = {a_tra:.4f}")