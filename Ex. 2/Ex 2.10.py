#multiplos

print("Digite dois numeros inteiros:")

n1 = int(input(""))
n2 = int(input(""))

if n1<n2:
    menor= n1
else:
    menor= n2
if n1>n2:
    maior= n1
else:
    maior= n2


if maior%menor==0:
    print("Sao multiplos")
else:
    print("Não são multiplos")