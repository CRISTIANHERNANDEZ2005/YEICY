#!/bin/bash

# Actualizar el sistema e instalar dependencias necesarias
apt-get update
apt-get install -y python3-dev build-essential

# Instalar las dependencias de Python
pip install --upgrade pip
pip install -r requirements.txt

# Ejecutar las migraciones de Django y recolectar archivos estáticos
python manage.py migrate --noinput
python manage.py collectstatic --noinput