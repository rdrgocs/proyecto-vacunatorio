# Vacunatorio Coelemu 💉

_Vacunatorio Coelemu es una plataforma web que permite el control interno de vacunaciones dentro del establecimiento, teniendo un fácil acceso a la información de los pacientes vacunados y por vacunar, además de las vacunas disponibles_


## Comenzando 🚀

### Pre-requisitos 📋

_Tener instalado python3, GIT (con la configuración inicial) y MySQL en el computador_

### Clonar proyecto 🧲

_Para clonar este proyecto en su computador debe seguir las siguientes instrucciones:_

* **1. Abrir una consola**
* **2. Dirigirse a la ruta en la que desea clonar el archivo**
* **3. Ejecutar el comando: git clone https://github.com/rdrgocs/vacunatorio-coelemu.git**

### Instalación 🔧

_Para instalar y descargar todas las dependencias necesarias para el correcto funcionamiento debe seguir los siguientes pasos:_

```bash
pip install -U pip
pip install -r requirements.txt
```
_En el caso que le aparezca error de acceso debe poner el siguiente comando:_
```bash
pip install -U pip --user
```

_En el caso de que en el momento de ejecutar el comando de instalación de requirements.txt muestre un error fatal de nombre "Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/" se deben seguir los siguientes pasos para solucionarlo, ya que estos ocurre sólo en algunos computadores._

* **Ir al sitio: https://www.lfd.uci.edu/~gohlke/pythonlibs/**
* **Buscar el archivo tipo mysql-client correspondiente a la versión de python instalada en el computador (Ctrl + F para buscar más rápido dentro de la página) y luego descargarlo.**
* **Por ejemplo, si se usa la versión de 3.8 de python y windows se debe descargar el archivo "mysqlclient‑1.4.6‑cp38‑cp38‑win32.whl" y el archivo "mysqlclient‑1.4.6‑cp38‑cp38‑win_amd64.whl" que son las dos opciones que corresponderán según su procesador.**
* **Una vez descargado el archivo, abra una consola(o terminal) y diríjase a la ruta en la que está almacenado el archivo descargado (probablemente la carpeta descargas) y ejecute el comando:**

```bash
pip install mysqlclient‑1.4.6‑cp38‑cp38‑win32.whl
```

* **En el caso que diga que no puede instalar ese, ejecutamos la otra versión descargada que en este caso sería la amd:**

```bash
mysqlclient‑1.4.6‑cp38‑cp38‑win_amd64.whl
```

* **Ahora que ya lo tenemos instalado, con la consola volvemos a la carpeta de el proyecto y ejecutamos nuevamente el comando:**

```bash
pip install -r requirements.txt
```

### Creación de base de datos local 💾

_Debe crear una base de datos local con las siguientes características:_

* **Nombre base de datos: vacunatorio**
* **Usuario base de datos: root**
* **Sin contraseña**

_luego debe ejecutar el script SQL llamado vacunatorioCoelemu.sql para obtener la estructura y datos de prueba para la aplicación._

## Inicio de la aplicación 💻

_Debe abrir una consola y situarse en la carpeta donde clonó el proyecto, luego debe ejecutar el siguiente comando:_

```bash
python app.py
```

_Al ejecutar ese comando se levantará un servidor local en su equipo y la aplicación se encontrará en el puerto 5000._
_Para visualizar y usar la aplicación usted debe escribir en el navegador alguna de estas dos opciones: **localhost:5000** o **127.0.0.1:5000**_

* **IMPORTANTE: NO CERRAR LA CONSOLA HASTA TERMINAR DE USAR LA APLICACIÓN**

## Construido con 🛠️

_La aplicación web fue desarrollada en el lenguaje Python, potenciada con el framework Flask y el motor de plantillas Jinja2, además de una base de datos MySQL_

* **Lenguaje de programación: Python**
* **Framework utilizado: Flask**
* **Motor de plantillas: Jinja2**
* **Motor de base de datos: MySQL**


## Autores ✒️

* **Rodrigo Carvajal Sandoval** - [rdrgocs](https://github.com/rdrgocs)
* **Nicolás Ruiz San Martín** - [nicoarsm](https://github.com/nicoarsm)

## Nota 📄

_Este proyecto fue desarrollado como exigencia para aprobar la asignatura "Desarrollo Avanzado de Aplicaciones Web con Python" en la Universidad del Bío-Bío_