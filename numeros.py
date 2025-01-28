# Este módulo es para los generadores y decoradores.
# RECUERDA USAR EL CODIGO DE LA FUNCION QUE PUSIMOS "MAY" Y "MIN" PARA HACER DECORADORES PARA LOS MENSAJES DE FARMACIA, PERFUMERIA, ETC

def decorar_turnos(turno):
    print("Su turno es:")
    return turno


def turno_perfumeria():
    
    n= 1
    while True:
        print(f"[P-{n}]")
        print("Espere y será atendid(a).")
        n += 1
        yield n


def turno_farmacia():
    
    n= 1
    while True:
        
        print(f"[F-{n}]")
        print("Espere y será atendid(a).")
        n += 1
        yield n


def turno_cosmeticos():
    
    n= 1
    while True:
        
        print(f"[C-{n}]")
        print("Espere y será atendid(a).")
        n += 1
        yield n
