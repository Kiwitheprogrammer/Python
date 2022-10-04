#menor_de_tres

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segunda valor: "))
n3 = int(input("Terceira valor: "))

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f"MENOR = {menor}")