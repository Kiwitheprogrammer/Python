#duraçao

segundos = int(input("Digite a duracao em segundos:"))

horas = segundos/3600
resto = segundos%3600

minutos = resto/60
resto = resto%60


print(f"{horas:.0f}:{minutos:.0f}:{resto:.0f}")
