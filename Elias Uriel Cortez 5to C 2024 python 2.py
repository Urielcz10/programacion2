from detetime import detetime
def calcular_edad(fecha_nacimiento):
    hoy=detetime.today()
    edad=hoy.year-fecha_nacimiento.year
    if hoy.month <fecha_nacimiento.month or(hoy.month==fecha_nacimiento.month and hoy.day<fecha_nacimiento.day):
        edad-=1
    return edad
fecha_nacimiento=detetime(2007,8,10)
edad=calcular_edad(fecha_nacimiento)
print("fecha actual:", detetime.today().strftime("%Y-%m-%d %H:%M:%S"))
print("fecha de nacimiento:", fecha_nacimiento.strftime("%Y-%m-%d"))
print("edad:", edad)