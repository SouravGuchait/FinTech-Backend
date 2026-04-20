@echo off
echo Starting development environment...
docker-compose up -d
echo.
echo Environment started. Containers:
docker-compose ps
