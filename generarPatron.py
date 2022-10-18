# parametros de entrada:
"""
El año del que queremos el patrón
El turno del que queremos el patrón

Salida---->   el patron de los turnos del año, desde 1-1 de ese año hasta 31-12 de ese año

"""
def generarPatron(year,turno):
    import datetime as dt
    from calendar import isleap

    # Valores globales iniciales
    year_inicial=2022           # este valor será fijo, el inicio del patron es 1-1-2022
    diasInicioCalendario=0              # Esta variable debe ser global, nos dira los dias a sumar
                                        # para en la serie coger desde ese día.
    #turno="C"         # FIXME   El valor de esta variable es meramente temporal, siempre será dada

    # Necesitamos el inicio del turno que nos piden y esto son valores fijos que sumamos a la 
    # variable global, segun el turno asignamos los valores de inicio para 1-1-2022
    year_final=year    # FIXME este sera el año que se le pasara por parametro
    turno=turno.capitalize()
    for anio in range(year_inicial,year_final):
        if isleap(anio):
            diasInicioCalendario=diasInicioCalendario+366
        else:
            diasInicioCalendario=diasInicioCalendario+365
    if turno=="A":
        valorTurnoInicio2022=19+diasInicioCalendario
    elif turno=="B":
        valorTurnoInicio2022=33+diasInicioCalendario
    elif turno=="C":
        valorTurnoInicio2022=12+diasInicioCalendario
    elif turno=="D":
        valorTurnoInicio2022=26+diasInicioCalendario
    elif turno=="E":
        valorTurnoInicio2022=5+diasInicioCalendario


    """-----------------------------------------------------------------    VIEJO   """

    #   Aqui caluclamos los dias totales que hay que sumar desde 1-1-2022 para el año que deseamos
    """---------------------------------------------------------------------------------------"""
    



    #print(diasInicioCalendario)
    #    Todo Aqui caluclamos o generaremos la serie de 40.000 dias sin turno especifico
    """---------------------------------------------------------------------------------------"""

    #vector con las repeticiones por valor
    repeticionValor=[2,2,3,4,3,2,2,5,2,3,2,5]
    #vector con los turnos como valores
    valorTurno=["M","T","N","D","M","T","N","D","M","T","N","D"]
        


    #// TODO seguir aqui ahora creando la serie 
                


        

    patronTurnos=[]
    dias=0
    # Calculo los dias totales para el patrón de turnos
    totalDiasPatron=366+(year_final-year_inicial)*366+100 #Multiplico por 366 para k salgan dias de más.
    while (dias<totalDiasPatron):
        iValor=0
        for iValor in range(len(valorTurno)):
            jRepValor=0
            for jRepValor in range(0,repeticionValor[iValor]):
                patronTurnos.append(valorTurno[iValor])
                
                dias=dias+1

   
    """

    Tienes la serie de turnos en :   patronTurnos
    Tienes el dia de comienzo segun el turno en ... valorTurnoInicio2022 
    Tienes una variable totalDiasPatron que calcula los dias para el patron, para no sobrecargar


    #TODO: sigue con la lista de las variables importantes
    """        
    valorFinal=365
    if isleap(year):
        valorFinal=366
    valorFinal=valorFinal+valorTurnoInicio2022
    patronYearPeticion=patronTurnos[valorTurnoInicio2022:valorFinal]
    return patronYearPeticion
