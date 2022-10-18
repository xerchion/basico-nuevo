import sqlite3
import Usuarios

def mostrarUsuarioNombre(nombre):
        
    conect=sqlite3.connect('cal_press.db')  
    cursor=conect.cursor()      
    cursor.execute("SELECT * FROM usuarios WHERE nombre=?",(nombre,))
    result=cursor.fetchone()
    if result:
        print("Usuario especifico, con nombre:",nombre," : ",result)
    else:
        print("El usuario no existe")
    conect.close()        
    return
def comprobarUsuario(usuario):
    """ Entrada: un usuario de tipo Usuario,
    devuelve True si esta en la base de datos, y False si no."""
    conect=sqlite3.connect('cal_press.db')  
    cursor=conect.cursor()      
    cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND contraseña=?",(usuario.nombre,usuario.contraseña))
    result=cursor.fetchone()
    conect.close()
    if result:
        usuario.turno=result[3]
    
        
        return True
    return False

def crearBD():
    conexion=sqlite3.connect('cal_press.db')

    #Creo el cursor, que sirve para hacer consultas o mandatos SQL
    cursor=conexion.cursor()

    #Hago una creación de tabla #TODO ESTO HABRA QUE QUITARLO SINO DA ERROR PK YA ESTA CREADA LA TABLA
    cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios (
        id TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        contraseña TEXT NOT NULL,
        turno TEXT NOT NULL,
        correo TEXT,
        cejemplo TEXT) """)
    # hacer commint
        #importante no olvidar guardar los datos tras un alta o modificación
    conexion.commit()

    # cerrar siempre la conesxion a la bd al terminar.
    conexion.close()
    return
    
def altaUsuario(usuario):
    """ Meter un usuario nuevo en la BBDD
        Devuelve True si todo es correcto y False si el usuario ya estaba en la BBDD"""

    #: Crear la conexión y el cursor

    #Creo la conexion a la tabla
    conect=sqlite3.connect('cal_press.db')
    #Creo el cursor, que sirve para hacer consultas o mandatos SQL
    curs=conect.cursor()

    tupla_datos=(usuario.nombre,usuario.contraseña)

    curs.execute("SELECT * FROM usuarios WHERE nombre=? AND contraseña=?",(tupla_datos))
    result=curs.fetchone()
    if result:
        #El usuario ya existe
        conect.close()
        return False
    print("no hay ningun usuario asin, asi que seguimos")  

    # calcular su nuevo ID, lo hago manual, pero: #TODO busca la manera de contar registros
                                                            #   creo que es con count
    # hacer consulta de un todo
    curs.execute("SELECT * FROM usuarios")
    result=curs.fetchall()
    nuevo_id=str(len(result)+1)
    
    tupla_datos=(nuevo_id,usuario.nombre,usuario.contraseña,usuario.turno,usuario.correo,usuario.colores)
    
    curs.execute("INSERT INTO usuarios VALUES (:id,:nombre,:contraseña,:turno,:correo,:colores)", tupla_datos)
    print("lo hace y sigueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

    # hacer commint
        #importante no olvidar guardar los datos tras un alta o modificación
    conect.commit()

    # cerrar siempre la conesxion a la bd al terminar.
    conect.close()

    return True   # POR DEFECTO, DANDO POR HECHO QUE DA ALGUN ERROR, QUITALO SI NO HACE FALTA


#TODO pasar los usuarios

""" usuPrueba=Usuarios.Usuario()
usuPrueba.id=60
usuPrueba.nombre="Jose"
usuPrueba.contraseña="Abcdff"
usuPrueba.turno="C" """

#Creo la conexion a la tabla

#HASTA AQUI HABRA QUE BORRAR PARA PODER SEGUIR.....
#TODO Alta usuario
    #Introduccion estática, este ya esta en la BBDD
#cursor.execute("INSERT INTO usuarios VALUES ('11','Pedro','vertigo','c')")

#Ahora una introducción dinámica usando variables, en este caso un objeto de la calse Usuarios
# lo que le pasamos como parametros de los datos debe ser una TUPLA..
#datos_alta=(usuPrueba.id,usuPrueba.nombre,usuPrueba.contraseña,usuPrueba.turno)

# PARA DAR DE ALTA HAY 3 FORMAS DE HACERLO

#  FORMA 1
# Esta es una manera de hacerlo, la comento pk no puede meter los mismos datos que la siguiente
#ya que el ID seria el mismo...

#cursor.execute("INSERT INTO usuarios VALUES (?,?,?,?)", datos_alta)

#  FORMA 2
# otra forma de hacer esto sería asi: (en el video dicen que se pasa un diccionario, 
# pero a mi me funciona bien con tupla como en el de arriba)

#cursor.execute("INSERT INTO usuarios VALUES (:id,:nombre,:contraseña,:turno)", datos_alta)

#  FORMA 3
# En esta, seria la opcion de no pasarle todos los campos, y esto se haria asi:
# para ello me he inventado el campo cejemplo y no le he puesto la propiedad NOT NULL

#cursor.execute("INSERT INTO usuarios (id,nombre,contraseña,turno )VALUES (:id,:nombre,:contraseña,:turno)", datos_alta)

#importante no olvidar guardar los datos tras un alta o modificación


def consultaTodos():
    #Creo la conexion a la tabla
    conect=sqlite3.connect('cal_press.db')
    #Creo el cursor, que sirve para hacer consultas o mandatos SQL
    cursor=conect.cursor()
    # hacer consulta de un todo
    cursor.execute("SELECT * FROM usuarios")
    usuario=cursor.fetchall()
    print("todos los usuarios: ",usuario)
    print("Cantidad de usuarios:",len(usuario))

    conect.commit()
    conect.close()

""" 
#TODO hacer busquedas de cosas
#empecemos con el ID
cursor.execute("SELECT * FROM usuarios WHERE id=?",("24",))
usuario=cursor.fetchall()
print("Usuario especifico, con id 24",usuario)

#buscquemos por contraseña
cursor.execute("SELECT * FROM usuarios WHERE contraseña=?",("Abcdff",))
usuario=cursor.fetchall()
#si no existe me devuelve una lista vacia, hagamos la comprobación antes de del print
if usuario:
    print("Usuario especifico, con contraseña Abcdff",usuario)  

#Busqueda de prueba con dos campos
    # Datos de ejemplo, borrar despues
    nombre="Jose"
    conword="Abcdff"
cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND contraseña=?",(nombre,conword))
usuario=cursor.fetchone()
if usuario:
    print("Busqueda de prueba con dos campos",usuario)  
else:
    print("no hay ningun usuario asin")



pedro=Usuarios.Usuario()

pedro.nombre="Alberto"
pedro.contraseña="seguiriri"
pedro.turno="D"
conexion.close()
altaUsuario(pedro)
mostrarUsuarioNombre("Alberto")

# cerrar siempre la conesxion a la bd al terminar.


 """