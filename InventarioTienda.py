## Objetivo principal de este ejercicio que hice en 40 minutos, poder fijar las bases de Funciones
## El enunciado fue hacer un sistema de inventario basico para una tienda pequeña. Debia ser interativo y permitir realizar operaciones con los productos
## el sistema puede ver inventario, agregar productos, actualizar stock, eliminar stock y buscar por nombre.
## pato sos un qlo
## saludos atte Ivan :)





def mostrar_menu():
    print("--- SISTEMA DE INVENTARIO DE TIENDA ---")
    print("1- ver inventario")
    print("2- Agregar productos")
    print("3- Actualizar stock de productos")
    print("4- Elimiar productos")
    print("5- buscar producto por nombre")
    print("6- Salir del sistema")
    print("----------------------------------------")

def obtener_flotante_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            print("El valor debe ser mayor o igual a 0.1")
        except ValueError:
            print("Tipeo invalido, por favor anota un numero que sea valido pelotudx")

def obtener_entero_positivo(mensaje):
    while True:
        try:
            valor = int (input(mensaje))
            if valor >= 0:
                return valor
            print("El stock debe ser un numero entero positivo pa")
        except ValueError:
            print("Otra ves, tipeo invalido, porfa manito anota un numero entero positivo")

def ver_inventario(inventario):
    if not inventario:
        print("\nEl Inventario esta vacio mono")
        return

    print("\n--- Inventario de la tienda ---")
    print(f"{'Producto':<20} | {'Precio':<15} | {'Stock':<10}")
    print("-" * 44)
    for nombre, datos in inventario.items():
        print(f"{nombre:<20} | ${datos['precio']:<14.2f} | {datos['stock']:<10}")

def agregar_producto(inventario):
    print("\n --- Agregar nuevo producto ----")
    nombre = input("Ingrese el nuevo producto: ").strip()

    if not nombre:
        print("El nombre no puede estar vacio, sos tontito o que?")
        return
    
    if nombre in inventario:
        print(f"El {nombre} ya existe en el inventario, no seas boludo")
        return
    
    precio = obtener_flotante_positivo("Ingrese el precio del producto: ")
    stock = obtener_entero_positivo("ingresa el stock inicial: ")

    inventario[nombre] = {
        "precio": precio,
        "stock": stock
    }
    print(f"Producto '{nombre}' fue añadido bien.")

def actualizar_stock(inventario):
    print("\n --- Actualizar stcok ---- ")
    if not inventario:
        print("El inventario esta vacio")
        return
    
    nombre = input ("Ingrese el nombre del producto a actualizar: ").strip()
    if nombre not in inventario:
        print(f"El producto '{nombre}' no esta en el inventario")
        return
    
    print(f"Stock actual de {nombre}: {inventario[nombre]['stock']}")

    nuevo_stock = obtener_entero_positivo("Ingrese el nuevo stock: ")

    inventario[nombre]["stock"] = nuevo_stock
    print(f"Stock de {nombre} fue actualizado a {nuevo_stock}")

def eliminar_producto(inventario):
    print("\n ---- Eliminar producto ----")
    if not inventario:
        print("el inventario esta vacio.")
        return
    
    nombre = input("ingrese el nombre del producto a eliminar mono: ").strip()
    if nombre not in inventario:
        print(f"El producto {nombre} no existe en el inventario. ")
        return
    
    confirmacion = input(f"Tas seguro que queres eliminar {nombre}? SI-NO: ").strip().lower()

    if confirmacion == "si":
        del inventario[nombre]
        print(f"Producto '{nombre}' fue eliminado del inventario.")
    else:
        print("operacion cancelada")

def buscar_producto(inventario):
    print("\n --- Buscar producto por nombre ----")
    if not inventario:
        print("Inventario vacio")
        return
    
    nombre = input("Ingrese el nombre del producto que quiere buscar: ").strip()
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"\n[Información del Producto]")
        print(f"Nombre: {nombre}")
        print(f"Precio: ${datos['precio']:.2f}")
        print(f"Stock: {datos['stock']} unidades")
    else:
        print(f"El producto '{nombre}' no fue encontrado en el inventario.")

def iniciar_tienda():
    inventario  = {}

    while True: 
        mostrar_menu()
        opcion = input ("\n Seleccione una opcion del 1 al 6: ").strip()

        if opcion == "1":
            ver_inventario(inventario)
        elif opcion == "2":
            agregar_producto(inventario)
        elif opcion == "3":
            actualizar_stock(inventario)
        elif opcion == "4":
            eliminar_producto(inventario)
        elif opcion == "5":
            buscar_producto(inventario)
        elif opcion == "6":
            print("\n Gracias por usar este sistema, Saliendo en 3....2....1....")
            break
        else:
            print("n\Opcion no valida, ingresa un numero del 1 al 6 papito.")

if __name__ == "__main__":
    iniciar_tienda()