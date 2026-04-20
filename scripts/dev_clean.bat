@echo off
echo Stopping and removing all containers, networks, and volumes...
docker-compose down -v --rmi all --remove-orphans
echo.
echo Cleanup completed. WARNING: All data has been deleted!
