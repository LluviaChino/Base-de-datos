#CRUD acciones básicas de crear, leer, actualizar y eliminar datos en una base de datos.
# Conexión o creación de una DB
import sqlite3
Conexion = sqlite3.connect('DataBaseInformatica.db')
cursorDB = Conexion.cursor()    
class ClassCRUD:
    # Constructor
    def __init__(self, NameTable):
        self.NameTable=NameTable   
        #self.CreateElement=CreateElement
    
    # Definir funcion (Metodo) para verificar si existe tabla o para crearla
    def CreateTable(Self):
        # Funciones SQLITE3 Realizar una consulta.
        cursorDB.execute('''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{}' '''.format(Self.NameTable))
        # Evaluar cuantas tablas a contado en la base de datos ELSE crear tabla
        if cursorDB.fetchone()[0]==1:
            return True
        else:
            #Crear tabla con tres valores CODIGO, NOMBRE , DATA1, DATA2, DATA3, DATA4
            cursorDB.execute('''CREATE TABLE {} (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT, DATA1, DATA2, DATA3, DATA4 ) '''.format(Self.NameTable))
            return False
    
    # Crear Insertar
    # Definir función para agrega elementos de la tabla
    def CreateData(self,nombre, data1, data2, data3, data4):
        #Insertar Valores en la tabla (?,?)
        cursorDB.execute('''INSERT INTO {} (NOMBRE, DATA1, DATA2, DATA3, DATA4) VALUES (?,?,?,?,?) '''.format(self.NameTable), (nombre, data1, data2, data3, data4))
        # Realizar Los cambios
        Conexion.commit()
    
    # Definir función selecionar y mostrar
    def ReadData(self):
        # Seleccione toda la tabla *
        cursorDB.execute(''' SELECT * FROM {} '''.format(self.NameTable))
        # Devolver en formato Lista
        lista = []
        # por cada fila encontrada en la consulta del cursor agrege a lista
        for filaencontrada in cursorDB.fetchall():
            lista.append(filaencontrada)
        return lista
    
    #Definir Función de actualización 
    def UpdateData(self,codigo, diccionario):
        ValoresValidos = ['NOMBRE', 'MATRICULA', 'DATA1', 'DATA2', 'DATA3', 'DATA4']
        # Por cada Key del valor de diccionario 
        for key in diccionario.keys():
            #si no hay filas 
            if key not in ValoresValidos:
                #Mostrar Exepción
                raise Exception('No existe la columna')
            else:
                # Realizar la modificacion de los datos (query)
                query = '''UPDATE {} SET {} = '{}' WHERE CODIGO = {} ''' .format(self.NameTable, key, diccionario[key], codigo)
                #Ejecutar 
                cursorDB.execute(query)
        #Establecer cambio 
        Conexion.commit()
    
    #DELET BORRAR 
    def DeleteData(self,codigo):
        cursorDB.execute(''' DELETE FROM {} WHERE CODIGO = {} ''' .format(self.NameTable, codigo))
        Conexion.commit()
 
#Tabla1=ClassCRUD("PROFESORES")
#Tabla2=ClassCRUD("ALUMNOS")


#Tabla1.CreateTable()
#Tabla2.CreateTable()

#Tabla1.CreateData('Juan Perez', 10, 10, 10, 10)
#Tabla1.CreateData('Juan Sanchez', 10, 10, 10, 10)
#Tabla2.CreateData('Juan Perez', 10, 10, 10, 10)

#print(Tabla1.ReadData())

#Tabla1.UpdateData(1,{'NOMBRE':'Panfilo','DATA1':1,'DATA2':2,'DATA3':3,'DATA4':4})
#Tabla1.DeleteData(1)

    


 