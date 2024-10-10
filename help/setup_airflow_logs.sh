# Como usar este script
# Primeiro, vá ao terminal e verifique se está no diretório correto.
# Execute no terminal: < chmod +x setup_airflow_logs.sh > para dar permissão ao script
# E depois execute o script no terminal com: < ./setup_airflow_logs.sh >

#!/bin/bash

# Defina o caminho do diretório de logs do Airflow
LOGS_DIR="/opt/airflow/logs/scheduler"

# Crie o diretório de logs, se não existir
if [ ! -d "$LOGS_DIR" ]; then
    echo "Criando diretório de logs: $LOGS_DIR"
    mkdir -p "$LOGS_DIR"
else
    echo "Diretório de logs já existe: $LOGS_DIR"
fi

# Altere as permissões do diretório de logs
echo "Alterando permissões do diretório de logs..."
chmod -R 755 /opt/airflow/logs  # Permissão de leitura e execução para outros usuários, escrita apenas para o proprietário

# Reinicie os containers do Docker
echo "Reiniciando os containers do Docker..."
docker-compose down
docker-compose up -d

echo "Script executado com sucesso!"
