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