gabarito = ['A', 'C','D','E', 'B','A','E','A','B', 'A']

notas = []

while True:
    qtd_acertos = 0
    for i in range(10):
        resposta = input(f"Resposta da questão {i+1}: ").strip().upper()
        if resposta == gabarito[i]:
            qtd_acertos +=1

    print(f"Você acertou {qtd_acertos} questões.")
    notas.append(qtd_acertos)


    continuar = input("Outro aluno vai fazer a prova? (S/N): ").strip().lower()
    if continuar != "s":
        break


maior = max(notas)
menor = min(notas)
total = len(notas)
media = sum(notas) / total

print("\n--- Resultados finais ---")
print(f"Maior número de acertos: {maior}")
print(f"Menor número de acertos: {menor}")
print(f"Total de alunos: {total}")
print(f"Média da turma: {media:.2f}")
