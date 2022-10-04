#pagamento
nome = str(input("Nome: "))
v_h = float(input("Valor por hora: "))
h_t = int(input("Horas de Trabalhos: "))

pg = v_h *h_t

print(f"O Pagamento para {nome} deve ser R${pg:.2f}")