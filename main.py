# Criar o projeto no Firebase

# Link documento REST API Firebase
# https://firebase.google.com/docs/reference/rest/database

# Criar o Database (atenção às regras de segurança)
# Estrutura de árvore

# Interação com o Database (REST API)
import requests
import json

link = "https://appvendas-9f4c3-default-rtdb.firebaseio.com/" #---> link do meu banco de dados

# Criar uma venda (POST)

 dados = {'Cliente': 'Alon', 'preco': '150', 'produto': 'fone de ouvido'}
 requisicao = requests.post(f'{link}/Vendas.json', data=json.dumps(dados))
 print(requisicao)
 print(requisicao.text)

# Criar um novo produto (POST)

 dados = {'nome': 'teclado', 'preco': '150', 'quantidade': '250'}
 requisicao = requests.post(f'{link}/produto/.json', data=json.dumps(dados))
 print(requisicao)
 print(requisicao.text)

# Editar a venda (PATCH)

 dados = {'cliente': 'celso'}
 requisicao = requests.patch(f'{link}/Vendas/-OPfsizRDE_jAjJZz367/.json', data=json.dumps(dados))
 print(requisicao)
 print(requisicao.text)

 Pegar uma venda específico ou todas as vendas (GET)
requisicao = requests.get(f'{link}/Vendas/.json')
print(requisicao)
dic_requisicao = requisicao.json()
print(dic_requisicao)
id_alon =None
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['Cliente']
    if cliente == 'Alon':
        print(id_venda)
        id_alon = id_venda
# Deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/produto/-OPfuVCmxAKvcqE6aSzn/.json')
print(requisicao)
print(requisicao.text)

