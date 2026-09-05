from cryptography.fernet import Fernet as fernet, InvalidToken
from secrets import choice, token_bytes
from time import sleep as tempo, time
from pathlib import Path
import hashlib
import base64
import string
import json

ARQUIVO_CONTAS = Path(__file__).parent / "contas.enc"
ARQUIVO_CONFIG = Path(__file__).parent / "config.json"
contas = None

def pegar_config():
    with open(ARQUIVO_CONFIG, "r") as arquivo:
        return json.load(arquivo)


def gerar_chave(senha, salt):
    chave = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode(),
        salt,
        600_000
    )

    return base64.urlsafe_b64encode(chave)


def ler(senha):
    config = pegar_config()
    salt = base64.b64decode(config["salt"])
    chave = gerar_chave(senha, salt)
    f = fernet(chave)
    with open(ARQUIVO_CONTAS, "rb")as arquivo:
        criptografado = arquivo.read()
    texto = f.decrypt(criptografado)
    return json.loads(texto.decode())


def criar_config():
    salt = token_bytes(16)
    config = {
        "salt": base64.b64encode(salt).decode(),
        "ultimo erro": 0
    }
    with open(ARQUIVO_CONFIG, "w") as arquivo:
        json.dump(config, arquivo, indent=4)


def salvar_tempo():
    dados = pegar_config()
    dados["ultimo erro"] = time()
    with open(ARQUIVO_CONFIG, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


def lembrar_tempo():
    dados = pegar_config()
    return time() - dados["ultimo erro"]


def escrever(dados, senha):
    config = pegar_config()
    salt = base64.b64decode(config["salt"])
    chave = gerar_chave(senha, salt)
    f = fernet(chave)
    texto = json.dumps(dados).encode()
    criptografado = f.encrypt(texto)
    with open(ARQUIVO_CONTAS, "wb") as arquivo:
        arquivo.write(criptografado)


def senha_forte(tamanho=16):
    carac = string.ascii_letters + string.digits + string.punctuation
    senha = ""
    for _ in range(tamanho):
        senha += choice(carac)
    return senha

liberado = False
print("\n\n", 20 * "=", "GERENCIADOR DE SENHAS", 20 * "=", "\n\n")
tempo(2)

if not ARQUIVO_CONTAS.exists() or ARQUIVO_CONTAS.stat().st_size == 0:
    print("""Bem-vindo ao gerenciador de senhas! 
Como é a sua primeira vez aqui, eu vou te ensinar como funciona:
Aqui você pode salvar os seus nomes de usuário e senhas, e consultá-los depois.
Você també consegue trocar as senhas com o tempo, e ainda criar um exemplo de senha segura.\n""")
    tempo(3)
    print("Mas como eu preciso saber se você é você nos próximos acessos, precisaremos que você crie um usuário e uma senha, que poderao ser acessados e mudados após o login.\n\n")
    usuario = input("Nome de usuário dessa conta: ")
    senha_conta = input("Senha: ")
    contas = {
        "Gerenciador": {
            "usuario": usuario,
            "senha": senha_conta
        }
    }
    criar_config()
    escrever(contas, senha_conta)
    liberado = True


else:
    if lembrar_tempo() > 60:
        print("Bom dia, querido usuário! Ou será que é intruso? 🤨 \nComo eu não sei, precisarei que você me diga o usuário e a sennha que você coloocou no primeiro uso:")
        tempo(2)
        usuario = input("Qual é o seu nome de usuário? ")
        senha = input("Qual é a sua senha? ")
        try:
            dados = ler(senha)
            if usuario == dados["Gerenciador"]["usuario"]:
                tempo(2)
                print(f'Você acertou! Então você realmente é você! Bem-vindo, {dados["Gerenciador"]["usuario"]}! Aproveite os nossos serviços em paz!')
                liberado = True
                senha_conta = senha
            else:
                tempo(2)
                print("Felizmente, você errou. ENTÃO SAIA, INTRUSO!!! Se você realmente é o usuário e apenas errou a senha, por favor me desculpe e reinicie o código")
                liberado = False
                salvar_tempo()
        except InvalidToken:
            tempo(2)
            print("Felizmente, você errou. ENTÃO SAIA, INTRUSO!!! Se você realmente é o usuário e apenas errou a senha, por favor me desculpe e reinicie o código")
            liberado = False
            salvar_tempo()
        
    else:
        print(f"Como você tentou entrar e errou a {lembrar_tempo():.0f} segundos, espere {60 - lembrar_tempo():.0f} segundos para tentar de novo.")
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

    dados = ler(senha_conta)
    match acao:
        case "1":
            nome = input("Qual é o nome desse site? ") 
            usuario = input("Qual é o seu nome de usuário nele? ")
            senha = input("Qual é a sua senha nele? ")
            dados[nome] = {
                "usuario": usuario,
                "senha": senha
            }
            print("Adicionado!")
        
        case "2":
            for conta, valor in dados.items():
                print(conta)
                print("   ", "Usuário:", valor['usuario'])
                print("   ", "Senha:", len(valor['senha']) * "*", "\n")
        
        case "3":
            conta = input("Qual é a conta? ")
            if conta in dados:
                print(f"Senha: {dados[conta]['senha']}")
            else:
                print("Não consegui achar essa conta")

        case "4":
            nome = input("Qual é o nome dessa conta? ")
            if nome in dados:
                usuario = input("Qual é o novo nome de usuário? ")
                dados[nome]["usuario"] = usuario
                print("Alterado!")
            else:
                print("Eu não consegui achar essa conta nos nossos dados. Se precisso, tente novamente.")

        case "5":
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
        
    if dados != ler(senha_conta):
        escrever(dados, senha_conta)