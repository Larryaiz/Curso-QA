import requests

squad = {
    "Graziele": "11630350",
    "Fabio": "11631014"
}

for nome, cep in squad.items():
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        cidade = dados.get("localidade", "Cidade não encontrada")
        print(f"{nome} mora na cidade: {cidade}")
    else:
        print(f"Erro ao consultar o CEP {cep} de {nome}. Status: {resposta.status_code}")
