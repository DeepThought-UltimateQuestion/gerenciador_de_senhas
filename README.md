# 🔐 Gerenciador de Senhas

Um gerenciador de senhas desenvolvido em **Python**, criado como um projeto de aprendizado e evolução em programação.

A ideia começou como um programa simples para armazenar credenciais e, versão após versão, foi evoluindo para incluir geração de senhas, persistência de dados, autenticação e criptografia.

> **Projeto em desenvolvimento.**
> O objetivo principal é aprender, experimentar e aplicar conceitos de Python e segurança digital.

---

# 💡 A ideia

A ideia do projeto é criar um programa capaz de centralizar diferentes contas e suas credenciais em um único lugar.

Em vez de precisar lembrar várias senhas, o usuário possui uma **senha principal** para acessar o gerenciador.

O programa permite:

* 👤 Armazenar usuários
* 🔑 Armazenar senhas
* ➕ Adicionar novas contas
* 🔎 Consultar credenciais
* ✏️ Alterar usuários e senhas
* 🗑️ Excluir contas
* 🎲 Gerar senhas fortes
* 🔐 Proteger os dados através de criptografia

O projeto também serve como uma forma prática de estudar programação: cada versão adiciona uma nova dificuldade e introduz novos conceitos.

---

# 🛠️ Tecnologias

O projeto é desenvolvido em:

* 🐍 **Python**
* 📄 JSON
* 🔐 cryptography
* 🔑 Fernet
* 🧂 PBKDF2-HMAC-SHA256
* 🎲 secrets
* 📁 pathlib

---

# 📈 Evolução do projeto

## 🟢 v1.0 — O começo

A primeira versão teve como objetivo criar o funcionamento básico do gerenciador.

Os dados eram armazenados em um arquivo JSON.

### Funcionalidades

* Criação de contas
* Armazenamento de usuário e senha
* Leitura das contas
* Alteração de usuários
* Alteração de senhas
* Exclusão de contas
* Geração de senhas fortes

A estrutura era relativamente simples:


Programa
   ↓
Dicionário Python
   ↓
JSON
   ↓
Arquivo


O foco dessa versão era aprender a trabalhar com:

* Funções
* Dicionários
* JSON
* Arquivos
* Loops
* Condicionais
* match/case

---

# 🟡 v2.0 — Segurança

A segunda versão mudou bastante o projeto.

O principal objetivo passou a ser **proteger os dados armazenados**.

Em vez de guardar diretamente um JSON legível, os dados passaram a ser criptografados antes de serem escritos no disco.

### 🔐 Criptografia

A v2.0 utiliza **Fernet** para criptografar os dados.

A senha principal é utilizada para derivar uma chave através de:


PBKDF2-HMAC-SHA256


com:


600.000 iterações


e um salt aleatório.

O processo funciona aproximadamente assim:


Senha principal
       ↓
     PBKDF2
       ↓
      Salt
       ↓
Chave de criptografia
       ↓
     Fernet
       ↓
Dados
       ↓
  contas.enc


### 📁 Arquivos

A v2.0 passou a utilizar dois arquivos principais:


contas.enc
config.json


contas.enc contém os dados criptografados.

config.json contém informações necessárias para o funcionamento do programa, como o salt e o momento da última tentativa de login incorreta.

---

# ⏱️ Proteção contra tentativas

Também foi implementado um sistema simples contra várias tentativas de login.

Quando o usuário fornece uma senha incorreta, o programa registra o momento da tentativa.

Depois disso, existe um período de espera de:


60 segundos


antes que uma nova tentativa possa ser realizada.

---

# 🎲 Geração de senhas

O projeto também possui um gerador de senhas:


senha_forte()


Ele utiliza secrets.choice() para escolher caracteres aleatoriamente entre:

* Letras maiúsculas
* Letras minúsculas
* Números
* Caracteres especiais

Exemplo:


G7@kP!2x#Lm9$Qw&


O tamanho padrão atualmente é de **16 caracteres**, mas pode ser alterado:


senha_forte(24)


---

# 🧠 O que o projeto ensina

O projeto foi crescendo junto com o aprendizado de Python.

Ao longo das versões, foram trabalhados conceitos como:

### Python

* Variáveis
* Condicionais
* Loops
* Funções
* Parâmetros
* Retorno de funções
* Dicionários
* .items()
* match/case
* Exceções
* try/except

### Arquivos

* Leitura e escrita de arquivos
* JSON
* json.load()
* json.dump()
* Path
* Arquivos binários

### Segurança

* Criptografia simétrica
* Fernet
* Hashing
* PBKDF2
* Salt
* Base64
* Geração segura de aleatoriedade
* Autenticação através da descriptografia

---

# 🔄 Comparação entre versões

| Funcionalidade                    | v1.0 | v2.0 |
| ---------------------------------- | :--: | :--: |
| Armazenamento de contas           |   ✅  |   ✅  |
| Adicionar contas                  |   ✅  |   ✅  |
| Alterar contas                    |   ✅  |   ✅  |
| Excluir contas                    |   ✅  |   ✅  |
| Gerador de senhas                 |   ✅  |   ✅  |
| Login                             |   ✅  |   ✅  |
| JSON legível                      |   ✅  |   ❌  |
| Dados criptografados              |   ❌  |   ✅  |
| Fernet                            |   ❌  |   ✅  |
| PBKDF2                            |   ❌  |   ✅  |
| Salt                              |   ❌  |   ✅  |
| Bloqueio após tentativa incorreta |   ❌  |   ✅  |

---

# ⚠️ Aviso de segurança

Apesar de a v2.0 utilizar técnicas reais de criptografia, **este projeto ainda é experimental e educacional**.

Ele não deve ser utilizado como substituto de um gerenciador de senhas profissional para armazenar credenciais extremamente importantes.

O objetivo principal deste projeto é:

> **Aprender programação construindo algo cada vez mais complexo e seguro.**

---

# 🎯 Objetivo do projeto

O objetivo não é simplesmente criar um gerenciador de senhas.

É acompanhar a evolução de um projeto real:

Ideia
  ↓
Código simples
  ↓
Persistência de dados
  ↓
Organização
  ↓
Autenticação
  ↓
Criptografia
  ↓
Segurança
  ↓
Novas funcionalidades
  ↓
Projeto cada vez mais completo

Cada versão representa uma etapa de aprendizado.

O projeto começou como um simples programa em Python e continua evoluindo conforme novos conceitos são aprendidos e aplicados.

---

# 📜 Versões

### v1.0

> Primeiro protótipo funcional.

Gerenciamento básico de contas e armazenamento em JSON.

### v2.0

> Primeira grande atualização de segurança.

Criptografia, PBKDF2, salt, Fernet e proteção contra tentativas consecutivas de login.

### 🔮 Próximas versões

> Continuar transformando o projeto em um gerenciador cada vez mais completo, organizado e seguro.

---

## 👨‍💻 Status

**Em desenvolvimento 🚧**

Este projeto está sendo desenvolvido continuamente, com novas funcionalidades e melhorias sendo adicionadas conforme o aprendizado avança.
