import Class_CRUD as comm
import math

TablaProfesores= []
TablaAlumnos= []

Profesores=comm.ClassCRUD("PROFESORES")
Alumnos=comm.ClassCRUD("ALUMNOS")


Profesores.CreateTable()
#Profesores.CreateData('X', 10, 0, 10, 10)
#Profesores.CreateData('Y', 10, 10, 10, 10)
#Profesores.CreateData('Z', 10, 10, 10, 10)
#TablaProfesores=Profesores.ReadData()
#print(TablaProfesores)
#Profesores.UpdateData(1,{'NOMBRE':'Panfilo','DATA1':1,'DATA2':2,'DATA3':3,'DATA4':4})
TablaProfesores=Profesores.ReadData()
print(TablaProfesores)
#Profesores.DeleteData(1)
#TablaProfesores=Profesores.ReadData()
#print(TablaProfesores)

Alumnos.CreateTable()
Alumnos.CreateData('A', 10, 10, 10, 10)
Alumnos.CreateData('B', 10, 10, 10, 10)
Alumnos.CreateData('C', 10, 10, 10, 10)
#TablaAlumnos=Alumnos.ReadData()
#print(TablaAlumnos)
#Alumnos.UpdateData(1,{'NOMBRE':'Jhon Smitt','DATA1':1,'DATA2':2,'DATA3':3,'DATA4':4})
TablaAlumnos=Alumnos.ReadData()
#print(TablaAlumnos)
#Alumnos.DeleteData(1)
#TablaAlumnos=Alumnos.ReadData()
#print(TablaAlumnos)

#Introducir Datos
#i=int(input("Introducir fila: "))
#j=int(input("Introducir columna: "))

# 5 Promedio
#Media
MediaProfesores=0.0
# Acumulador
AccProfesores=0.0
#Leer
for Fila in TablaProfesores:
    # Lectura de todos los Data1 Fila[2]
    if Fila[2]!='':
        #Accumulador
        AccProfesores=AccProfesores+float(Fila[2])
MediaProfesores=AccProfesores/len(TablaProfesores)
#5 Identificar Valores Faltantes Media o mediana
for fila in TablaProfesores:
    if fila[2]=='':
        Profesores.UpdateData(int(fila[0]),{'NOMBRE':fila[1],'DATA1':MediaProfesores,'DATA2':float(fila[3]),'DATA3':float(fila[4]),'DATA4':float(fila[5])})
#print(MediaProfesores) Data 1
#Modificar
print('Media',MediaProfesores)

# 2 complete el valor faltante manualmente Data 2
for fila in TablaProfesores:
    if fila[3]=='':
        ValorManual=float(input("Introdusca el valor faltante: "))
        Profesores.UpdateData(int(fila[0]),{'NOMBRE':fila[1],'DATA1':float(fila[2]),'DATA2':ValorManual,'DATA3':float(fila[4]),'DATA4':float(fila[5])})

#1 Eliminar Fila (Tupla) Nombre
for fila in TablaProfesores:
    if fila[1]=='':
        Alumnos.DeleteData(int(fila[0]))
        print('Valor elimidado',fila[0])
        
# 3 Remplazo por etiqueta Codigo
for fila in TablaProfesores:
    if fila[4]=='':
        ValorEtiqueta=999
        Profesores.UpdateData(int(fila[0]),{'NOMBRE':fila[1],'DATA1':float(fila[2]),'DATA2':float(fila[3]),'DATA3':ValorEtiqueta,'DATA4':float(fila[5])})

#Correlacion Lineal
#Sumatoria X Data 3
Sx=0.0
#Sumatoria y Data 4
Sy=0.0
#Sumatoria X2
Sx2=0.0
#Sumatoria XY
Sxy=0.0
# Tamaño de muestra (numero de datos)
n=len(TablaProfesores)
#Leer
for Fila in TablaProfesores:
    # Lectura de todos los Data1 Fila[2]
    if Fila[5]!='':
        #sumatoria x
        Sx=Sx+float(Fila[4])
        Sx2=Sx2+(float(Fila[4])*float(Fila[4]))
        Sy=Sy+float(Fila[5])
        Sxy=Sxy+(float(Fila[4])*float(Fila[5]))
#y=a*x+b  (Data 3=x, Data 4=y)
print('n: ',n)
a=((n*Sxy)-(Sx*Sy))/((n*Sx2)-(Sx*Sx))
print('a: ',a)
b=(Sy-(a*Sx))/n
print('b: ',b)
for fila in TablaProfesores:
    if fila[5]=='':
        y=(a*float(fila[4]))+b
        print('Nuevo y:',y)
        Profesores.UpdateData(int(fila[0]),{'NOMBRE':fila[1],'DATA1':float(fila[2]),'DATA2':float(fila[3]),'DATA3':float(fila[4]),'DATA4':y})
#y=a*x+b  (Data 3=x, Data 4=y)

#DESVIACION ESTANDAR

AccDesviacion = 0.0
for Fila in TablaProfesores:
    if Fila[2]!='':
        AccDesviacion=AccDesviacion+((float(Fila[2])-MediaProfesores)*(float(Fila[2])-MediaProfesores))
S= math.sqrt(AccDesviacion)/(len(TablaProfesores)-1)
print('La desviación estandar es: ', S)

print('Este es un nuevo mensaje 7/03/2025 a las 2:56 pm')