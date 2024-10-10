#!/bin/bash

# Atualizar o pip
echo "Atualizando o pip..."
pip install --upgrade pip

# Instalar o Meltano
echo "Instalando o Meltano..."
pip install meltano

# Verificar a versão do Meltano
echo "Versão do Meltano:"
meltano --version

# Inicializar o projeto Meltano
echo "Inicializando o projeto Meltano..."
meltano init etl_meltano

# Entrar no diretório do projeto
cd etl_meltano

# Instalar extratores e carregadores

# Adicionar extrator CSV
echo "Adicionando extrator CSV..."
meltano add extractor tap-csv

# Adicionar carregador CSV
echo "Adicionando carregador CSV..."
meltano add loader target-csv

# Adicionar extrator PostgreSQL
echo "Adicionando extrator PostgreSQL..."
meltano add extractor tap-postgres

# Adicionar carregador PostgreSQL
echo "Adicionando carregador PostgreSQL..."
meltano add loader target-postgres

echo "Configuração do Meltano concluída com sucesso!"
