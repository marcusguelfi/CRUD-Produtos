
# Sistema de Gerenciamento de Produtos com Django


Este é um sistema simples de gerenciamento de produtos desenvolvido com Django. Ele permite que usuários se cadastrem, façam login, e gerenciem produtos com base em suas permissões (Analista ou Supervisor). O sistema também inclui uma API RESTful para consulta de produtos.



## Funcionalidades

1. Autenticação de Usuários:
- Cadastro de usuários.

- Login e logout.

- Controle de permissões via grupos (Analista e Supervisor).

2. Gerenciamento de Produtos:

-   Adicionar, visualizar, editar e excluir produtos.

- Permissões diferenciadas para Analistas e Supervisores.

3. API RESTful:

- Consulta de produtos (somente leitura).

- Acesso restrito a usuários autenticados.

4. Interface Web:

- Páginas para a exibição dos produtos.



## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python (versão 3.8 ou superior).

- Pip (gerenciador de pacotes do Python).

- Git.
## Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto.

1. Clone o Repositório:

    Se você estiver usando Git, clone o repositório:

```bash
  git clone https://github.com/marcusguelfi/CRUD-Produtos.git
```
Se não estiver usando Git, baixe o código-fonte e extraia-o em uma pasta

2. Instale as Dependências

```bash
  pip install -r requirements.txt
```

3. Configure o Banco de Dados


 Execute as migrações para criar as tabelas no banco de dados:

```bash
  python manage.py migrate
```

4. Crie um Superusuário

    
 Crie um superusuário para acessar o Django Admin:

```bash
  python manage.py createsuperuser
```
Siga as instruções para definir um nome de usuário, e-mail e senha.

5. Execute o Servidor de Desenvolvimento

    
 Inicie o servidor de desenvolvimento:

```bash
  python manage.py runserver
```
O projeto estará disponível em:
```bash
  http://127.0.0.1:8000/
```
## Como Usar
1. Acesse o Sistema

Página Inicial: 
```bash
http://127.0.0.1:8000/
```
Cadastro de Usuário:
```bash
http://127.0.0.1:8000/signup/
```

Login: 
```bash
http://127.0.0.1:8000/login/
```


2. Gerenciamento de Produtos


Adicionar Produto: 

```bash
http://127.0.0.1:8000/adicionar/
```

Editar Produto: 
```bash
http://127.0.0.1:8000/editar/<id>/
```


Excluir Produto: 
```bash
http://127.0.0.1:8000/excluir/<id>/
```


3. API RESTful


Listar Produtos:
```bash
http://127.0.0.1:8000/api/produtos/
```
- Acesso restrito a usuários autenticados.

- Retorno em formato JSON.

4. Django Admin


Acesse o Painel de Administração: 
```bash
http://127.0.0.1:8000/admin/
```

Use as credenciais do superusuário criado anteriormente.

No Django Admin, você pode:

 - Gerenciar usuários e grupos.

 - Atribuir permissões a usuários.