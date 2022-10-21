# BIBLIOTECA con Django
Proyecto realizado con Django 4.X para crear un portal para la gestión de nuestra propia biblioteca administrando las ubicaciones, insertando los géneros literarios, así como las editoriales de nuestros betsellers y nuestros autores favoritos, todo ello tener nuestros libros gestionados por MyBiblio y siempre controlados de donde se encuentra.

## Ejecutar correctamente el proyecto con Django

Como no he podido subir el proyecto a un servidor por falta de tiempo, arrancaremos el proyecto con una combinación de docker-compose y usar python3.

### Requisitos
Python version >=3.8
Docker version >=20.10.16
Docker-compose version >=1.25.0


### Clonar el respositorio.
Lo primero de todo es clonar el repositorio dentro de alguna caperta de nuestro ordenador.  Para ello accedemos a la web https://github.com/Chegarra/django_biblioteca y clonamos el repositorio.  Yo os pongo el clonado con el uso de HTTPS.
```
git clone https://github.com/Chegarra/django_biblioteca.git
```

### Arrancar PostgreSQL
Una vez clonado el repositorio, entramos en la carpeta **django_biblioteca** y modificaremos el documento `docker-compose.yml` usando un editor, como por ejemplo el nano
```sh
cd django_biblioteca/
nano docker-compose.yml
```
Una vez dentro del documento buscamos en el servicio **db** la etiqueta **volumes:** y comentamos o eliminamos la linea existente y creamos una nueva tal y como indica el comentario.  Una vez realizado el cambio, guardamos y salimos fuera del editor.  Ejecutamos la siguiente instrucción para arrancar el gestor de bases de datos **PostgreSQL**
```sh
docker-compose up --build -d db
docker-compose ps
```
Si todo ha ido correcto, al hacer _docker ps_ debería aparecer un contenedor con el gestor de base de datos lenvantado.  Ya tenemos el primer componente.

### Arrancar entorno virtual
Para instalar las liberias necesarias que harán funcionar correctamente el proyecto, deberemos crear un entorno virtual, activarlo correctamente e instalar todas las librerias del documento  `requirement.txt`.  Para ello podemos ejecutar el siguiente grupo de lineas para ello y esperamos a que se instale todo.
```
python3 -m venv entorno_biblioteca
. entorno_biblioteca/bin/activate
python3 -m pip install -r requirements.txt
```
PD: Si hay algún problema con el psycopg2-binary, pueden intentar con psycopg2.


### Arrancar el proyecto djanto y realizar su 1a configuración
Ya tenemos conectado el PostgreSQL y creado el entorno virtual, ahora toca ejecutar el proyecto.  Para ello vamos a entrar en la carpeta **biblioteca** donde se encontrará el documento `manage.py` y ejecutaremos los comandos para crear las tablas necesarias para que Django funcione correctamente y así poder acceder al proyecto.  Antes de arrancar el servidor, siempre va bien crear un super usuario para acceder al portal del administrador, para ello ejecutamos el comando de createsuperuser y seguimos las instruccions.

Una vez ya tenemos el usuario, ya podemos ejecutar el runserver.
```
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
Si todo ha ido bien, en la terminal no debería aparecer ningún error y debería poner un mensaje parecido a las siguientes lienas:
```
Django version 4.1.2, using settings 'biblioteca.settings.desa'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
PD: El runserver ya está configurado para que seleccione la configuración necesaría sin necesidad de recurrir a la opcción de _--settings_

### Acceder al proyecto Django MyBiblio
Ahora podemos acceder desde un navegador al http://localhost:8000 y nos deberá aparecer la página de inicio del proyecto.  Si queremos entrar al Administrador de Django, acedamos a la siguiente url: http://localhost:8000/admin y usamos las credenciales creadas con el comando superuser para logearnos.

## Primeros pasos

Dentro de la web, existen 5 apartados principales: Libro, Autor, Género, Ubicación y Editorial.

Recomiendo añadir primero algunos Géneros, Editoriales, Ubicaciones y Autores antes de crear registrar los libros, ya que son campos obligatorios y están referenciados como claves ajenas.  Y ya disfrutar y navegar por la interfaz web creada para la gestión de nuestra biblioteca.

PD: Tambíen se puede gestionar mediante el Administrador de Django (http://localhost:8000/admin), pero recomiendo la interfaz.
