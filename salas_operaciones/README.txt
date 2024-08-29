Instalación del entorno de ejecución y dependencias
===================================================
1. Crear entorno virtual python version 3.12.4
2. Instalar django version 5.0.6
3. Instalar pip
4. Instalar las siguientes librerías
    pip install asgiref==3.8.1
    Django==5.0.6
    psycopg==3.2.1
    psycopg2==2.9.9
    setuptools==69.5.1
    sqlparse==0.5.0
    typing_extensions==4.12.2
    wheel==0.43.0

Instalación de base de datos
============================
Para utilizar esta aplicación debe tener instalado un servidor de base de datos PostgreSQL y tener permisos de ejecución
y creación de objetos.

6. Crear base de datos [nombre_de_base_de_datos] en PostgreSQL
7. Ejecutar el script "salas_operaciones.sql" en una hoja de ejecución SQL. Para esto puede hacerlo
desde cualquier cliente PostgreSQL dentro de la base de datos [nombre_de_base_de_datos]

Instalación de la aplicación
============================
8. Descomprima el archivo [nombre_de_archivo_zip].

Se asume que el servidor PostgreSQL es accesible desde el host en el que que se ejecutará la conexión.
Si tiene dudas de la conectividad entre ambos hosts revise la documentación de PostgreSQL.

9. Coloque las credenciales de acceso a base de datos en el archivo "/salas_operaciones/settings.py",
reemplazando la seccion DATABASES del archivo para que quede como se muestra:

DATABASES = {
    "default": {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': 'salas_operaciones',
        'USER': <- Acá colocar el usuario de acceso a la base de datos en su servidor PostgreSQL
        'PASSWORD':  <- Acá colocar la password de acceso a la base de datos en su servidor PostgreSQL
        'HOST': '127.0.0.1', <- IP del host de base datos, si es local mantener este valor.
        'PORT': '5432' <- Puerto de acceso a la base de base datos, este es el valor por defecto.
    },
}

Ejecución de la aplicación
==========================
Para ejecutar la aplicación debe escribir el siguiente comando en su terminal, dentro del entorno virtual que está utilizando.

python manage.py runserver

Asegúrese de ejecutar esta instrucción en la carpeta que contiene el archivo manage.py que es la siguiente:

/salas_operaciones

La aplicación por defecto se ejecuta en el puerto 8000 del host. Si necesita ejecutarla en otro puerto,
debe especificarlo al levantar el servidor:

python manage.py runserver [numero de puerto]

Acceso a la aplicación
======================
Para entrar al administrador Django de la aplicación debe escribir la siguiente URL en su navegador web:

http://127.0.0.1:8000/admin

Las credenciales de acceso por default son:

user: admin
password: admin

Para ingresar a la aplicación debe escribir lo siguiente en su navegador:

http://127.0.0.1:8000/

Los usuarios registrados con sus respectivas claves son:

user: admin
password: admin
perfil: administrador

user: ngorosito
password: m.123456
perfil: veterinario

user: doc@gmail.com
password: m.123456
perfil: veterinario