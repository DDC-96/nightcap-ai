#!/usr/bin/env bash 

################################################################################
# Nightcap Docker Runner Script v2.0.0
#
# This script automates the local deployment of the Nightcap app using Docker.
#
# It performs the following:
# 1. Removes any existing containers named `nightcap-backend` and `nightcap-frontend` in case some were left behind during local testing.
# 2. Pulls the latest images for the backend and frontend from Docker Hub that was pushed by the CICD workflow.
# 3. Dynamically creates a new Docker network with an incremented version number 
#    (e.g. nightcap-net-v1, nightcap-net-v2, etc.) so it stays static for now.
# 4. Starts the backend container using an `.env` file for environment variables
# 5. Starts the frontend container
# 
# 
#  
################################################################################

# VARS
DOCKER_USER="dcruzdevops"
BACKEND_IMAGE="$DOCKER_USER/nightcap-backend:latest"
FRONTEND_IMAGE="$DOCKER_USER/nightcap-frontend:latest"
ENV_FILE="./backend/.env"
ENV_FRONTEND="./frontend/nightcap-ui/.env.production"
# BASE_NET_NAME="nightcap-net"
# LAST_VERSION=$(docker network ls --format '{{.Name}}' | grep "$BASE_NET_NAME-v" | sed -E "s/.*-v([0-9]+)/\1/" | sort -n | tail -n 1)
# NEXT_VERSION=$((LAST_VERSION + 1))
# NETWORK_NAME="${BASE_NET_NAME}-v${NEXT_VERSION}"

# echo "Cleaning up existing containers if they exist..."
# sleep 2

# # REMOVE EXISITING CONTAINERS 
# if docker ps -a --format '{{.Names}}' | grep -Eq "^nightcap-backend$"; then
#   docker rm -f nightcap-backend && echo "Removed existing nightcap-backend container"
# else
#   echo "No existing nightcap-backend container"
# fi

# if docker ps -a --format '{{.Names}}' | grep -Eq "^nightcap-frontend$"; then
#   docker rm -f nightcap-frontend && echo "Removed existing nightcap-frontend container"
# else
#   echo "No existing nightcap-frontend container"
# fi

# PULL LATEST IMAGES 
docker pull "$BACKEND_IMAGE"
docker pull "$FRONTEND_IMAGE"
sleep 5
echo "Pulling latest Docker images.."
sleep 5


# # BUILD DOCKER NETWORK
# echo "Creating Docker network: $NETWORK_NAME"
# docker network create "$NETWORK_NAME" && echo "Docker network '$NETWORK_NAME' created."

# CREATE AND RUN CONTAINERS 
echo "Starting backend container..."
sleep 5

if [ -f "$ENV_FILE" ]; then
  docker run -d \
    --env-file "$ENV_FILE"\
    --name nightcap-backend \
    -p 8000:8000 \
    "$BACKEND_IMAGE"
else
  echo "ERROR: .env file not found at $ENV_FILE. Backend container not started."
  exit 1
fi

echo "Starting frontend container..."
sleep 5

if [ -f "$ENV_FRONTEND" ]; then 
  docker run -d \
    --env-file "$ENV_FRONTEND" \
    --name nightcap-frontend \
    -p 3000:3000 \
    "$FRONTEND_IMAGE"
else
  echo "ERROR: .env.production file not found at $ENV_FRONTEND. Frontend container not started."
  exit 1
fi 


sleep 5

