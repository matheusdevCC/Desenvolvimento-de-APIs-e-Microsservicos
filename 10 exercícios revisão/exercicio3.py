nota_1 = float(input('digite sua primeira nota: '))
nota_2 = float(input('digite sua segunda nota: '))

nota_parcial = (nota_1 + nota_2) / 2

if nota_parcial >= 9.0:
      conceito = 'A'
elif 7.5 <= nota_parcial < 9.0:
      conceito = 'B'  
elif 6.0 <= nota_parcial <= 7.5:
      conceito = 'C'   
elif 4.0 <= nota_parcial <= 6.0:
      conceito = 'D'  
else:
      conceito = 'E'
 
status = "APROVADO" if conceito in "ABC" else "REPROVADO"
print(F'Notas {nota_1:.1f} e {nota_2:.1f}')
print(f'Média: {nota_parcial:.1f}')
print(f'Conceito: {conceito}')
