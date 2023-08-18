import numpy as np
import math


def mensaje_bienvenida():    
    print("╔═══════════════════════════════════╗")
    print("║            Bienvenido a           ║")
    print("║       Calculadora de Sucesiones   ║")
    print("║             Geométricas           ║")
    print("╚═══════════════════════════════════╝")

def caja_bonita(string):
    box_width = max(len(string) + 4, 40)  
    horizontal_border = "═" * box_width
    padding = (box_width - len(string) - 2) // 2  
    empty_line = f"║{' ' * padding}{string}{' ' * padding}  ║"

    print(f"╔{horizontal_border}╗")
    print(empty_line)
    print(f"╚{horizontal_border}╝")

def print_menu():
    print("╔═════════════════════════════════╗")
    print("║           MENÚ PRINCIPAL        ║")
    print("╠═════════════════════════════════╣")
    print("║ 1) Ingresar términos            ║")
    print("║    conocidos                    ║")
    print("║ 2) Salir                        ║")
    print("╚═════════════════════════════════╝")

def print_menu_log():
    print("╔═════════════════════════════════╗")
    print("║    ¿Desea sacar la posición     ║")
    print("║    de algún valor dentro de     ║")
    print("║    la sucesión ?                ║")
    print("╠═════════════════════════════════╣")
    print("║ 1) Sí                           ║")
    print("║ 2) No                           ║")
    print("╚═════════════════════════════════╝")



def ingresoDatos():
    #Creación matriz
    primerN, segundoN = np.zeros(2), np.zeros(2)
    try:

        primerN[0] = int(input("Ingrese la posición de la N del primer valor:\n"))
        if primerN[0]<= 0:
            caja_bonita("Las posiciones de N deben ser enteros positivos.")
            return None

        primerN[1] = float(input(f"Ingrese el valor de a{int(primerN[0])}:\n"))

        segundoN[0] = int(input("Ingrese la posición de la N del segundo valor:\n"))
        if segundoN[0]<= 0:
            caja_bonita("Las posiciones de N deben ser enteros positivos.")
            return None
        segundoN[1] = float(input(f"Ingrese el valor de a{int(segundoN[0])}:\n"))

        

        razon = (segundoN[1] / primerN[1]) ** (1 / (segundoN[0] - primerN[0]))
        a1 = primerN[1] / (razon ** (primerN[0] - 1))

        return razon, a1

    except ValueError:
        caja_bonita("Por favor ingrese valores númericos.")
    except:
        caja_bonita("Por favor revise su input.")

# 2 = 8 ** 1/3

#forma general
# an = a1 * (r ** (n-1))

#a3= a1 * razon ** (3-1)
# 5 = a1 * 4
# 5/4 = a1


def printSucesion(a1,razon):
    try:

        tamano = int(input("Ingrese la cantidad de enes que quiere sacar:\n"))

        if tamano <= 0:
            caja_bonita("Las posiciones de N deben ser enteros positivos.")
            return None

        matriz = np.empty(tamano, dtype=object)

        for x in range(1, tamano + 1):
            resultado = a1 * (razon ** (x - 1))
            matriz[x - 1] = ([x, resultado])

        for lista in matriz:
            caja_bonita(f"n{lista[0]}={lista[1]}")

    except ValueError:
        caja_bonita("Por favor ingrese valores númericos.")
    except:
        caja_bonita("Por favor revise su input.")


def funcionLog(a1,razon):
    try:

        numeroDado = float(input("Ingrese el número del que quiere sacar la n en la sucesión:\n"))

        # base = razon
        # x = numeroDado / primerTermino
        # n = math.log(x,base) + 1

        x = numeroDado / a1

        n = math.log(x, razon) + 1

        if math.isclose(n, round(n), rel_tol=1e-9, abs_tol=1e-9):
            caja_bonita(f"La n de {numeroDado} es {int(round(n))}.")
        else:
            caja_bonita(f"{numeroDado} no pertenece a la secuencia.")

    except ValueError:
        caja_bonita("Por favor ingrese valores númericos.")
    except:
        caja_bonita("Por favor revise su input.")


menu=True
mensaje_bienvenida()
while menu:
    try:
        print_menu()
        eleccion=int(input("Seleccione una opción:\n"))
        match eleccion:
            case 1:
                razon, a1= ingresoDatos()
                printSucesion(a1,razon)
                subMenu=True
                while subMenu:
                    print_menu_log()
                    sacarLog=int(input("Su opción:\n"))
                    match sacarLog:
                        case 1:
                            funcionLog(a1,razon)
                        case 2:
                            subMenu=False
                        case _:
                            caja_bonita("La opción ingresada no es válida.")
            case 2:
                caja_bonita("Gracias por usar este programa. Fernando Belmar 18/08/23.")
                menu = False
            case _:
                caja_bonita("La opción ingresada no es válida.")
    except ValueError:
        caja_bonita("Por favor ingrese valores númericos.")
    except:
        caja_bonita("Por favor revise su input.")
