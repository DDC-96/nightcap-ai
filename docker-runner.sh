#!/bin/sh

# VARS
DOCKER_USER=""
BACKEND_IMAGE="$DOCKER_USER/nightcap-backend:latest"
FRONTEND_IMAGE="$DOCKER_USER/nightcap-frontend:latest"
FRONTEND_URL=""
BACKEND_URL=""

# REMOVE EXISIGING CONTAINERS 
docker rm -f nightcap-frontend nightcap-backend 2>/dev/null || true

# PULL IMAGES 
docker pull --platform "$PLATFORM" "$BACKEND_IMAGE"
docker pull --platform "$PLATFORM" "$FRONTEND_IMAGE"

# DOCKER NETWORK BUILD
docker network rm nightcap-net 2>/dev/null || true 
docker network create nightcap-net

# Run Docker Containers locally
docker run -d \
    --name nightcap-backend \
    --network nightcap-net \
    -p xxxx:xxxx "$BACKEND_IMAGE"

docker run -d \
    --name nightcap-frontend \
    --network nightcap-net \
    -p xxxx:xxxx "$FRONTEND_IMAGE"


echo "Frontend URL: "$FRONTEND_URL" "
echo "Backend URL: "$BACKEND_URL" "

