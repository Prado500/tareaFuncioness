
precioM = 1800000

totalP1 = 0.0

totalP2 = 0.0

totalP3 = 0.0

p1 = " Java de Cero a Senior "

p2 = " Python con IA Aplicada "

p3 = " Mobile Senior con IA "

def autenticarUsuario():
    usuario = input("ingrese el ususario: ")
    if usuario == "root":
        clave = input("Digite su contraseña: ")
        if clave == "1234":
            centroDeLlamado()
        else:
            print("Contraseña incorrecta")
    else:
        print("Usuario no encontrado")

def mostrarMenu():
    print("*" * 10)
    print("/\/\/\/" * 10)
    print("             DEV SENIOR - SISTEMA DE VENTAS")
    print("/\/\/\/" * 10)
    print("*" * 10)
    print("(1.) Mostrar Programas ")
    print("(2.) Vender Programas ")
    print("(3.) Consultar ingresos acumulados por programa ")
    print("(4.) Total general de ingresos del día ")
    print("(5.) Salir del sistema ")
    print("\n")
 
 
 
def mostrarProgramas():
    p1 = " Java de Cero a Senior "
    p2 = " Python con IA Aplicada "
    p3 = " Mobile Senior con IA "
    precio1 = " $ 1.800.000 "
    precio2 = " $ 1.800.000 "
    precio3 = " $ 1.800.000 "
    print("-" * 60)
    print("CATÁLOGO DE LOS 3 PROGRAMAS MAS DEMANDADOS")
    print("-" * 60)
    print(f"Programa {p1} || Valor con Descuento: {precio1}")
    print(f"Programa {p2} || Valor con Descuento: {precio2}")
    print(f"Programa {p3} || Valor con Descuento: {precio3}")
    print("\n")
    
    
def venderProgramas():
    totalPrograma1 = 0.0
    totalPrograma2 = 0.0
    totalPrograma3 = 0.0
    totalPrograma4 = 0.0
    totalPrograma5 = 0.0
    cantidad = 0
    ventaRegistrada = 0.0
    
    mostrarProgramas()
    
    opcion = input("Digite el número del programa al que desea registrar la venta: \n (1) Java de Cero a Senior \n (2) Python con IA Aplicada \n (3) Mobile Senior con IA ")
    if opcion == "1":
        cantidad = int(input("Digite la cantidad de programas 1 a vender: "))                    #como acceder a variables declaradas dentro de otras funciones
        if cantidad > 0:
            global totalP1
            ventaRegistrada = cantidad * precioM
            totalPrograma1 += ventaRegistrada
            totalP1 += totalPrograma1
        else:
            print("La cantidad solo puede ser positiva y mayor a 0")
    elif opcion == "2":
        cantidad = int(input("Digite la cantidad de programas 2 a vender: "))                    #como acceder a variables declaradas dentro de otras funciones
        if cantidad > 0:
            global totalP2
            ventaRegistrada = cantidad * precioM
            totalPrograma2 += ventaRegistrada
            totalP2 += totalPrograma2
        else:
            print("La cantidad solo puede ser positiva y mayor a 0")        
    elif opcion == "3":
        cantidad = int(input("Digite la cantidad de programas 3 a vender: "))                    #como acceder a variables declaradas dentro de otras funciones
        if cantidad > 0:
            global totalP3
            ventaRegistrada = cantidad * precioM
            totalPrograma3 += ventaRegistrada
            totalP3 += totalPrograma3
        else:
            print("La cantidad solo puede ser positiva y mayor a 0")
        
      
    else:
        print("Ha registrado una opción inválida.")
       
    return totalPrograma1, totalPrograma2, totalPrograma3, totalPrograma4, totalPrograma5

def ingresosXPrograma():
    print(f"Los ingresos acululados del programa {p1} son de $ {totalP1}")
    print(f"Los ingresos acululados del programa {p2} son de $ {totalP2}")
    print(f"Los ingresos acululados del programa {p3} son de $ {totalP3}")


def ingresosDia():
    print(f"Los ingrsos del dia son: {totalP1 + totalP2 + totalP3}")

def salir():
    print("Gracias por usar el sistema")
        
def centroDeLlamado(): 
    while True:
        
        mostrarMenu()
        
        opcion = ""
        
        opcion = input("Digite la opción del menú que necesite: ")
        
        if opcion == "1":
            mostrarProgramas()
        
        elif opcion == "2":
            venderProgramas()
        
        elif opcion == "3":
            ingresosXPrograma()
        
        elif opcion == "4":
            ingresosDia()
        
        elif opcion == "5":
            salir()
            break
        
        else:
            print("Opción Inválida. Por favor digite un número del 1 al 5")
    

autenticarUsuario()