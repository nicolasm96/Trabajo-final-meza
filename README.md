## proyecto

- Crear una pagina de compra y venta de camiseta de furbol, tanto vintaje como de los ultimos años

## CreaciÃ³n de la estructura del proyecto

- Crear la carpeta `TuPrimeraPagina+Meza 2`
- Abrir VSCode en esa carpeta

## Crear el entorno virtual

```bash
python -m venv .venv
```

- Activar el entorno desde VSCode como se indica en las diapositivas.

## Crear la estructura del proyecto

- Crear la carpeta `project` (mkdir project)
- Crear el archivo `.gitignore`
- Crear el archivo `README.md`

## InstalaciÃ³n de Django

```bash
pip install django
```

## Crear el proyecto Django y ejecutar el servidor Django

```bash
cd project
django-admin startproject config .
python manage.py runserver
```

- Abrir el navegador y ejecutar el servidor Django en la direcciÃ³n `127.0.0.1:8000`


## Crear la app home

- Crear la app `home` (django-admin startapp home)
- en config en la parte de seting agregamos `home` a  `INSTALLED_APPS`
- en viwes creamos la funcion index
- definimos nuestra `url`("")
- creamos la carpeta templates/comentario
- creamos nuestro archivo `base.html`
- definimos la herencia
- creamos nuestro archivo `index.html`
- en el archivo index utilizamos la herencia de `home/base.html`
- se agregar href que redireccionaran a las paguinas creadas
- creamos otro archivo llamado `about.html`
- -definimos nuestra `url`(about/)
- en el archivo crear utilizamos la herencia de `home/base.html`
- completamos lo que queremos visualizar dentro del html


## Crear la app comentario

- Crear la app `comentario` (django-admin startapp comentario)
- en config en la parte de seting agregamos `comentario` a  `INSTALLED_APPS`
- en carpeta `models.py` creamos las clase comentario
- en viwes creamos la funcion index
- agregamos un forms `comentarioFrom`
- definimos nuestra `url`("")
- creamos la carpeta templates/comentario
- creamos nuestro archivo `index.html`
- en el archivo index utilizamos la herencia de `home/base.html`
- completamos lo que queremos visualizar dentro del html
- creamos otro archivo llamado `exito_comentario.html`
- -definimos nuestra `url`(exito_comentario/)
- en el archivo crear utilizamos la herencia de `home/base.html`
- completamos lo que queremos visualizar dentro del html
- python manage.py makemigrations
- python manage.py migrate


## Crear la app cliente

- Crear la app `cliente` (django-admin startapp cliente)
- en config en la parte de seting agregamos `cliente` a  `INSTALLED_APPS`
- en carpeta `models.py` creamos las clases pais y cliente
- en viwes creamos la funcion index
- definimos nuestra `url`("")
- creamos la carpeta templates/cliente
- creamos nuestro archivo `index.html`
- en el archivo index utilizamos la herencia de `home/base.html`
- completamos lo que queremos visualizar dentro del html
- agregamos un forms con la creacion de cliente
- en viwes creamos la funcion `crear`
- -definimos nuestra `url`(crear/)
- dentro de templates/cliente se creo un archivo `crear.html`
- en el archivo crear utilizamos la herencia de `home/base.html`
- completamos lo que queremos visualizar dentro del html
- python manage.py makemigrations
- python manage.py migrate


## Crear la app  compraventa (en desarollo)

- Crear la app `compraventa` (django-admin startapp cliente)
- en config en la parte de seting agregamos `compraventa` a  `INSTALLED_APPS`
-`sigue en desarollo`



## InicializaciÃ³n de Git

Posicionarse el la raiz del proyecto:

```bash
git init
```

## Primer commit y nueva rama de desarrollo

```bash
git add .
git commit -m "Primer commit"
```

## Comandos para Git

Para mostrar las ramas:
```bash
git branch
```


