salario=float(input("seu salario: "))
if salario > 1250:
    aumento1=salario/100*10
    print(f"salario apos o aumento: {salario+aumento1}")
else:
    aumento2=salario/100*15
    print(f"salario apos o aumento: {salario+aumento2}")