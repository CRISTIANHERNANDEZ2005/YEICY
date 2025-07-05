# Sistema de Gestión de Productos y Categorías

Este es un sistema de gestión de productos y categorías desarrollado con Django. Permite administrar un catálogo de productos organizados por categorías, con funcionalidades completas de CRUD (Crear, Leer, Actualizar, Eliminar) para ambas entidades.

## Características

### Gestión de Categorías
- Listado de categorías
- Creación de nuevas categorías
- Visualización detallada de categorías
- Edición de categorías existentes
- Eliminación de categorías

### Gestión de Productos
- Listado de productos con filtrado por categoría
- Creación de nuevos productos
- Visualización detallada de productos
- Edición de productos existentes
- Eliminación de productos
- Gestión de imágenes de productos

### Características Técnicas
- Interfaz de usuario moderna con Bootstrap 5
- Diseño responsivo para dispositivos móviles y de escritorio
- Validación de formularios
- Mensajes de retroalimentación para el usuario
- Confirmación para acciones destructivas

## Tecnologías Utilizadas

- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, JavaScript
- **Frameworks CSS**: Bootstrap 5
- **Iconos**: Font Awesome
- **Base de datos**: PostgreSQL (Neon.tech)

## Base de datos

Este proyecto utiliza PostgreSQL (Neon.tech) como base de datos.

Para desplegar en Render.com, se recomienda usar la variable de entorno `DATABASE_URL` para la configuración de la base de datos.

Para configurar localmente, crea un archivo `.env` con las variables de entorno necesarias.

Consulta el archivo `NEON_MIGRATION.md` para más detalles sobre la configuración y migración a PostgreSQL.

## Instalación

1. Clona este repositorio
2. Crea un entorno virtual: `python -m venv venv`
3. Activa el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Crea un archivo `.env` en la raíz del proyecto con las variables de entorno necesarias (ver `.env.example`)
5. Instala las dependencias: `pip install -r requirements.txt`
6. Realiza las migraciones: `python manage.py migrate`
7. Crea un superusuario: `python manage.py createsuperuser`
8. Inicia el servidor: `python manage.py runserver`

> **Nota**: Para más detalles sobre la configuración de la base de datos PostgreSQL en Neon.tech, consulta el archivo `NEON_MIGRATION.md`.

## Estructura del Proyecto

```
tienda/              # Directorio principal del proyecto Django
├── settings.py      # Configuración del proyecto
├── urls.py          # URLs principales del proyecto
└── ...

productos/           # Aplicación de productos y categorías
├── models.py        # Modelos de datos (Producto, Categoría)
├── views.py         # Vistas para manejar las peticiones
├── urls.py          # URLs de la aplicación
├── forms.py         # Formularios para validación de datos
├── admin.py         # Configuración del panel de administración
└── templates/       # Plantillas HTML
    └── productos/   # Plantillas específicas de la aplicación
        ├── categorias/  # Plantillas para gestión de categorías
        └── productos/   # Plantillas para gestión de productos

static/              # Archivos estáticos
├── css/             # Hojas de estilo
├── js/              # Scripts JavaScript
└── img/             # Imágenes estáticas

media/               # Archivos subidos por los usuarios
└── productos/       # Imágenes de productos
```

## Uso

1. Accede a la aplicación en `http://localhost:8000/`
2. Crea categorías desde el menú "Categorías"
3. Añade productos asignándolos a las categorías creadas
4. Gestiona tu inventario actualizando los productos según sea necesario

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.