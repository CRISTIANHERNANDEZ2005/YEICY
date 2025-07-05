# Migración a Neon.tech PostgreSQL

## Resumen

Este documento describe el proceso de migración de la base de datos SQLite local a PostgreSQL alojado en Neon.tech. La migración se realizó para mejorar la escalabilidad, rendimiento y características avanzadas que ofrece PostgreSQL en un entorno de nube.

## Cambios realizados

1. **Instalación de dependencias**:
   - Se agregó `psycopg2-binary` para la conexión con PostgreSQL

2. **Configuración de variables de entorno**:
   - Se creó un archivo `.env` para almacenar de forma segura las credenciales de la base de datos
   - Se configuró la aplicación para cargar estas variables usando `python-dotenv`

3. **Modificación de la configuración de Django**:
   - Se actualizó `settings.py` para usar PostgreSQL en lugar de SQLite
   - Se implementó la carga de configuración desde variables de entorno
   - Se ajustaron los parámetros de conexión específicos para Neon.tech

4. **Migración de datos**:
   - Se ejecutaron las migraciones en la nueva base de datos
   - Se creó un superusuario para el panel de administración

## Estructura de la base de datos

La estructura de la base de datos se mantiene igual que en la versión SQLite, con las siguientes tablas principales:

- `productos_categoria`: Almacena las categorías de productos
- `productos_producto`: Almacena los productos con referencias a sus categorías

## Ventajas de la migración

1. **Escalabilidad**: PostgreSQL maneja mejor grandes volúmenes de datos
2. **Concurrencia**: Mejor manejo de conexiones simultáneas
3. **Características avanzadas**: Índices avanzados, búsqueda de texto completo, tipos de datos JSON
4. **Respaldos automáticos**: Neon.tech proporciona respaldos automáticos
5. **Alta disponibilidad**: Servicio gestionado con alta disponibilidad

## Consideraciones para producción

1. **Seguridad**:
   - Asegúrate de que las credenciales de la base de datos estén protegidas
   - No incluyas el archivo `.env` en el control de versiones
   - Considera usar un gestor de secretos para producción

2. **Rendimiento**:
   - Monitorea el rendimiento de las consultas
   - Considera implementar caché para consultas frecuentes

3. **Costos**:
   - Neon.tech ofrece un plan gratuito con limitaciones
   - Monitorea el uso para evitar cargos inesperados en planes de pago

## Solución de problemas

- Si encuentras errores de conexión, verifica que las credenciales en el archivo `.env` sean correctas
- Para problemas específicos con Neon.tech, consulta su [documentación oficial](https://neon.tech/docs/)
- Si necesitas volver a SQLite temporalmente, puedes modificar la configuración en `settings.py`