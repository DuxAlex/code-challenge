#!/bin/bash

# Set environment variables for the database
export DATABASE_URL="postgresql://northwind_user:thewindisblowing@localhost:5432/northwind"
export CSV_FILE_PATH="/workspaces/code-challenge/airflow/data/order_details.csv"  # Replace with the actual path
export OUTPUT_DIR="/data"

# Define the docker-compose.yml file path
DOCKER_COMPOSE_FILE="docker-compose.yaml"

# Start the docker-compose stack
docker-compose -f "$DOCKER_COMPOSE_FILE" up 

# Output success message
echo "Docker-compose stack started successfully with Airflow running and sample DAGs removed."
echo "Access Airflow UI at http://localhost:8080"