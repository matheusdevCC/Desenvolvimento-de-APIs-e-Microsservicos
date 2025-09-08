import requests

# Solicita ao usuário o nome do país
pais = input("Digite o nome do país: ").strip().lower()

# URL da API
url = f"https://restcountries.com/v3.1/name/{pais}"

try:
    # Faz a requisição GET
    response = requests.get(url)
    response.raise_for_status()  # Levanta erro se o status não for 200
    
    # Converte a resposta JSON em objeto Python
    dados = response.json()[0]  # Pegamos o primeiro resultado
    
    # Nome do país
    nome_pais = dados.get("name", {}).get("common", "Desconhecido")
    
    # Linguagens
    linguagens = ", ".join(dados.get("languages", {}).values())
    
    # Região e sub-região
    regiao = dados.get("region", "Desconhecida")
    subregiao = dados.get("subregion", "Desconhecida")
    
    # Capital
    capital = ", ".join(dados.get("capital", ["Desconhecida"]))
    
    # Moeda
    moedas = dados.get("currencies", {})
    if moedas:
        sigla_moeda = list(moedas.keys())[0]
        nome_moeda = moedas[sigla_moeda].get("name", "Desconhecido")
        simbolo_moeda = moedas[sigla_moeda].get("symbol", "")
    else:
        sigla_moeda = nome_moeda = simbolo_moeda = "Desconhecido"
    
    # Fronteiras
    fronteiras = ", ".join(dados.get("borders", ["Nenhum"]))
    
    # Exibição dos dados
    print("\nInformações sobre o país:")
    print(f"Nome: {nome_pais}")
    print(f"Linguagem(s): {linguagens}")
    print(f"Região: {regiao}")
    print(f"Sub-região: {subregiao}")
    print(f"Capital: {capital}")
    print(f"Moeda: {sigla_moeda} - {nome_moeda} ({simbolo_moeda})")
    print(f"Fronteiras: {fronteiras}")
    
except requests.exceptions.HTTPError:
    print("Erro: país não encontrado ou nome inválido.")
except Exception as e:
    print("Ocorreu um erro:", e)
