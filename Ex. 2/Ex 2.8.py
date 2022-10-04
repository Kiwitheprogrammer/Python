#temperatura
from calendar import c


C_F= str(input("Voce vai digitar a temperatura em qual escala (C/F)? "))

if C_F == "C" or C_F == "c":
    temp_c= float(input("Digite a temperatura em Celsius:"))
    temp_f = ((temp_c*9)/5)+35
    print(f"Temperatura equivalente em Fahrenheit: {temp_f:.2f}")

if C_F == "F" or C_F == "f":
    temp_f= float(input("Digite a temperatura em Fahrenheit:"))
    temp_c= (temp_f-32)*5/9
    print(f"Temperatura equivalente em Celsius: {temp_c:.2}")