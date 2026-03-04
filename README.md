# DevOps Portfolio - EKS Deployment

Simple FastAPI microservice containerized with Docker.

## Local run
cd app
docker build -t portfolio-api:local .
docker run --rm -p 8080:8080 -e APP_VERSION=local portfolio-api:local

## Endpoints
GET /health
GET /version
