
salario_inicial = 1000.0
salario = salario_inicial

percentual = 1.5 / 100  

for ano in range(1996, 2026):  
    salario += salario * percentual  
    percentual *= 2  

print(f"Salário em 2025 (salário inicial R$ 1000.00): R$ {salario:.2f}")


salario_inicial = float(input("\nQual era seu salário inicial? "))
salario = salario_inicial
percentual = 1.5 / 100

for ano in range(1996, 2026):
    salario += salario * percentual
    percentual *= 2

print(f"Salário em 2025 considerando salário inicial de R$ {salario_inicial:.2f}: R$ {salario:.2f}")
