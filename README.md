# 🚀 Projeto de Processamento de Dados com Meltano e Airflow

## 📝 Descrição
Este projeto tem como objetivo automatizar a criação de ambientes e a execução de pipelines de dados usando Meltano e Airflow. Ele inclui a configuração de um banco de dados PostgreSQL e a inicialização do Airflow para gerenciar as DAGs que orquestram o fluxo de dados entre fontes de dados como CSV e PostgreSQL.

### Desafio de Código da Indicium Tech
Este desafio foi desenvolvido para candidatos a Engenharia de Dados.

## Contexto
Na Indicium, desenvolvemos pipelines de dados completos para nossos clientes, extraindo dados de diversas fontes e carregando-os em destinos variados, como data warehouses ou APIs para integração com sistemas de terceiros. Como desenvolvedor de software focado em projetos de dados, sua missão é planejar, desenvolver, implantar e manter uma pipeline de dados.

## O Desafio
Você receberá duas fontes de dados: um banco de dados PostgreSQL e um arquivo CSV. O arquivo CSV representa detalhes de pedidos de um sistema de e-commerce, e o banco de dados é uma versão modificada do Northwind, onde a tabela `order_details` não está presente, sendo substituída pelo arquivo CSV.

Seu objetivo é construir uma pipeline que extraia dados diariamente de ambas as fontes, salvando-os primeiro em disco local e, em seguida, carregando-os em um banco de dados PostgreSQL.

## Requisitos Principais
- A pipeline deve ser executada diariamente e ter uma estrutura de arquivos separada por fonte, tabela e data.
- As etapas de escrita (para o disco local e para o PostgreSQL) devem ser isoladas e idempotentes.
- A solução deve permitir reprocessar dados de dias anteriores.
- Ferramentas obrigatórias: Airflow, Meltano ou Embulk, e PostgreSQL.

## Critérios de Avaliação
- Código limpo e organizado.
- Decisões bem fundamentadas sobre a arquitetura e formatos utilizados.
- Capacidade de buscar informações e resolver problemas com ferramentas desconhecidas.

## ✅ Pré-requisitos
- 🐍 Python 3.6 ou superior
- 🐳 Docker e Docker Compose
- 🌐 Git

## ⚙️ Instalação

1. *Criação do Ambiente Virtual Python*
Para criar um ambiente virtual, execute:

```bash
python -m venv .venv
```
*Para Linux/Mac:*

```bash
source .venv/bin/activate 
``` 
*ou para Windows:*

```bash
.\venv\Scripts\activate
``` 
2. *Instalação do Meltano*

Execute os comandos abaixo no terminal para instalar o Meltano e configurar o projeto:

```bash
pip install --upgrade pip && pip install meltano
meltano --version  # Verifique a versão instalada
meltano init etl_meltano  # Inicie um novo projeto
cd etl_meltano
meltano add extractor tap-csv  # Adicione o extrator CSV
meltano add loader target-csv  # Adicione o carregador CSV
meltano add extractor tap-postgres  # Adicione o extrator PostgreSQL
meltano add loader target-postgres  # Adicione o carregador PostgreSQL
```

💡 Dica para usuários Windows: Execute os comandos individualmente para evitar erros.
🖥️ Usuários Linux: Podem usar o script disponível na pasta help:

```bash
sh help/setup_meltano.sh 
```

3. *Inicie o Docker*
Para subir o banco de dados PostgreSQL e iniciar o Airflow, execute:

```bash*
docker-compose up -d
```

Nota: O usuário e a senha padrão do Airflow são ambos admin.

⚠️ Erros Conhecidos
Atualmente, as DAGs do Airflow podem apresentar o erro de "arquivo/diretório não encontrado" ao tentar referenciar o Meltano.
Sugestões e contribuições para resolver esse problema são bem-vindas! 💡

🤝 Contribuição
Contribuições são sempre bem-vindas!
Abra uma issue para relatar problemas, envie um pull request para propor melhorias ou correções.

###📞 Contato
Fique à vontade para entrar em contato comigo para mais informações ou suporte:
📧 Email: *alexkrypt.ti@gmail.com*

