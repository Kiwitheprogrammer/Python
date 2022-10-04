#retangulo
b = float(input("Base do retangulo: "))
h = float(input("Altura do retangulo:"))

area = b*h
perimetro = (b+h)*2
diagonal = (b*b+h*h) **0.5

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL =  {diagonal:.4f}")