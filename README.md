# PicPay API

## Descrição

Este projeto é uma API REST desenvolvida em Django para gerenciar funcionalidades relacionadas a pagamentos, usuários e permissões. A API foi projetada para ser escalável, modular e fácil de manter.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```
core/
    manage.py
    core/
        settings.py
        urls.py
        ...

    payments/
        models.py
        views.py
        api.py
        ...

    users/
        models.py
        views.py
        api.py
        validators.py
        ...
```

### Principais Módulos

- **core**: Contém as configurações principais do projeto.
- **payments**: Gerencia funcionalidades relacionadas a pagamentos.
- **users**: Gerencia funcionalidades relacionadas a usuários e validações.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.11
- **Framework**: Django
- **Banco de Dados**: SQLite (padrão, mas pode ser configurado para outros bancos como PostgreSQL ou MySQL)
- **Outras Dependências**: 
  - Django REST Framework
  - Celery (para tarefas assíncronas)

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

## Endpoints Principais

### Usuários
- **POST /users/**: Criação de usuários.
- **GET /users/{id}/**: Detalhes de um usuário.

### Pagamentos
- **POST /payments/**: Criação de um pagamento.
- **GET /payments/{id}/**: Detalhes de um pagamento.

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