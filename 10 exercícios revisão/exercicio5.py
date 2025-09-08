total_geral = 0

print("=== Cardápio ===")
print("100 - Cachorro Quente - R$ 1.20")
print("101 - Bauru Simples   - R$ 1.30")
print("102 - Bauru com ovo   - R$ 1.50")
print("103 - Hambúrguer      - R$ 1.20")
print("104 - Cheeseburguer   - R$ 1.30")
print("105 - Refrigerante    - R$ 1.00")

while True:
    codigo = int(input("\nDigite o código do item (0 para encerrar): "))
    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade: "))

    if codigo == 100:
        preco = 1.20
        nome = "Cachorro Quente"
    elif codigo == 101:
        preco = 1.30
        nome = "Bauru Simples"
    elif codigo == 102:
        preco = 1.50
        nome = "Bauru com ovo"
    elif codigo == 103:
        preco = 1.20
        nome = "Hambúrguer"
    elif codigo == 104:
        preco = 1.30
        nome = "Cheeseburguer"
    elif codigo == 105:
        preco = 1.00
        nome = "Refrigerante"
    else:
        print("Código inválido, tente novamente!")
        continue

    subtotal = preco * quantidade
    total_geral += subtotal
    print(f"{nome} - {quantidade} x R$ {preco:.2f} = R$ {subtotal:.2f}")

print("\n=== Total do pedido ===")
print(f"Valor a pagar: R$ {total_geral:.2f}")
