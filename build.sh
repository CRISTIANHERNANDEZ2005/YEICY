#!/bin/bash

# Actualizar el sistema e instalar dependencias necesarias
#!/bin/bash

# Configurar entorno seguro sin dependencias de sistema

# Instalar las dependencias de Python
#!/bin/bash

# Instalar dependencias en entorno aislado
python -m venv .venv
source .venv/bin/activate

# Versiones específicas compatibles con Render
python -m pip install --upgrade pip==23.3.2 setuptools==68.2.2 wheel==0.42.0

# Instalar Pillow con wheel precompilado
pip install --use-pep517 --only-binary=:all: Pillow==10.3.0

# Instalar resto de dependencias
pip install -r requirements.txt --no-cache-dir

# Verificar instalación de Django
python -c "import django; print(f'Django version: {django.__version__}')"

# Ejecutar las migraciones de Django y recolectar archivos estáticos
python manage.py migrate --noinput
python manage.py collectstatic --noinput