def operacion(n1, n2, accion):
    if accion == "sumar":
        return n1 + n2
    elif accion == "restar":
        return n1 - n2
    elif accion == "multiplicar":
        return n1 * n2
    else:
        return "Operación no válida"

# --- Parte para interactuar con el usuario ---
# Pedimos los números (convertimos a int porque input devuelve texto)
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
tipo = input("¿Qué desea hacer? (sumar/restar/multiplicar): ")

# Llamamos a la función y guardamos el resultado
resultado = operacion(num1, num2, tipo)

print(f"El resultado es: {resultado}")