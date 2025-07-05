#!/bin/bash

# Actualizar el sistema e instalar dependencias necesarias
apt-get update
apt-get install -y python3-dev build-essential libjpeg-dev zlib1g-dev libpng-dev

# Instalar las dependencias de Python
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt --no-cache-dir

# Ejecutar las migraciones de Django y recolectar archivos estáticos
python manage.py migrate --noinput
python manage.py collectstatic --noinput