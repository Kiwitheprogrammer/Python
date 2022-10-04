#glicose

medi_gli = float(input("Digite a medida da glicose: "))

if medi_gli <= 100:
    print("Classificacao: normal")
if medi_gli > 100 and medi_gli < 140:
    print("Classificacao: elevado")
else:
    print("Classificacao: diabetes")
