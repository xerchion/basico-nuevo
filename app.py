
from flask import Flask,render_template

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

#Creamos el index de la app, utilizando templates, en html desde la carpteta templates
@calendario.route("/", methods=["POST","GET"])
def index():
    print("estoy en la app")
    return render_template("index.html")



if __name__=="__main__":
    calendario.run(debug=True)




    


