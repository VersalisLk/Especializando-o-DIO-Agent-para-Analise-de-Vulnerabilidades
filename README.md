# Especializando o DIO Agent para Análise de Vulnerabilidades


---

## 1- Introdução<br><br>

Este projeto tem como objetivo especializar o DIO Agent para atuar como um assistente de análise de vulnerabilidades em segurança da informação,<br>
Através da implementação de uma nova Skill, arquivos de conhecimento e ajustes na persona do agente, buscamos desenvolver um assistente capaz de analisar vulnerabilidades, avaliar riscos, identificar possíveis impactos e orientar medidas de correção.<br>
<br>
Durante o projeto, também serão realizados testes utilizando uma aplicação vulnerável a SQL Injection, permitindo observar como o agente identifica falhas e sugere melhorias no código.

## 2- Ambiente utilizado<br><br>

Sistema operacional: Ubuntu; <br>
Linguagem de programação: Python; <br>
Editor de código: Visual Studio Code; <br>
Agente: DIO Agent; <br>
Harness: Hermes; <br>
Repositório base: digitalinnovationone/dio-agent.<br>

---

## 3- Primeiro cenário - Identificação e correção de SQL Injection<br>

### Objetivo:<br>

Compreender como funciona uma vulnerabilidade de SQL Injection, utilizando uma aplicação desenvolvida em Python para demonstrar como entradas não tratadas podem comprometer consultas ao banco de dados.

### Procedimento:<br>

Foi criada uma aplicação simples em Python contendo um formulário de autenticação que utiliza entradas fornecidas pelo usuário para construir uma consulta SQL.<br>
O DIO Agent foi utilizado para analisar o código, identificar possíveis vulnerabilidades e apresentar recomendações de correção.

### Análise realizada pelo agente:<br>

O Dio agent identificou vulnerabilidades no código de instrução do arquivo para o DB, corrigindo posteriormente de forma automatica, explicando o problema, dando dicas e citando medidas de prevenção.

### Correção:<br>

Foi realizada a alteração da consulta SQL, substituindo a concatenação de strings pela utilização de consultas parametrizadas.

### Resultado obtido:<br>

Após o agente realizar a correção, obtivemos um código mais seguro.

---

## 4- Segundo cenário - Especialização do DIO Agent<br>

### Objetivo:<br>

Adicionar conhecimentos e instruções ao DIO Agent para especializá-lo na análise de vulnerabilidades.

### Criação da Skill:<br>

Foi criada uma nova Skill chamada vulnerability-analysis, responsável por orientar o agente durante o processo de identificação, análise e recomendação de correções de vulnerabilidades.


### Base de conhecimento:<br>

Foi criado o arquivo security-basics.md, contendo conceitos fundamentais de segurança da informação, como:

- Vulnerabilidade;<br>
- Ameaça;<br>
- Risco;<br>
- Confidencialidade;<br>
- Integridade;<br>
- Disponibilidade;<br>
- Boas práticas de segurança.<br><br>

### Personalidade do agente:<br>

Foi realizada uma alteração no arquivo para orientar o comportamento do agente durante análises de segurança.

### Atualização do AGENTS.md:<br>

Foi adicionada uma referência à nova Skill na tabela de habilidades disponíveis, permitindo que o agente identifique quando utilizar a análise de vulnerabilidades.

---

## 5- Terceiro cenário - Testando o agente especializado<br>

### Objetivo:<br>

Verificar se a especialização implementada permite que o agente conduza análises de segurança de maneira mais estruturada.

### Procedimento:<br>

Foi apresentado ao agente um cenário de segurança envolvendo um site online na qual o agente orientou algumas medidas para prevenir possíveis vulnerabilidades.<br>
Durante a interação, foi observado se o agente solicitava informações adicionais antes de recomendar procedimentos e se conseguia avaliar os riscos envolvidos.

### Resultado obtido:<br>

O agente conseguiu percorrer todo o problema e sugerir correções uteis para o problema ficticio.

---

## 6- Conclusão<br>

A realização deste projeto permitiu compreender como agentes de inteligência artificial podem ser especializados através de arquivos de conhecimento, instruções e definição de comportamento.<br><br>
A implementação de uma Skill voltada para análise de vulnerabilidades demonstrou como é possível orientar um agente para identificar problemas de segurança, avaliar riscos e recomendar medidas de correção.<br><br>
Além disso, os testes com SQL Injection contribuíram para reforçar conhecimentos sobre vulnerabilidades em aplicações web e a importância de práticas seguras de desenvolvimento.<br><br>
O projeto também proporcionou um primeiro contato com a utilização de agentes especializados aplicados à segurança da informação.<br><br>

---

AVISO!!!

Todas as análises e testes deste projeto possuem finalidade exclusivamente educacional.<br>
As aplicações utilizadas são próprias e executadas em ambiente controlado. Nenhum teste deve ser realizado contra sistemas sem autorização.
