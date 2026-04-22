supermercado = {
    "lacteos" : {
        "leche":1100,
        "yogurt":450,
        "queso":2500
    },
    "verduras": {
      "tomate":1500,
      "lechuga":900,
      "papas":1200  
    },
    "carnes":{
      "pollo":5000,
      "vacuno":9500,
      "cerdo":4500 
    },
    "aseo":{
        "cloro":1300,
        "detergente":7500
        
    }
}

menu = []
carrito_total = 0


print("----  BIENVENIDO ----")

while True:
    print("\n--- PASILLOS DISPONIBLES ---")
    print("1. lacteos\n2. verduras\n3. carnes\n4. articulos_de_aseo\n5. Salir y pagar.")
    
    opcion = input("Que menu desea ingresar? Ingrese numero o '5'/'salir' para pagar: ").lower()
    
    if opcion == 5 or opcion == "salir":
        break
    
    if opcion == 1:
        opcion == "lacteos"
    elif opcion == 2:
        opcion == "verduras"
    elif opcion == 3:
        opcion == "carnes"
    elif opcion == 4:
        opcion == "aseo"
        
    if opcion in supermercado:
        
        while True:
            print (f"---- ESTAS EN EL PASILLO: {opcion.upper()} -----")
            producto_pasillo = supermercado[opcion]
            
            for prodd, precio in producto_pasillo.items():
                print(f"- {prodd.capitalize()} : ${precio}")
                
                producto = input ("\n Seleccione el producto que desea subir a su carrito o tipee 'volver' para volver al menu pincipal: ").lower()
                
                if producto == "volver":
                    break
                
                if producto in producto_pasillo:
                    
                    precio1 = producto_pasillo[producto]
                    
                    menu.append({"nombre": producto, "precio": precio1})
                    
                    carrito_total += precio1
                    
                    print(f"{producto} ha sido añadido al carrito con exito")
                else:
                    print("Producto no encontrado, error 404 not found pa")
    else:
        print("Opcion invalida, ingrese de nuevo.")
    


print("----- BOLETA ELECTRONICA -----")

if not carrito_total:
    print("No se realizaron compras.")
else:
    for item in carrito_total:
        print(f"{item['nombre'].capitalize():<15} ${item['precio']:>5}")

print("-" * 30)
print(f"TOTAL A PAGAR:   ${carrito_total}")
print("="*30)
print("¡Gracias por su compra!")



## A ESTO LE FALTA MEJORAR
