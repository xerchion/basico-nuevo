
from flask import Flask,render_template,session,request

from datetime import date
import calendarioReal
import Usuarios
import gestionBD
import time
import formularios


calendario=Flask(__name__)
usuario=Usuarios.Usuario()
turno=""
year=date.today().year

colores={"A":"bg-success", "B":"bg-primary", "C":"bg-danger" ,"D":"bg-warning" ,"E":"bg-warning bg-opacity-50" }
coloresdias={"N": "bg-secondary","T":"bg-warning" ,"M":"bg-info" } #Mañana tarde noche
nombreUsuarioActivo="Invitado"
calendario.secret_key = b'eadbfd1f49d6d770ff5cad200d212c74c8f17389df36f7179210af1f9f481741'

#Creamos el index de la app, utilizando templates, en html desde la carpteta templates
@calendario.route("/", methods=["POST","GET"])
def index():
    if 'message' in session:
        print("hay mensajes", session)
    print(session)

    turno=usuario.turno
    nombreUsuario=usuario.nombre

    datosCalendario=formularios.Datos(request.form)

    if request.method=='POST': #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        print("Soy index y llega por post")
    else:
        print("llega por otra cosa",year,turno,nombreUsuarioActivo)

        
   
    if 'username' in session:
        nombreUsuario=session["username"]
        turno=usuario.turno
    else:
        nombreUsuario="Invitado"
        usuario.nombre="Invitado"
        turno=usuario.turno
#para la prueba

    

#   activa este return para las pruebas
    #return render_template("pruebas.html",formulario=datosCalendario,year=2022)
# fin de prueba
    return render_template("index.html")
# ruta de pruebas


if __name__=="__main__":
    calendario.run(debug=True)




    


