litros = int(input())
tipo_combustivel = input()

if tipo_combustivel == 'A' and litros <=20:
    valor = litros * 1.90
    desconto = valor * 0.03
    valor_pagar = valor - desconto
    print(F'Valor final: {valor_pagar}')
elif tipo_combustivel == 'A' and litros > 20:
    valor = litros * 1.90
    desconto = valor * 0.05
    valor_pagar = valor - desconto
    print(F'Valor final: {valor_pagar}')

elif tipo_combustivel == 'G' and litros <= 20:
    valor = litros * 2.50
    desconto = valor * 0.04
    valor_pagar = valor - desconto
    print(F'Valor final: {valor_pagar}')

elif tipo_combustivel == 'G' and litros > 20:
    valor = litros * 2.50
    desconto = valor * 0.06
    valor_pagar = valor - desconto
    print(F'Valor final: {valor_pagar}')    
    

    
