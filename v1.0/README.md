# GERENCIADOR DE SENHAS
## Esse é um programa que armazena, recupera, lembra e sugere usuário e senhas de aplicativos.

Funcionalidades:
    * Cria um login principal para acessar o gerenciador
    * Permite:
        * Adicionar logins
        * Consultar logins
        * Alterar eles
        * Excluir um site
        * Sugerir uma senha segura

Tecnologias e módulos usados:
    * Python 3.10+
    * Módulos:
        * json: lê e escreve no .json
        * secret: permite escolher um caractere aleatório, o que ajuda na senha segura
        * string: dá toda a lista de caracteres, o que ajuda na senha segura
        * time: permite dar uma pausa, o que torna o sistema mais fluido

Instalação:
    * É necesssário ter um Python 3.10+
    * Baixar/clonar o projeto
    * Entrar no diretório
    * Executar o arquivo contas.py

Primeiro uso:
    * O sistema detecta que é o primeiro uso com base no vazio no .json
    * Pede para você criar um usuário e senha
    * Depois, só te deixa entrar depois que fizer o login

Como usar:
    * Opções e suas respectivas ações:
        * 1 - O sistema pede o nome, o usuário e a senha de um aplicativo e armazena como uma nova conta no .json
        * 2 - Organiza as informações do .json e mostra de uma forma mais fácil de entender. Não mostra as senhas, para dar um pouco mais de segurança
        * 3 - Lê a senha de uma conta específica
        * 4 - Altera o usuário de uma conta
        * 5 - Altera a senha de uma conta
        * 6 - Sugere uma senha forte usando um loop for com as bibliotecas string e secret
        * 7 - Deleta uma conta, para caso você pare de usar um aplicativo
        * 8 - Interrompe o loop while, encerrando o programa

Armazenamento:
    * Os dados são armazenados num arquivo chamado contas.json por meio da biblioteca JSON
    * Os dados atualmente são armazenados em texto puro, sem nenhuma espécie de criptografia para proteção

Aviso:
    * Esse projeto é educacional e apenas armazena senhas, sem criptografá-las para proteção

Melhorias futuras:
    * Criptografia
    * Interface gráfica
    * Limite de tentativas de login por tempo