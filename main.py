# funciones: escoger area, decidir si quiere mas turnos, finalizar programa
import numeros

def inicio():
    
    eleccion_menu= 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,5):
        print("-"*170)
        
        print("Elija el área a la que se quiere dirigir:")
        print('''

        [1] - Perfumería
        [2] - Farmacia
        [3] - Cosméticos
        [4] - Salir
              
        ''')
        eleccion_menu= input("Número: ")
    return int(eleccion_menu)

def otro_turno():
    turno_diferente = "x" 
    while turno_diferente.lower() != "t":
        turno_diferente= input("\nPresione T si quiere sacar otro turno o si quiere salir: ")


generadorP = numeros.turno_perfumeria()
generadorF= numeros.turno_farmacia()
generadorC = numeros.turno_cosmeticos()

finalizar= False

while finalizar is False:
    menu= inicio()

    if menu== 1:
        numeros.decorar_turnos(generadorP)
        next(generadorP)
        otro_turno()

    if menu== 2:
        numeros.decorar_turnos(generadorF)
        next(generadorF)
        otro_turno()

    if menu== 3:
        numeros.decorar_turnos(generadorC)
        next(generadorC)
        otro_turno()

    if menu== 4:
        print("¡Nos Vemos!")
        finalizar= True
