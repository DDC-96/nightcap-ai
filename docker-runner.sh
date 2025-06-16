#!/bin/sh

# VARS
DOCKER_USER="dcruzdevops"
BACKEND_IMAGE="$DOCKER_USER/nightcap-backend:latest"
FRONTEND_IMAGE="$DOCKER_USER/nightcap-frontend:latest"
FRONTEND_URL="http://localhost:3000"
BACKEND_URL="http://localhost:8000/docs"
PLATFORM="linux/amd64"

# REMOVE EXISIGING CONTAINERS 
docker rm -f nightcap-frontend nightcap-backend 2>/dev/null || true

# PULL IMAGES 
docker pull --platform "$PLATFORM" "$BACKEND_IMAGE"
docker pull --platform "$PLATFORM" "$FRONTEND_IMAGE"

# DOCKER NETWORK
docker network rm nightcap-net 2>/dev/null || true 
docker network create nightcap-net

# Run Docker Containers locally
docker run -d \
    --platform $PLATFORM \
    --name nightcap-backend \
    --network nightcap-net \
    -p 8000:8000 "$BACKEND_IMAGE"

docker run -d \
    --platform $PLATFORM \
    --name nightcap-frontend \
    --network nightcap-net \
    -p 3000:3000 "$FRONTEND_IMAGE"



echo "Nightcap is now running."
echo "Frontend URL: "$FRONTEND_URL" "
echo "Backend URL: "$BACKEND_URL" "

