#operadora

q_m = int(input("Digite a quantidade de minutos:"))

if q_m <= 100:
    vp = 50
else:
    m_e = q_m - 100 
    vp  = 50 + m_e*2

print(f"Valor a pagar: R$ {vp:.2f}")