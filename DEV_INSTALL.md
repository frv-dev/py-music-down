# DEV INSTALL

## Configuração automática

EM DESENVOLVIMENTO

## Configuração manual

Tenha o Python 3.12.0 ou superior instalado.

Crie um ambiente virtual com o comando:

```sh
python -m venv venv
```

Acesse o seu ambiente virtual:

```sh
# Linux / Mac
source ./venv/bin/activate

# Windows
.\venv\bin\activate
```

Instale as dependências com o comando:

```sh
pip install -r requirements.txt
```

Para sair do ambiente virtual execute o comando:

```sh
deactivate
```

## Adicionando novas dependências

Ao adicionar novas dependências com o `pip` execute o comando:

```sh
pip freeze > requirements.txt
```

Isso atualizará a lista de dependências do projeto.
