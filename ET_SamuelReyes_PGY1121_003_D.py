asistentes = list(range(1,101))
entradas = [None]*100
silver = int(50000)
gold = int(80000)
platinum = int(120000)
entra=0
cant=0

def menu():
    print("""
    Bienvenido a creativos.cl!!
    [1] Comprar entradas
    [2] Mostrar ubicaciones disponibles
    [3] Ver listado de asistentes
    [4] Mostrar ganancias totales
    [5] Salir""")



def comprar_entrada(rut:str):
    op=input("""
    ¿Desea comprar entradas?
    [1] Si
    [2] No
    """)
    if op == 1:
        print("Usted ha ingresado la opcion de comprar entradas")
        if op == 2:
            print("Usted sera dirigido al menu principal...")
    while True:
        entra=input("""
        Ingrese el tipo de entrada que desea comprar: 
        [1] silver: 50000
        [2] gold: 80000
        [3] platinum: 120000
        """)
        if entra == "1" == silver:
            break
        elif entra == "2" == gold:
            break
        elif entra == "3" ==platinum:
            break
        cant =int(input("Ingrese la cantidad de entradas que desea:"))
        if cant <1:
            print("La cantidad minima de entradas a comprar es de 1")
        elif cant >3:
            print("La cantidad maxima es de 3 entradas!!")
        for i in range(cant):
            asis=input("Ingrese la ubicacion de la entrada que desea!")
        if asis in asistentes and (len(asis)) == 1 or 2 or 3 and asistentes(int(asis)-1)=="X":
            entradas[(int(asis)-1)]=rut
            print("Compra realizada con exito!!")
            break

def mostrar_disponibilidad():
    for i in range (len(asistentes)):
        if entradas [i] !=None:
            print(f"{i+1} -RUT: {rut}")

def listado_asis():
    if entradas !=None:
        rut.index

def ganancias():
    total=entra*cant


while True:
    menu()
    opcion=input("Ingrese la opcion que desee: ")
    match opcion:
        case"1":
            print(asistentes)
            rut = input ("Introduzca su rut, sin digito verificador, guion ni puntos para hacer la compra")
            if rut <= "12345678":
                print("No ingrese el digito verificador")
            if rut == "-" and ".":
                print("Ingrese rut sin guion ni puntos!!!!")
            comprar_entrada(rut)
        case"2":
            mostrar_disponibilidad()
            pass
        case"3":
            listado_asis()
            pass
        case"4":
            ganancias()
            pass
        case"5":
            from os import system 
            system ("cls")
            break