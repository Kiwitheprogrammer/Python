#aumento
sal_aut = float(input("Digite o salario da pessoa: R$ "))

if sal_aut <= 1000:
    aum=sal_aut*20/100
    nov_sal = sal_aut+aum
    por = "20%"

if sal_aut > 1000 and sal_aut <= 3000:
    aum=sal_aut*15/100
    nov_sal = sal_aut+aum
    por = "15%"

if sal_aut > 3000 and sal_aut <= 8000:
    aum=sal_aut*10/100
    nov_sal = sal_aut+aum
    por = "10%"

if sal_aut > 8000:
    aum=sal_aut*5/100
    nov_sal = sal_aut+aum
    por = "5%"


print(f"Novo salario: R${nov_sal}")
print(f"Aumento = R${aum}")
print(f"Porcentagem = {por}")