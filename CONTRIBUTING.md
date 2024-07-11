# Contribuindo com a API da Comunidade IV

Primeiramente, agradecemos por dedicar seu tempo para contribuir com o projeto! 🎉

A seguir, temos um guia para lhe ajudar a contribuir com a API da Comunidade IV através de _issues_ e _pull requests_. Se você ficar com alguma dúvida sobre o processo, [faça uma pergunta](https://github.com/Comunidade-IV/api-comunidade-iv/issues/new) na parte de issues deste repositório.

**Conteúdo**

- [Reportar privadamente problemas de segurança](#reportar-privadamente-problemas-de-segurança)
- [Participar de debates em issues do repositório](#participar-de-debates-em-issues-do-repositório)
- [Participar de revisões de Pull Requests (PRs)](#participar-de-revisões-de-pull-requests-prs)
- [Desenvolver o código-fonte](#desenvolver-o-código-fonte)
  - [Configurar o ambiente de desenvolvimento](#configurar-o-ambiente-de-desenvolvimento)
  - [Rodar o lint do código](#rodar-o-lint-do-código)
  - [Criar novas Migrations](#criar-novas-migrations)
  - [Commit das alterações](#commit-das-alterações)
  - [Enviar pull requests](#enviar-pull-requests)
  - [Gerenciar o trabalho com quadros de projeto](#gerenciar-o-trabalho-com-quadros-de-projeto)

## Reportar privadamente problemas de segurança

Caso tenha encontrado alguma falha de segurança, pedimos que [reporte de forma privada pelo GitHub](https://github.com/Comunidade-IV/api-comunidade-iv/security/advisories/new). Isso permite discutir detalhes da vulnerabilidade de modo privado com os mantenedores do repositório sem o vazamento da vulnerabilidade ou de informações confidenciais.

Você pode seguir [o tutorial do GitHub](https://docs.github.com/pt/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability#privately-reporting-a-security-vulnerability) sobre como fazer esse tipo de relato.

## Participar de debates em issues do repositório

Sugestões e reportes de bugs são feitos através de issues. Antes de criar um novo, [pesquise se o assunto já está sendo abordado](https://github.com/Comunidade-IV/api-comunidade-iv/issues) e complemente o debate com o seu ponto de vista ou com uma sugestão de implementação, se necessário.

Para abrir um issue, utilize os templates disponíveis clicando em [novo issue](https://github.com/Comunidade-IV/api-comunidade-iv/issues/new/choose).

O título, descrição e comentários devem ser feitos em português.

## Participar de revisões de Pull Requests (PRs)

Mesmo não sendo um mantenedor do repositório, você também pode revisar os pull requests, apontando erros que encontrou enquanto lia o código ou testava a implementação. Isso ajudará quem criou o PR e a pessoa que for avaliar o código antes de realizar o merge, possibilitando um processo de integração mais rápido.

Se você não possui certeza sobre algo, deixe claro no seu comentário para que um mantenedor possa responder suas dúvidas.

## Desenvolver o código-fonte

Se o problema que você quer resolver ainda não estiver documentado em um issue, então [leia o tópico sobre issues](#participar-de-debates-em-issues-do-repositório) e primeiro exponha o problema, depois proponha a solução (no próprio issue e sem preocupação com a implementação). Isso evitará que você invista seu tempo realizando uma modificação no código que não será aceita por não ser algo desejado ou que o comportamento esperado ainda não foi bem definido.

Se você está procurando algo para desenvolver como sendo a sua primeira interação com o código do repositório, você pode procurar por [issues com o label _"good first issue"_](https://github.com/Comunidade-IV/api-comunidade-iv/contribute), que são tarefas que não exigem conhecimento aprofundado sobre o código da API da Comunidade IV, e que são possíveis até para quem nunca fez uma contribuição para um projeto de código aberto.

As alterações no código devem estar em inglês (nomes de funções, variáveis etc.) e seguir o padrão do projeto. Para entender como rodar o projeto e realizar suas alterações, leia as seções relacionadas no [README](/README.md#instalar-e-rodar-o-projeto).

### Configurar o ambiente de desenvolvimento

Para configurar o ambiente de desenvolvimento, siga os passos abaixo:

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

 - caso estes dois passos anteriores tenham deixado você confuso [aqui](https://www.youtube.com/watch?v=3UdHJluar8U) tem um vídeo que pode te ajudar a instalar e em entender todo o ambiente utilizado poara desenvolver a api.

4. Configure o banco de dados:

```bash
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

### Rodar o lint do código

O seu código deve estar de acordo com o padrão do projeto. Para verificar se existe algum erro de lint, você pode usar o comando:

```bash
poetry run flake8
```

Alguns erros podem ser corrigidos automaticamente usando o comando abaixo, mas outros precisarão ser corrigidos de forma manual.

```bash
poetry run black .
```

### Criar novas Migrations

Se você está desenvolvendo algo que envolve uma alteração no banco de dados, você pode utilizar o comando `makemigrations` para criar uma nova migração, por exemplo:

```bash
python manage.py makemigrations
```

Isso irá resultar em um novo arquivo de migração na pasta `migrations`. Para aplicar a migração, utilize o comando:

```bash
python manage.py migrate
```

### Commit das alterações

Após finalizar suas alterações e se certificar que todos os testes estão passando com o comando geral `python manage.py test`, chegou a hora de fazer o commit das suas alterações.

Para ser auxiliado no padrão de commit que utilizamos, utilize o padrão do Conventional Commits. **A mensagem de commit deve estar em inglês.**

### Enviar pull requests

Após realizar as alterações, você pode [criar um novo pull request](https://github.com/Comunidade-IV/api-comunidade-iv/compare). A descrição estará pré-preenchida com comentários, que servem para te guiar a criar a descrição adequada, contendo as modificações realizadas no código e qual o impacto delas. Isso irá facilitar a revisão do PR por colaboradores do repositório. O título e a descrição do PR devem estar em português, e os commits em inglês. Para mais detalhes sobre a criação de um pull request, consulte a [documentação do GitHub](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

Se você percebeu que alguma verificação não está passando no PR, pode corrigir localmente e realizar um novo commit. Caso tudo esteja passando, basta aguardar a revisão do código por outros colaboradores do projeto. Depois de revisado, você pode precisar realizar alguma modificação. Durante o processo de revisão, um mantenedor do repositório poderá liberar a implantação em um ambiente de homologação com o código do seu PR, gerando um link exclusivo para esse ambiente.

Quando as revisões forem feitas e aceitarem seu código, um mantenedor do repositório poderá realizar o merge, e então as suas modificações estarão rodando em produção 🎉.

### Gerenciar o trabalho com quadros de projeto

Para melhor organização e rastreamento do trabalho, utilizamos os quadros de projeto do GitHub. Isso nos permite visualizar as tarefas em andamento, em revisão e concluídas, além de saber quem está responsável por cada atividade. 

Para acessar os quadros de projeto, vá até a aba [Projetos](https://github.com/Comunidade-IV/api-comunidade-iv/projects) no repositório. Lá você encontrará diferentes quadros com as tarefas categorizadas por status. Ao criar ou ser designado para uma tarefa, mova o cartão correspondente para a coluna apropriada para indicar o progresso da atividade.

Os mantenedores do projeto também utilizam esses quadros para revisar o andamento das contribuições, priorizar novas funcionalidades e correções de bugs. Isso garante uma gestão mais eficaz e colaborativa das contribuições, facilitando a integração e lançamento de novas versões da API.

Atribua as issues e pull requests a si mesmo ou a outros colaboradores para que todos saibam quem está trabalhando em cada parte do projeto. Use os comentários nas issues e PRs para discutir detalhes e fornecer feedback, garantindo que todas as mudanças sejam bem comunicadas e alinhadas com os objetivos do projeto.