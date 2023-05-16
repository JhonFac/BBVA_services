#!/bin/sh

set -e
# start Container
echo "Contenedor iniciado"
echo "$(date): Ejecutando proceso"

# Copiar los archivos de certificado al directorio de nginx
#cp /scripts/fullchain.pem /etc/ssl/certs/
#cp /scripts/privkey.pem /etc/ssl/private/
#cp /scripts/options-ssl-nginx.conf /etc/nginx/

# Iniciar nginx con la configuración adecuada para HTTPS 

python manage.py makemigrations
python manage.py migrate
#python manage.py runserver 0.0.0.0:$PORT
#python manage.py runserver 0.0.0.0:8000
gunicorn BBVA.wsgi:application --bind 0.0.0.0:443 --certfile ./fullchain.pem --keyfile ./privkey.pem
