# Troco
preco_pro = float(input("Preço unitário do produto: "))
quant_pro = int(input("Quantidade comprada: "))
dinh_rec  = float(input("Dinheiro recebido: "))

troco = dinh_rec-(preco_pro*quant_pro)

print(f"TROCO: {troco:.2f}")