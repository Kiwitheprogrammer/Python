#Terreno
lar = float(input("Digite a largura do terreno: "))
comp = float(input("Digite o comprimento do terreno: "))
valor_m = float(input("Digite o valor do metro quadrado: R$"))

area = lar*comp
valor_ter = area*valor_m

print(f"Area do Terreno = {area:.2f}")
print(f"Preco do Terreno = {valor_ter:.2f}")