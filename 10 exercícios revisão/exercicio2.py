valor_saque = int(input('Valor saque: '))

if 10 <= valor_saque <=600:
    restante = valor_saque
    for n in[100,50,10,5,1]:
        qtd = restante // n
        restante %= n
        if qtd:
            print(f'{qtd} nota(s) de {n}')
else:
    print('valor invalido')
    
