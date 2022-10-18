

from wtforms import Form
from wtforms import SelectField,StringField,EmailField,IntegerField,PasswordField
from wtforms import validators
from datetime import date

year=int(date.today().year)


class Acceso(Form):
    nombre=StringField("Nombre:",
    [ validators.data_required()])
    """
    ,[
        validators.length(min=5,max=10)
    ])"""
    contra_usuario=PasswordField("Contraseña:",
    [ validators.data_required()])
    """,[
        validators.length(min=6,max=20)
    ])"""

class AltaUsuario(Form):
    nombre=StringField("Nombre:",
    [
        validators.length(min=2,max=20),
        validators.data_required()  
    ])
    contra_usuario=PasswordField("Contraseña:",
    [
        validators.length(min=2,max=20),
        validators.data_required()
    ])


    turno = SelectField('Turno:', 
        [ 
            validators.data_required()
        ],
    
        choices=[('A', 'Turno A'), ('B', 'Turno B'), \
        ('C', 'Tunro C'),('D', 'Turno D'), ('E', 'Turno E')])

    correo=EmailField("E-mail:",
    [
        validators.length(min=3,max=40)
          
    ])
    
class Datos(Form):
    from datetime import time
    yearActual=year=date.today().year
    electedYears=[]


    year=SelectField("Año:",
        [
        validators.NumberRange(min=2022,max=3000),
        validators.data_required()
        ],
        
        choices=[(str(i),str(i)) for i in range(yearActual,yearActual+10)])
       
    turno = SelectField('Turno:',
        [validators.data_required()],
        choices=[('','Elige un Turno'),('A', 'Turno A'), ('B', 'Turno B'), \
        ('C', 'Tunro C'),('D', 'Turno D'), ('E', 'Turno E')])                                                

    #ejemplo de Lista desplegable
    #lenguaje = SelectField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])