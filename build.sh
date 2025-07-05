#!/bin/bash

# Crear y activar entorno virtual
python -m venv .venv
source .venv/bin/activate

# Instalar las versiones más recientes de pip/setuptools/wheel
python -m pip install --upgrade pip setuptools wheel

# Instalar psycopg 3.2.x que es compatible con Python 3.13
pip install --no-cache-dir "psycopg[binary,pool]==3.2.8"

# Instalar Django 5.x que es compatible con Python 3.13
pip install --no-cache-dir "Django==5.0.4"

# Instalar Pillow
pip install --no-cache-dir "Pillow==11.0.0"

# Instalar el resto de dependencias (actualizadas para compatibilidad)
pip install --no-cache-dir -r requirements.txt

# Verificar instalación
python -c "import django; print(f'Django version: {django.__version__}')"

# Ejecutar migraciones y recolectar estáticos
python manage.py migrate --noinput
python manage.py collectstatic --noinput