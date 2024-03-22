import requests

def teste_palindromo_api(texto):
    url = 'https://teia-e11b9df945e5.herokuapp.com/palindrome'
    headers = {'Content-Type': 'application/json'}
    data = {'texto': texto}
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        print(f"Response: {response.json()}")
    else:
        print(f"Error: {response.status_code}")


palavras = [
    "casa", "gato", "cachorro", "árvore", "carro", "flor", "livro", "cadeira", "mesa", "telefone",
    "janela", "porta", "teto", "chão", "parede", "computador", "teclado", "mouse", "tela", "sol",
    "chuva", "nuvem", "céu", "estrela", "lua", "arara", "ala", "ama", "mar", "rio", "lago", "montanha", "vale",
    "cidade", "vila", "campo", "floresta", "praia", "areia", "pedra", "rocha", "terra",
    "água", "fogo", "ar", "vento", "calor", "frio", "quente", "gelado", "molhado", "seco"
]

for palavra in palavras:
    teste_palindromo_api(palavra)

# Testar com uma palavra palíndroma
teste_palindromo_api('radar')

# Testar com uma palavra não palíndroma
teste_palindromo_api('hello')
