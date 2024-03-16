 # Curso Git | GitHub

## Para que serve?

 Git: Software de controle de versão(versionamento)
 GitHub: Plataforma de rede social para programadores

Principais vantagens:

- Controle de histórico
- Trabalho em equipe
- Ramificação do projeto
- Segurança
- Organização

GitHub

- Repositórios ilimitados
- Hospedagem de código-fonte
- Caracteristica de rede social
- GitHub Pages integrado
- Colaboração
- Forks

### O que é uma branch?

Significa "ramificação" ou "galho". 
É uma linha independente de desenvolvimento de um projeto de software que diverge da linha principal de desenvolvimento.
Uma branch é utilizada quando um desenvolvedor precisa criar uma nova funcionalidade
ou fazer uma alteração no código sem afetar a versão principal do projeto
As alterações realizadas em uma branch não afetam o código que está em outras branches.

### O que é um commit?

Operação que registra uma alteração no repositório de código-fonte.
permite que um desenvolvedor salve as alterações feitas em um ou mais arquivos no repositório, 
juntamente com uma mensagem descritiva que explica as alterações realizadas.

### Como clonar um repositório?

- Acesse o repositório no GitHub
- Clique no botão [Code]
- Selecione o protocolo de transferência que você deseja usar para clonar o repositório [HTTPS ou SSH]
- Copie o URL que aparece na caixa
- Abra o terminal no seu computador.
- Navegue até a pasta onde você deseja clonar o repositório usando o comando cd 
- Digite o comando git clone <URL> 
- Pressione Enter 
- Aguarde... Pronto!

Se caso tenha o GitHub desktop é só entrar no repositório, clicar no botão [Code]
e clicar em [Open desktop] e clonar.

### O que é issues?

São erros ou bugs que precisam ser corrigidos no código de um software ou em um projeto de desenvolvimento.

### Código html feito durante a aula

```
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Curso em Vídeo</title>
    <link rel="stylesheet" href="estilos/style.css">
</head>
<body>
    <main>
        <header>
            <h1>Cursos Grátis</h1>
        </header>
        <article>
            <h2>Cursos de HTML5</h2>
            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. In veniam at quam accusamus, ex culpa quia harum velit facere earum magnam ipsum suscipit vitae possimus aperiam vel distinctio, optio minima.</p>
        </article>
        <article>
            <h2>Curso de JavaScript</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos suscipit delectus architecto, fuga quaerat incidunt possimus tempora numquam. Cupiditate ipsa labore placeat velit facere ex? Cumque itaque consequuntur fuga modi?</p>
            teste
        </article>
    </main>
    
</body>
</html>
```

### Comandos em caso de usar o GIT BASH

git init → Inicializa um repositório

git add nome_do_arquivo → Adiciona um arquivo p/ ser direcionado

git add -all ou $git add . → Ele adiciona todos os arquivos que estiver naquele commit aguardando para dar push.

git status → Aparece o status de arquivos a serem usado pelo commit.

git commit -m "texto desejado"  → Adiciona um comentário

git branch -M "main"  → Master p/ Main

git remote add nome_projeto <link> → Diz o local para onde o diretório do seu arquivo.

git push -u nome_projeto main → Ele joga o commit para o repositório do GitHub.

git checkout -b "nome-da-branch" → Cria mais uma branch.

git checkout nome-da-branch → Volta para a branch desejada.

git merge nome-da-branch → juntar branch com a principal

git clone <link> → ele cópia um repositório existente.

git pull → Pega a atualização do git clone. (Antes entrar com $cd).

