#baskara
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

delta=b**2-4*a*c

if delta <0:
    print("Esta equação não possui raizes reais")
else:
 x1= (-b+(delta)**0.5)/2*a
 x2= (-b-(delta)**0.5)/2*a
 print(f"X1 = {x1:.4f}")
 print(f"X2 = {x2:.4f}")