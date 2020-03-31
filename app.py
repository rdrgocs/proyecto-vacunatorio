#INTEGRANTES: RODRIGO CARVAJAL SANDOVAL (19.333.972-7) - NICOLÁS RUIZ SAN MARTIN (19.716.810-2)

import requests
import ctypes
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from datetime import date, datetime


app = Flask(__name__)

app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "vacunatorio"
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

#PAGINA PRINCIPAL LISTAR PACIENTES
@app.route('/')
def listar_pacientes():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nombre_paciente,rut_paciente,DATE_FORMAT(fecha_nacimiento, '%d/%m/%Y') FROM paciente")
    data = cursor.fetchall()
    return render_template('listado_pacientes.html', pacientes = data)

#PAGINA PARA AGREGAR PACIENTE
@app.route('/paciente/add')
def mostrar_add_paciente():
        return render_template('nuevo_paciente.html')


#PAGINA PARA LISTAR TODOS LOS PACIENTES QUE SE HAN VACUNADO CON DICHA VACUNA
@app.route('/vacunas/<string:nombre_vacuna>/pacientes')
def listar_pacientes_por_vacuna(nombre_vacuna):

    #LISTAR PACIENTES POR VACUNA
    cursor_pacientes_vacuna = mysql.connection.cursor()
    query = "SELECT P.nombre_paciente, P.rut_paciente, DATE_FORMAT(R.fecha_vacuna, '%d/%m/%Y') FROM paciente P, vacuna V, recibe R WHERE P.rut_paciente = R.rut_paciente AND V.nombre_enfermedad = R.nombre_enfermedad AND V.nombre_enfermedad = '" + nombre_vacuna + "'"
    cursor_pacientes_vacuna.execute(query)
    data_pacientes_vacuna = cursor_pacientes_vacuna.fetchall()
    return render_template('listado_vacunas_por_paciente.html', pacientes = data_pacientes_vacuna, nombre = nombre_vacuna)

#AGREGA PACIENTE A BD
@app.route('/paciente/add/agregar', methods=['POST'])
def add_paciente():
        if request.method == 'POST':
                nombre = request.form['nombre']
                run = request.form['run']
                fechaNto = request.form['fechaNto']
                cur = mysql.connection.cursor()
                cur.execute('SELECT COUNT(*) FROM paciente WHERE rut_paciente = %s',[run])
                count_row = cur.fetchone()
                count = count_row[0]
                if count == 0:
                        cur.execute('INSERT INTO paciente (nombre_paciente,rut_paciente,fecha_nacimiento) VALUES (%s, %s, %s)',
                                (nombre, run, fechaNto))
                        mysql.connection.commit()
                        flash('Paciente ingresado satisfactoriamente')
                        return redirect(url_for('listar_pacientes'))
                else:
                        flash('El paciente ya se encuentra registrado en el sistema')
                        return redirect(url_for('listar_pacientes'))

#PAGINA PARA LISTAR LAS VACUNAS QUE TIENE UN PACIENTE
@app.route('/paciente/<string:rut>/vacunas')
def listar_vacunas_paciente(rut):

    #LISTAR VACUNAS POR PACIENTE
    cursor_vacunas_paciente = mysql.connection.cursor()
    query = "SELECT V.nombre_enfermedad,DATE_FORMAT(R.fecha_vacuna, '%d/%m/%Y') FROM paciente P, recibe R, vacuna V WHERE P.rut_paciente = R.rut_paciente AND R.nombre_enfermedad = V.nombre_enfermedad AND P.rut_paciente = '" + rut +"'"
    cursor_vacunas_paciente.execute(query)
    data_vacunas_paciente = cursor_vacunas_paciente.fetchall()

    #OBTENER NOMBRE DE PACIENTE
    cursor_nombre_paciente = mysql.connection.cursor()
    cursor_nombre_paciente.execute('SELECT nombre_paciente FROM paciente WHERE rut_paciente = %s',[rut])
    data_nombre_paciente = cursor_nombre_paciente.fetchall()
    return render_template('vacunas_paciente.html', vacunas = data_vacunas_paciente, nombres = data_nombre_paciente)

#PAGINA PARA VACUNAR PACIENTE
@app.route("/paciente/<string:rut>/addVacuna")
def mostrar_vacunar_paciente(rut):

        #RECUPERAR DATOS DEL PACIENTE
        cursor_paciente = mysql.connection.cursor()
        query = "SELECT nombre_paciente,rut_paciente,DATE_FORMAT(fecha_nacimiento, '%d/%m/%Y') FROM paciente WHERE rut_paciente = '" + rut + "'"
        cursor_paciente.execute(query)
        data_paciente = cursor_paciente.fetchall()

        #RECUPERAR VACUNAS
        cursor_vacunas = mysql.connection.cursor()
        cursor_vacunas.execute('SELECT nombre_enfermedad FROM vacuna')
        data_vacunas = cursor_vacunas.fetchall()
        return render_template('vacunar_paciente.html', vacunas = data_vacunas, paciente = data_paciente)

@app.route("/paciente/<string:rut>/addVacuna/agregar", methods=['POST'])
def vacunar_paciente(rut):
        if request.method == 'POST':
                vacuna = request.form['vacuna']
                rutAux = rut
                cur = mysql.connection.cursor()
                cur.execute('SELECT COUNT(*) FROM recibe WHERE rut_paciente = %s AND nombre_enfermedad = %s', (rut,vacuna))
                count_row = cur.fetchone()
                count = count_row[0]
                if count == 0:
                        cur.execute('INSERT INTO recibe (rut_paciente,nombre_enfermedad,fecha_vacuna) VALUES (%s,%s,%s)', (rutAux,vacuna,date.today()))
                        mysql.connection.commit()
                        flash('Paciente vacunado satisfactoriamente')
                        return redirect(url_for('listar_vacunas_paciente',rut=rutAux))
                else:
                        flash('El paciente ya ha recibido anteriormente la vacuna antes seleccionada')
                        return redirect(url_for('listar_vacunas_paciente',rut=rutAux))


#LISTADO DE VACUNAS
@app.route('/vacunas')
def listar_vacunas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nombre_enfermedad,DATE_FORMAT(fecha_registro, '%d/%m/%Y') FROM vacuna")
    data = cursor.fetchall()
    return render_template('listado_vacunas.html', vacunas = data)

#PAGINA PARA AGREGAR VACUNA
@app.route('/vacuna/add')
def mostrar_add_vacuna():
        return render_template('nueva_vacuna.html')

#AGREGA VACUNA A BD
@app.route('/vacuna/add/agregar', methods=['POST'])
def add_vacuna():
        if request.method == 'POST':
                nombre = request.form['nombre']
                cur = mysql.connection.cursor()
                cur.execute('SELECT COUNT(*) FROM vacuna WHERE nombre_enfermedad = %s', [nombre])
                count_row = cur.fetchone()
                count = count_row[0]
                if count == 0:
                        cur = mysql.connection.cursor()
                        cur.execute('INSERT INTO vacuna (nombre_enfermedad,fecha_registro ) VALUES (%s,%s)',
                                (nombre,date.today()))
                        mysql.connection.commit()
                        flash('Vacuna ingresada satisfactoriamente')
                        return redirect(url_for('listar_vacunas'))
                else:
                        flash('La vacuna que se desea ingresar ya se encuentra registrada')
                        return redirect(url_for('listar_vacunas'))

if __name__ == "__main__":
	app.run(debug=True)
