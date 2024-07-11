
# API da Comunidade IV

Bem-vindo à API da Comunidade IV! Este é um projeto de backend desenvolvido com Django e Django REST Framework (DRF), que visa integrar os serviços de fórum e blog da Comunidade IV. Este projeto é totalmente open-source e aberto para contribuições de qualquer pessoa que tenha conhecimento básico de desenvolvimento em Python.

## Índice

- [Visão Geral](#visão-geral)
- [Recursos](#recursos)
- [Como Começar](#como-começar)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
  - [Rodando o Projeto](#rodando-o-projeto)
- [Como Contribuir](#como-contribuir)
  - [Reportar Problemas](#reportar-problemas)
  - [Participar de Debates](#participar-de-debates)
  - [Revisar Pull Requests](#revisar-pull-requests)
  - [Desenvolver o Código](#desenvolver-o-código)
- [Licença](#licença)

## Visão Geral

A API da Comunidade IV foi criada para fornecer uma plataforma robusta e escalável para integrar funcionalidades de fórum e blog. Utilizando Django e DRF, oferecemos uma API RESTful que pode ser facilmente consumida por aplicações frontend e mobile, proporcionando uma experiência de usuário rica e interativa.

## Recursos

- **Autenticação de Usuários:** Gerenciamento seguro de usuários com registro, login e perfis.
- **Gestão de Conteúdo:** Criação, edição e exclusão de postagens de blog e tópicos de fórum.
- **Comentários:** Sistema de comentários para postagens de blog e tópicos de fórum.
- **Administração:** Painel de administração completo para gerenciar usuários e conteúdo.
- **API RESTful:** Endpoints bem documentados e prontos para serem consumidos.

## Como Começar

### Pré-requisitos

- Python 3.8 ou superior
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/Comunidade-IV/api-comunidade-iv.git
    cd api-comunidade-iv
    ```

2. Instale as dependências usando Poetry:

    ```bash
    poetry install
    ```

3. Ative o ambiente virtual do Poetry:

    ```bash
    poetry shell
    ```

4. Configure o banco de dados:

    ```bash
    python manage.py migrate
    ```

### Rodando o Projeto

1. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

2. Acesse `http://localhost:8000` no seu navegador para ver a API em execução.

## Como Contribuir

Contribuir para a API da Comunidade IV é simples e incentivamos todos a participar. Veja como você pode ajudar:

### Reportar Problemas

Caso encontre algum problema, por favor, [reporte uma issue](https://github.com/Comunidade-IV/api-comunidade-iv/issues/new). Descreva o problema de forma detalhada e forneça informações sobre como reproduzi-lo.

### Participar de Debates

Sugestões e discussões sobre melhorias são bem-vindas. Participe dos debates em [issues](https://github.com/Comunidade-IV/api-comunidade-iv/issues) existentes ou abra uma nova issue para iniciar uma discussão.

### Revisar Pull Requests

Mesmo que você não seja um mantenedor, pode revisar pull requests. Isso ajuda a garantir que o código seja de alta qualidade e facilita o processo de integração.

### Desenvolver o Código

Se deseja contribuir com código, siga estes passos:

1. Fork este repositório e clone o seu fork.
2. Crie uma nova branch para a sua funcionalidade ou correção de bug:

    ```bash
    git checkout -b minha-feature
    ```

3. Faça as alterações necessárias.
4. Adicione e commit as suas mudanças:

    ```bash
    git add .
    git commit -m "Minha nova feature"
    ```

5. Envie as mudanças para o seu repositório fork:

    ```bash
    git push origin minha-feature
    ```

6. Abra um pull request no repositório original.

Para mais detalhes sobre como contribuir, leia nosso [guia de contribuição](CONTRIBUTING.md).

## Licença

Este projeto está licenciado sob a licença MIT. Para mais detalhes, leia o arquivo [LICENSE](LICENSE).


## Contribuidores

<a href="https://github.com/Comunidade-IV/api-comunidade-iv/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Comunidade-IV/api-comunidade-iv&max=500" alt="Lista de contribuidores" width="50%"/>
</a>