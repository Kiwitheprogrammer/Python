#Tempo_de_jogo

h_i = int(input("Hora Inicial: "))
h_f = int(input("Hora Final: "))

if h_i < h_f:
    temp_j = h_f - h_i
else:
    temp_j = (24 - h_i) + h_f

print(f"O Jogo Durou {temp_j} Hora(s)") 