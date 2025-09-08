
valores = []

while True:
    numero = float(input("Digite um número (-1 para encerrar): "))
    if numero == -1:
        break
    valores.append(numero)


quantidade = len(valores)
print(f"\nQuantidade de valores lidos: {quantidade}")


print("Valores na ordem informada:", end=" ")
for v in valores:
    print(v, end=" ")
print()


print("Valores na ordem inversa:", end=" ")
for v in reversed(valores):
    print(v, end=" ")
print()


soma = sum(valores)
print(f"Soma dos valores: {soma}")


if quantidade > 0:
    media = soma / quantidade
else:
    media = 0
print(f"Média dos valores: {media}")


acima_media = sum(1 for v in valores if v > media)
print(f"Quantidade de valores acima da média: {acima_media}")
