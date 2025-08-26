# SaldoPy
>Um programa python com intuito de controle de despesas

### O programa SaldoPy foi criado, como forma de estudo, para contrele de despesas. Consiste no usuário selecionar a ação que deseja fazer, usando uma sequência de números de 1-8, sendo elas ver, adicionar, editar e apagar despesas/receitas. E também mostra se o usuário está em saldo positivo ou negativo considerando todas despesas e todas receitas.

## Configurações e Requisitos
> [!IMPORTANT]
>  - Para rodar este programa é necessário ter o python instalado (**Python 3.10+**), ou usá-lo em algum editor on-line da sua preferência.<br>
>  - As configurações necessárias são apenas relacionadas ao banco de dados, criação e conexão.
### Criação
Para a criação do banco de dados basta usar o arquivo na raiz do projeto nomeado como "dataBase.sql", nele já está incluso a criação do banco de dados, bem como as tabelas de despesas(expenses) e receitas(profits).
### Conexão
A conexão com o banco de dados é feito nas seguintes linhas (Linha 4 à linha 9):
``` python
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='crud_python',
)
```
#### Após estas configurações, já é possível usar este programa, sendo necessário apenas executar ele via terminal, ou algum editor de código. Para fazer isso pelo terminal, acesse a pasta pelo terminal e digite o seguinte comando:
``` bash
py main.py
```

## Tecnologias usadas
- Python <img height=20 width=20 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
- Mysql <img height=20 width=20 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg" />
