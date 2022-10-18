
from flask import Flask,render_template,session,request,redirect,url_for,flash

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
    return render_template("index.html",formulario=datosCalendario,year=year,turno=turno,colores=colores,nombre=nombreUsuario)

@calendario.route("/anualllamada",methods=["POST","GET"])
def anualllamada(usuario):

    if 'username' in session:
        nombreUsuario=session['username']
        turno=session['turn']
        #if usuario.turno!=turno:
            #print("puede qqqqqqqqqqqqqqqqqqqqqqqqe lleeeeeeeeeeeeeeeegue")
            #pass # no se muy bien que hacer aqui, seria para que no cambie el color
    else:
        nombreUsuario="Invitado"
        turno=""
    mes=1  # FIXME  ESTO VA A SER PARA PROBAR UN MES EN CONCRETO
    calendario=calendarioReal.calendarioReal(int(year),turno)

    return(render_template("calendarioYear.html",cd=coloresdias,colores=colores,year=year,turno=turno,nombre=nombreUsuario,calendario=calendario))


@calendario.route("/anual",methods=["POST","GET"])
def anual():    

    if session: #todo esto es viejo, cambia por username
        nombreUsuario=session['username']

        turno=session['turn']
    else:
        nombreUsuario="Invitado"
        turno=""
    year=request.form['year']
    turno=request.form['turno']

    mes=1  # FIXME  ESTO VA A SER PARA PROBAR UN MES EN CONCRETO
    print(year,turno)
    calendario=calendarioReal.calendarioReal(int(year),turno)

    return(render_template("calendarioYear.html",cd=coloresdias,turno=turno,nombre=nombreUsuario,colores=colores,mes=mes,year=year,calendario=calendario))



@calendario.route("/alta",methods=["POST","GET"])
def alta():
    datos=formularios.AltaUsuario(request.form)
    renderizaAlta=render_template("altaUsuario.html",form=datos,nombre="Invitado")
    if request.method=='POST': #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        print("llega por post, de momento sin datos")
        #validamos
        usuario.nombre=datos.nombre.data
        usuario.contraseña=datos.contra_usuario.data
        usuario.turno=datos.turno.data
        usuario.correo=datos.correo.data
        usuario.colores=""
        if gestionBD.comprobarUsuario(usuario):
            flash("Este usuario y contraseña ya están registrados")
           
            #calendario=calendarioReal.calendarioReal(int(year),usuario.turno)                
            #renderizaAlta=render_template("calendarioYear.html",colores=colores,cd=coloresdias,mes=mes,year=year,nombre=session['username'],turno=session['turn'],calendario=calendario)

        else:
            print("no esta, lo doy de alta")
            
            #TODO aqui tiene que ir el loggin o la llamada al login........ 
            session['username']=usuario.nombre
            session['turn']=usuario.turno
                #Guardamos
            if gestionBD.altaUsuario(usuario):
                print("dado bien de alta")
                    #vamos a pagina de confirmación
                #flash("Usuario dado de alta satisfactoriamente, ahora por favor inicie sesion")

                #renderizaAlta=render_template("usuarioExito.html",usuario=usuario.nombre)
                calendario=calendarioReal.calendarioReal(int(year),usuario.turno)
                renderizaAlta=render_template("calendarioYear.html",cd=coloresdias,colores=colores,mes=mes,year=year,turno=usuario.turno,nombre=usuario.nombre,calendario=calendario)
    else:            
            
            print(usuario.turno,usuario.nombre,"aquiiiiiiiiiiiiiiiiiiiii")
            redirect(request.url)
            #calendario=calendarioReal.calendarioReal(int(year),usuario.turno)

            #renderizaAlta=render_template("calendarioYear.html",cd=coloresdias,colores=colores,mes=mes,year=year,nombre=nombreUsuario,turno=usuario.turno,calendario=calendario)

            
         
    return renderizaAlta

# Las siguientes lineas crean otra página de prueba de calendarioHTML, puedes borrarlo
# con estas lineas activo el debug para no tener que cerrar y abrir el servidor en cada cambio
#que hiciera, de esta manera no hay que hacer ctrl-c para salir del servidor.
# para que funcione no puede ser con "flask run" en la consola, debe ser con "pyton app.py"


#iniciar sesion

@calendario.route('/login', methods=['GET', 'POST'])
def login():
  
    import formularios
    datos=formularios.Acceso(request.form)
    if request.method=='POST' and datos.validate(): #el llamar a validate, parece estar obsoleto, ya lo hace en el formulario
        usuario.nombre=datos.nombre.data
        usuario.contraseña=datos.contra_usuario.data
        if gestionBD.comprobarUsuario(usuario):
            session['username'] = usuario.nombre
            session['turn']=usuario.turno
            

                        #mensaje de introducido bien
            anualllamada(usuario)        
            return anualllamada(usuario)

        else:
            
            flash("El usuario no existe o la contraseña es incorrecta, por favor inténtalo de nuevo")
         
    #else:
        #logout()
    return render_template("iniciarSesion.html",form=datos,nombre=nombreUsuarioActivo,colores=colores)
        





@calendario.route('/logout')
def logout():
    # remove the username from the session if it's there
    if 'username' in session:
        session.pop('username', None)
        
        session.pop('turn', None)

    #print(session['turn'])
    #del session['username']
    usuario.nombre="Invitado"
    usuario.turno=""
    return redirect(url_for('index'))


if __name__=="__main__":
    calendario.run(debug=True)




    


