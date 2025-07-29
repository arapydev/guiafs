# Usamos una imagen oficial de Python como base
FROM python:3.11-slim

# Establecemos variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Creamos un directorio para la app dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos e instalamos las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código de nuestro proyecto al contenedor
COPY . /app/

# Exponemos el puerto 8000 para que el mundo exterior pueda conectarse
EXPOSE 8000

# Nuevo paso: Recolectar todos los archivos estáticos
RUN python manage.py collectstatic --noinput

# El comando que se ejecutará cuando el contenedor inicie
# Inicia Gunicorn con 2 workers, escuchando en el puerto 8000
# Línea nueva y correcta
# Línea nueva y correcta
CMD gunicorn --bind 0.0.0.0:$PORT --workers 2 core.wsgi:application