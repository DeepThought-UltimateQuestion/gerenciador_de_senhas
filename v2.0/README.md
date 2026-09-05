# 🔐 Gerenciador de Senhas — v2.0

Um gerenciador de senhas desenvolvido em **Python**, criado para armazenar, consultar e gerenciar credenciais de diferentes contas de forma simples e segura.

A versão **2.0** introduz armazenamento **criptografado**, derivação segura de chave a partir da senha principal e proteção contra tentativas consecutivas de login.

---

## 🚀 Funcionalidades

* 🔐 Criptografia dos dados utilizando **Fernet**
* 🔑 Derivação da chave através de **PBKDF2-HMAC-SHA256**
* 🧂 Utilização de **salt aleatório**
* 💾 Armazenamento criptografado em `contas.enc`
* ⚙️ Configurações e controle de tentativas em `config.json`
* 👤 Sistema de login
* ➕ Adição de novas contas
* 📖 Visualização das contas cadastradas
* 🔎 Consulta de senhas
* ✏️ Alteração de usuários
* 🔑 Alteração de senhas
* 🗑️ Exclusão de contas
* 🎲 Geração de senhas fortes
* ⏱️ Bloqueio temporário após uma tentativa de login incorreta

---

## 🛡️ Segurança

A versão 2.0 não armazena as contas diretamente em texto puro.

As informações são transformadas em JSON e posteriormente criptografadas antes de serem armazenadas em:

```text
contas.enc
```

A chave utilizada pelo Fernet não é armazenada diretamente. Ela é derivada da senha principal através de:

```text
PBKDF2-HMAC-SHA256
```

com **600.000 iterações** e um `salt` aleatório de 16 bytes.

O `salt` é armazenado em:

```text
config.json
```

O `salt` não precisa ser secreto. Sua função é impedir que a mesma senha sempre produza a mesma chave.

### Estrutura dos arquivos

```text
gerenciador_de_senhas/
│
├── contas.py
├── contas.enc
├── config.json
└── README.md
```

### `contas.enc`

Contém as contas do usuário de forma criptografada.

Seu conteúdo não deve ser legível diretamente.

### `config.json`

Armazena informações necessárias para o funcionamento do sistema:

```json
{
    "salt": "...",
    "ultimo erro": 0
}
```

`ultimo erro` é utilizado para controlar o tempo de espera após uma tentativa de login incorreta.

---

## 🔑 Como funciona a criptografia

O processo pode ser resumido assim:

```text
Senha principal
       ↓
     PBKDF2
       ↓
      Salt
       ↓
Chave derivada
       ↓
     Fernet
       ↓
Dados criptografados
       ↓
   contas.enc
```

Para acessar os dados novamente:

```text
Senha fornecida
       ↓
     PBKDF2
       ↓
Mesmo Salt
       ↓
Mesma chave
       ↓
     Fernet
       ↓
Descriptografia
       ↓
Dados originais
```

Se a senha estiver incorreta, a chave gerada será diferente e o Fernet rejeitará a descriptografia.

---

## 🎲 Gerador de senhas

O programa possui uma função capaz de gerar senhas aleatórias:

```python
senha_forte()
```

Ela utiliza:

* Letras maiúsculas
* Letras minúsculas
* Números
* Caracteres especiais

A geração utiliza `secrets.choice()`, que é apropriado para geração de valores aleatórios voltados para segurança.

---

## ⏱️ Proteção contra tentativas de login

Quando uma tentativa de login é incorreta, o programa registra o momento da tentativa em:

```text
config.json
```

Na próxima tentativa, o programa calcula quanto tempo passou.

Atualmente, o período de espera é de:

```text
60 segundos
```

Isso ajuda a dificultar várias tentativas consecutivas de senha.

---

## 📋 Menu

Depois do login, o usuário possui as seguintes opções:

```text
1 - Adicionar login de um novo site
2 - Ler todas as contas
3 - Ler uma senha
4 - Alterar um usuario
5 - Alterar uma senha
6 - Sugerir senha forte
7 - Deletar uma conta
8 - Sair
```

---

## 📦 Requisitos

O projeto utiliza Python 3 e a biblioteca:

```text
cryptography
```

Instalação:

```bash
pip install cryptography
```

---

## ▶️ Executando

Clone ou baixe o projeto e execute:

```bash
python3 contas.py
```

Na primeira execução, o programa solicitará a criação do usuário e da senha principal.

Depois disso, os arquivos necessários serão criados automaticamente.

---

## ⚠️ Importante

Este projeto é principalmente **educacional**.

Apesar de utilizar técnicas reais de criptografia, ele ainda não deve ser considerado um gerenciador de senhas pronto para armazenar credenciais extremamente importantes.

Por exemplo, ainda existem melhorias possíveis relacionadas a:

* Proteção da senha principal
* Organização dos dados
* Controle de acesso
* Segurança da memória
* Backup seguro
* Tratamento de arquivos corrompidos
* Política de senhas
* Autenticação mais robusta

**Nunca coloque senhas reais e importantes neste projeto sem entender completamente os riscos.**

---

## 🧠 O que foi aprendido na v2.0

A versão 2.0 envolve conceitos importantes de Python e segurança:

* Funções
* Dicionários
* JSON
* Manipulação de arquivos
* `Path`
* `match/case`
* Exceções
* `try/except`
* Criptografia simétrica
* Fernet
* Hashing
* PBKDF2
* Salt
* Codificação Base64
* Geração segura de números aleatórios
* Controle de tempo
* Estruturação de um projeto Python

---

## 📈 Evolução

### v1.0

A primeira versão tinha como objetivo criar a estrutura básica do gerenciador:

* Cadastro de contas
* Leitura de contas
* Alteração de credenciais
* Exclusão de contas
* Geração de senhas

Os dados eram armazenados diretamente em JSON.

### v2.0

A segunda versão introduziu uma camada de segurança muito maior:

* 🔐 Criptografia Fernet
* 🧂 Salt aleatório
* 🔑 PBKDF2-HMAC-SHA256
* ⏱️ Proteção contra tentativas consecutivas
* 📁 Separação entre dados criptografados e configuração

---

## 📜 Licença

Projeto desenvolvido para fins educacionais e de aprendizado.

Sinta-se livre para estudar, modificar e evoluir o projeto.
