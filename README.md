# Bank Challenge API

## Descrição

A Bank Challenge API é uma API RESTful desenvolvida em Django para gerenciar funcionalidades de pagamentos, contas, usuários e permissões. Projetada para ser escalável, modular e de fácil manutenção, ela é ideal para sistemas financeiros que exigem transações seguras e confiáveis. Esta documentação é destinada a desenvolvedores que desejam configurar, utilizar ou contribuir com o projeto.

### Funcionalidades

-Gestão de contas e transferências.

-Validação de saldo e tipo de conta.

-Autenticações como validação de CPF e campos unicos já existentes no Banco de Dados.

-Autorização externa com simulação de serviço offline.

-Notificações após transações.

-Atomicidade em caso de falha nas transações.

-Contas do tipo empresarial podem apenas receber pagamentos.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```
core/
├── manage.py
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── payments/
│   ├── models.py
│   ├── views.py
│   ├── api.py
│   └── ...
├── users/
│   ├── models.py
│   ├── views.py
│   ├── api.py
│   ├── validators.py
│   └── ...
```

### Principais Módulos

- **core**: Configurações globais do projeto, incluindo URLs, Schemas, Autenticador externo e settings do Django.
- **payments**: Lógica para gerenciamento de transações com autenticador de pagamento externo e atomicidade.
- **users**: Gerenciamento de usuários, autenticação (CPF) e validações (campos unicos: CPF e email).

## Tecnologias Utilizadas

- **Linguagem**: Python 3.11
- **Framework**: Django 5.x com Django Ninja para APIs
- **Banco de Dados**: SQLite (padrão para desenvolvimento; suporta PostgreSQL/MySQL em produção)
- **DevOps**: Postman (teste de requisições da API)
- **CI/CD**: Git e GitHub
- **Outras Dependências**: 
  - Django Ninja: Construção de endpoints RESTful
  - DjangoQ: Gerenciamento de tarefas assíncronas
  - Outras: Consulte o arquivo [requirements.txt](requirements.txt)

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
   A API estará disponível em [http://localhost:8000](http://localhost:8000).

## Endpoints Principais

### Usuários
- **POST /users/**
  Criação de usuários.
  
  **Exemplo de payload:**
  ```bash
  {
      user:{
          "username": "joao",
          "first_name": "João",
          "last_name": "Silveira",
          "email": "joao@email.com",
          "password": "1234", #proteção por hash
          "cpf": "551.963.610-90" #autenticador
          },
      type_user:{
          "type":"user" / "company" 
          }
  }
  ```
  **Resposta Esperada (200 Created)**:
  ```bash
  {
    "user_id": 1
  }
  ```
  **Exceptions:**
  
  (Response 400):
    ```bash
  {
    "errors": {
      "cpf": "CPF Inválido.",
      "email": "Já existe uma conta com esse email cadastrado."
      }
  }
  ```
  (Response 500):
    ```bash
  {
    "errors": "Erro interno do servidor, por favor contate um Administrador"
  }
  ```

### Pagamentos
- **POST /payments/**
  Criação de um pagamento.
  
   **Exemplo de payload:**
  ```bash
    {
     "amount": 10, #Valor
     "payer_id": 6, #Quem enviou
     "payee_id": 8 #Quem recebeu
    }
  ```
  **Resposta Esperada (200 Created)**:
  ```bash
  {
    "transaction_id": 1
  }
  ```
  **Exceptions:**
  
  
  (Response 400):
    ```bash
  {
    "error": "Saldo  Insuficiente."
  }
  ```
  (Response 403):
    ```bash
  {
    "error": "Sem permissão para realizar transferências."
  }
  ```
  (Response 403):
    ```bash
  {
    "error": "O usuário não pode receber transferências."
  }
  ```
    

## Testes

Para rodar os testes, utilize o comando:
```bash
python manage.py test
```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m 'Minha nova feature'
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
