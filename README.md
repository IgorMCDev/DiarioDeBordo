# DiarioDeBordo

[![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Python 3.11](https://img.shields.io/badge/python-311-blue.svg?style=plastic)](https://www.python.org/downloads/release/python-3114/)

Projeto destinado a analisar como os clientes utilizam o transporte de um aplicativo durante um determinado período.

### A análise:

A análise é feita considerando um arquivo '.csv' que possui as informações de transportes para o período. A partir das informações desse arquivo, conseguimos analisar o número de corridas diárias, distâncias percorrida, objetivo da viagem, entre outros.

## Configurações

O projeto foi desenvolvido utilizando-se o python na versão 3.11.4. Verifique e instale caso necessário.

[Download Python](https://www.python.org/downloads/)

### Clonando o projeto:

```bash
# comando para clonar o projeto através do git
git clone https://github.com/IgorMCDev/DiarioDeBordo.git
```

### Instalando as dependências:

O projeto exige, além do python a instalação da lib 'pandas' para sua execução.

```bash
# comando para instalar o pandas
pip install pandas==2.0.3
```

Ou ainda, execute a instalação por meio do arquivo 'requirements.txt'
 
```bash
# comando para instalar o pandas
pip install -r requirements.txt
```

### Inciando o projeto:

Execute o arquivo main.py para iniciar o projeto.

```bash
# comando para executar o programa
python main.py
```

## Funcionamento do programa

O programa é capaz de realizar uma análise sobre as corridas diárias a partir de um arquivo '.csv' que possui as informações de viagens realizadas.

Por padrão o arquivo '.csv' deve apresentar o nome 'info_transportes' e estar na pasta raiz do projeto para a execução do programa. Porém, a fim de auxiliar e facilitar para o usuário, também é possível informar o diretório do arquivo e nome do mesmo, caso o arquivo não esteja na pasta raiz do projeto.

O programa deve gerar como saída um novo arquivo de nome 'info_corridas_do_dia' no mesmo diretório do arquivo de transportes. O arquivo 'info_corridas_do_dia' contém a análise das corridas diárias.

