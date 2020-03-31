/*INTEGRANTES: 
    RODRIGO CARVAJAL SANDOVAL (19.333.972-7)
    NICOLÁS RUIZ SAN MARTÍN (19.716.810-2)
*/

CREATE TABLE paciente (
  nombre_paciente varchar(100),
  rut_paciente varchar(12) NOT NULL,
  fecha_nacimiento date,
  primary key (rut_paciente)
);

CREATE TABLE vacuna (
  nombre_enfermedad varchar(100) NOT NULL,
  fecha_registro DATE NOT NULL,
  primary key (nombre_enfermedad)
);

CREATE TABLE recibe (
  rut_paciente varchar(12),
  nombre_enfermedad varchar(100),
  fecha_vacuna DATE,
  foreign key (rut_paciente) references paciente(rut_paciente),
  foreign key (nombre_enfermedad) references vacuna(nombre_enfermedad),
  primary key (rut_paciente,nombre_enfermedad)
);

INSERT INTO paciente (nombre_paciente, rut_paciente, fecha_nacimiento) VALUES
    ('Andrea Gonzalez Escobar','16943162-0','1986/12/01'),
    ('Jorge Rebolledo Soto','16383423-5','1985/11/02'),
    ('Catalina Vargas Pardo','14517866-5','1979/10/03'),
    ('Rodrigo Zapata Cordova','11124288-7','1969/09/13'),
    ('Natalia Barra Gutierrez','8870332-4','1954/08/05'),
    ('Darlyng Saavedra Avila','15584667-4','1981/07/12'),
    ('Ricardo Cardoso Morente','18102958-7','1993/06/22'),
    ('Manuel Quiroga Granero','22802486-4','2001/05/11'),
    ('Marcos Heredia Cozar','7607401-1','1948/04/01'),
    ('Agustin Contreras Morilla','7021892-5','1946/03/30'),
    ('Oscar Lahoz Serrano','8256936-7','1953/02/24'),
    ('Victoria Galvan Canal','12527009-3','1972/01/26'),
    ('Carolina Gallego Recuero','16130923-0','1983/12/05'),
    ('Alba Piedra Cascales','18452935-1','1992/11/19'),
    ('Ines Porras Monserrat','9179852-2','1960/10/25'),
    ('Sandra Bernardez Reguera','17700892-3','1990/09/18'),
    ('Emilio Baena Arranz','5295370-7','1943/08/29'),
    ('Paula Gonzalez Escobar','19335947-7','1996/10/21'),
    ('Rodrigo Carvajal Sandoval','19333972-7','1996/06/07'),
    ('Nicolas Ruiz San Martin','19716810-2','1997/06/09');

  INSERT INTO vacuna (nombre_enfermedad, fecha_registro) VALUES
    ('Hepatitis A','2010/03/15'),
    ('Hepatitis B','2010/02/27'),
    ('Influenza','2011/03/19'),
    ('Paperas','2009/02/04'),
    ('Poliomelitis','2010/01/03'),
    ('Rotavirus','2008/09/18'),
    ('Varicela','2009/12/31'),
    ('Neumonia','2007/10/14'),
    ('SIDA','2012/03/15'),
    ('COVID-19','2020/02/24');

  INSERT INTO recibe (rut_paciente, nombre_enfermedad, fecha_vacuna) VALUES
    ('16943162-0','Hepatitis A','2019/12/24'),
    ('16943162-0','Paperas','2020/01/03'),
    ('16943162-0','Influenza','2008/08/08'),
    ('16943162-0','Varicela','2014/10/14'),
    ('16943162-0','COVID-19','2017/06/12'),
    ('16383423-5','Hepatitis B','2019/07/06'),
    ('16383423-5','Paperas','2020/01/03'),
    ('16383423-5','Rotavirus','2019/12/24'),
    ('16383423-5','Varicela','2019/07/06'),
    ('16383423-5','COVID-19','2008/08/08'),
    ('14517866-5','Influenza','2015/10/21'),
    ('14517866-5','Poliomelitis','2020/01/03'),
    ('14517866-5','Neumonia','2019/12/24'),
    ('14517866-5','COVID-19','2015/10/21'),
    ('11124288-7','Paperas','2017/06/12'),
    ('11124288-7','Rotavirus','2019/07/06'),
    ('11124288-7','Poliomelitis','2019/12/24'),
    ('11124288-7','Hepatitis B','2020/01/03'),
    ('8870332-4','Hepatitis A','2008/08/08'),
    ('8870332-4','Poliomelitis','2015/10/21'),
    ('8870332-4','Rotavirus','2019/12/24'),
    ('8870332-4','COVID-19','2015/10/21'),
    ('15584667-4','Influenza','2019/07/06'),
    ('15584667-4','Paperas','2008/08/08'),
    ('15584667-4','SIDA','2020/01/03'),
    ('15584667-4','Neumonia','2017/06/12'),
    ('18102958-7','SIDA','2019/07/06'),
    ('18102958-7','COVID-19','2020/01/03'),
    ('22802486-4','Neumonia','2015/10/21'),
    ('22802486-4','Poliomelitis','2008/08/08'),
    ('22802486-4','COVID-19','2019/07/06'),
    ('7607401-1','Rotavirus','2015/10/21'),
    ('7607401-1','Hepatitis A','2019/12/24'),
    ('7607401-1','Hepatitis B','2015/10/21'),
    ('7607401-1','Varicela','2017/06/12'),
    ('7021892-5','Influenza','2020/01/03'),
    ('7021892-5','Paperas','2015/10/21'),
    ('7021892-5','Rotavirus','2008/08/08'),
    ('7021892-5','SIDA','2019/12/24'),
    ('8256936-7','COVID-19','2019/07/06'),
    ('8256936-7','Varicela','2015/10/21'),
    ('12527009-3','Influenza','2019/12/24'),
    ('12527009-3','Paperas','2008/08/08'),
    ('12527009-3','Neumonia','2017/06/12'),
    ('16130923-0','COVID-19','2015/10/21'),
    ('18452935-1','Rotavirus','2019/12/24'),
    ('18452935-1','Poliomelitis','2020/01/03'),
    ('9179852-2','COVID-19','2019/07/06'),
    ('17700892-3','Influenza','2008/08/08'),
    ('5295370-7','SIDA','2019/07/06'),
    ('5295370-7','Influenza','2017/06/12'),
    ('19335947-7','Rotavirus','2019/12/24'),
    ('19335947-7','Varicela','2015/10/21'),
    ('19335947-7','SIDA','2019/07/06'),
    ('19335947-7','COVID-19','2019/12/24'),
    ('19335947-7','Paperas','2008/08/08'),
    ('19333972-7','Poliomelitis','2015/10/21'),
    ('19333972-7','SIDA','2020/01/03'),
    ('19333972-7','COVID-19','2017/06/12'),
    ('19333972-7','Influenza','2015/10/21'),
    ('19716810-2','SIDA','2008/08/08'),
    ('19716810-2','Neumonia','2019/12/24'),
    ('19716810-2','Hepatitis A','2017/06/12'),
    ('19716810-2','Paperas','2019/07/06');
