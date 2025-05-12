#modulo para las funciones para llamar a las funciones para la conexion de la base de datos

import sqlite3



class gestCasino:
    def __init__(self, db_name='DataBase_Casino.db'):
            self.conexion = sqlite3.connect(db_name)
            self.cur = self.conexion.cursor()

    def conexionYcreacion(self, db_name='DataBase_Casino.db'):
        self.conexion = sqlite3.connect(db_name)
        

    def registro_usu(self,dni,nombre,apellidos,edad,saldo):
        self.cur.execute(''' INSERT INTO USUARIOS (DNI,NOMBRE,APELLIDOS,EDAD,SALDO) 
                        VALUES(?,?,?,?,?)''',(dni,nombre,apellidos,edad,saldo))
        self.conexion.commit()
        print('Usuario Registro Exitosamente')

    def ingreso_saldo(self,dinero,dni):
        self.cur.execute(''' UPDATE USUARIOS SET SALDO = SALDO + ? WHERE DNI = ?''', (dinero, dni))
        self.conexion.commit()
        print('Saldo Ingresado Correctamente')

    def retiro_saldo(self,dinero,dni):
        self.cur.execute('UPDATE USUARIOS SET SALDO = SALDO - ? WHERE DNI= ?',(dinero,dni))
        self.conexion.commit()
        print('Retiro exitodo')
    
    def revision_datos(self,dni_reg,nombre):
        self.cur.execute('SELECT DNI,NOMBRE FROM USUARIOS WHERE DNI = ? AND NOMBRE = ?',(dni_reg,nombre))
        resultado= self.cur.fetchall()

        if resultado and resultado[0][0] == dni_reg and resultado[0][1] == nombre:
            return True
        else:
            return False
    def dispo_saldo(self,dni_reg):
        self.cur.execute('SELECT SALDO FROM USUARIOS WHERE DNI = ?', (dni_reg,))

        saldo= self.cur.fetchone()
        return saldo[0] if saldo else 0
    def actualizar_saldo(self,dni_reg,saldo_registro):
        self.cur.execute('UPDATE USUARIOS SET SALDO = ? WHERE DNI = ?',(saldo_registro,dni_reg)) 
        self.conexion.commit()
    def cerrarconexion(self):
        self.conexion.close()
    def borrado(self):
        self.cur.execute('DROP TABLE IF EXISTS USUARIOS')
        self.conexion.commit()
        tabla_usuarios= ('''CREATE TABLE USUARIOS(
                         DNI VARCHAR(9) PRIMARY KEY,
                         NOMBRE VARCHAR(20) NOT NULL,
                         APELLIDOS VARCHAR(40) NOT NULL, 
                         EDAD INT(3) NOT NULL,
                         SALDO REAL)''')
        self.cur.execute(tabla_usuarios)
        self.conexion.commit()

