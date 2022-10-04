#troco_verificado
pre_uni = float(input("Preço unitário do produto: "))
q_compr = int(input("Quantidade comprada: "))
din_rec = float(input("Dinheiro recebido:"))

a_pag = pre_uni*q_compr
troco = din_rec-a_pag
insuficiente = troco *(-1)
if din_rec >= a_pag:
    print(f"TROCO = {troco}")
else:
    print(f"DINHEIRO INSUFICIENTE. FALTAM {insuficiente} REAIS")