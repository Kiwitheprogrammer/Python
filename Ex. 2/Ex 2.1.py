#notas
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

n_f = n1+n2/2

if n_f >= 60:
    print(f"Nota Final = {n_f:.1f}")
else:
    print(f"Nota Final = {n_f:.1f}")
    print("Reprovado")