@echo off
echo Running database migrations...
docker-compose exec web python manage.py migrate
echo.
echo Migrations completed.
