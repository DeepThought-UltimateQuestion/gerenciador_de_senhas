from secrets import choice
import string
import json
from time import sleep as tempo

contas = None
def ler():
    with open("contas.json", "r") as arquivo:
        contas = arquivo.read()
        if contas.strip() == "":
            return {}
        else:
            return json.loads(contas)


def escrever(x):
    with open("contas.json", "w") as arquivo:
        json.dump(x, arquivo, indent=4)


def senha_forte(tamanho=16):
    carac = string.ascii_letters + string.digits + string.punctuation
    senha = ""
    for _ in range(tamanho):
        senha += choice(carac)
    return senha


liberado = False
print("\n\n", 20 * "=", "GERENCIADOR DE SENHAS", 20 * "=", "\n\n")
tempo(2)

if ler() == {}:
    print("""Bem-vindo ao gerenciador de senhas! 
Como é a sua primeira vez aqui, eu vou te ensinar como funciona:
Aqui você pode salvar os seus nomes de usuário e senhas, e consultá-los depois.
Você també consegue trocar as senhas com o tempo, e ainda criar um exemplo de senha segura.\n""")
    tempo(3)
    print("Mas como eu preciso saber se você é você nos próximos acessos, precisaremos que você crie um usuário e uma senha, que poderao ser acessados e mudados após o login.\n\n")
    usuario = input("Nome de usuário dessa conta: ")
    senha = input("Senha: ")
    contas = {
        "Gerenciador": {
            "usuario": usuario,
            "senha": senha
        }
    }
    dados = ler()
    dados.update(contas)
    escrever(dados)
    liberado = True


else:
    print("Bom dia, querido usuário! Ou será que é intruso? 🤨 \nComo eu não sei, precisarei que você me diga o usuário e a sennha que você coloocou no primeiro uso:")
    tempo(2)
    usuario = input("Qual é o seu nome de usuário? ")
    senha = input("Qual é a sua senha? ")
    dados = ler()
    if usuario == dados["Gerenciador"]["usuario"] and senha == dados["Gerenciador"]["senha"]:
        tempo(2)
        print(f'Você acertou! Então você realmente é você! Bem-vindo, {dados["Gerenciador"]["usuario"]}! Aproveite os nossos serviços em paz!')
        liberado = True
    else:
        tempo(2)
        print("Felizmente, você errou. ENTÃO SAIA, INTRUSO!!! Se você realmente é o usuário e apenas errou a senha, por favor me desculpe e reinicie o código")
        liberado = False

while liberado:
    tempo(1)
    acao = input("""\n\nEntão, o que você deseja fazer hoje?
1 - Adicionar login de um novo site
2 - Ler todas as contas
3 - Ler uma senha
4 - Alterar um usuario
5 - Alterar uma senha
6 - Sugerir senha forte
7 - Deletar uma conta
8 - Sair
                 
Escolha: """)

    match acao:
        case "1":
            nome = input("Qual é o nome desse site? ") 
            usuario = input("Qual é o seu nome de usuário nele? ")
            senha = input("Qual é a sua senha nele? ")
            dados = ler()
            dados[nome] = {
                "usuario": usuario,
                "senha": senha
            }
            print("Adicionado!")
        
        case "2":
            for conta, valor in ler().items():
                print(conta)
                print("   ", "Usuário:", valor['usuario'])
                print("   ", "Senha:", len(valor['senha']) * "*", "\n")
        
        case "3":
            conta = input("Qual é a conta? ")
            dados = ler()
            if conta in dados:
                print(f"Senha: {dados[conta]['senha']}")
            else:
                print("Não consegui achar essa conta")

        case "4":
            dados = ler()
            nome = input("Qual é o nome dessa conta? ")
            if nome in dados:
                usuario = input("Qual é o novo nome de usuário? ")
                dados[nome]["usuario"] = usuario
                print("Alterado!")
            else:
                print("Eu não consegui achar essa conta nos nossos dados. Se precisso, tente novamente.")

        case "5":
            dados = ler()
            nome = input("Qual é o nome dessa conta? ")
            if nome in dados:
                senha = input("Qual é a nova senha? ")
                dados[nome]["senha"] = senha
                print("Alterado!")
            else:
                print("Eu não consegui achar essa conta nos nossos dados. Se precisso, tente novamente.")
        
        case "6":
            print(f"A senha é: {senha_forte()}")

        case "7":
            conta = input("Qual é a conta que você deseja apagar? ")
            dados = ler()
            if conta in dados:
                cert = input("Tem certeza? s/n: ").upper()
                if cert == "S":
                    del dados[conta]
                    print("Feito")
                else:
                    print("Ok")
            else:
                print("Não consegui achar essa conta")

        case "8":
            print("Adeus!")
            break

        case _:
            print("Não consegui entender o comando. Por favor, tente novamente.")
        
    if dados != ler():
        escrever(dados)