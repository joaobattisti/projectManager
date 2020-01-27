# projectManager
<b>Um simples sistema de gerenciamento de projetos baseados em python 3.6 e Django 3.0 com deploy no Heroku.</b>

<h4><b>Principais características:</b></h4>

Aplicação é dividida em 3 "módulos" para integrar a aplicação: Home, Project e Activities.

Os módulos Project e Activities realizam operações de Criação, Leitura, Update e Delete.

O módulo Home é aplicado basicamente organização do trabalho e inicialização da aplicação.

O framework bootstrap para garantir questões de responsividade e css da aplicação

Quanto a questão de segurança é aplicado um login para acesso as páginas principais, também é utilizado a tag csrf com objetivo de garantir a segurança da aplicação na execução de nas entradas(login e Create).

O sistema de gerenciamento possui um deploy no heroku: https://gerenciamento-projeto.herokuapp.com/ <br>
*para utilização da aplicação é necessário usuário e senha.

A aplicação local utiliza SqLite e PostgreSQL no servidor.

