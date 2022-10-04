#lanchonete
cod_pro = int(input("Codigo do produto comprado [1-8]: "))
q_compr = int(input("Quantidade comprada: "))

if cod_pro == 1:
    valor = q_compr * 5
if cod_pro == 2:
    valor = q_compr * 3.5
if cod_pro == 3:
    valor = q_compr * 4.8
if cod_pro == 4:
    valor = q_compr * 8.9
if cod_pro == 5:
    valor = q_compr * 7.32

print(f"Valor a pagar: R$ {valor:.2f}")