class CajeroAutomatico:
    def mostrar_saldo(self, cliente):
        print(f"\n--- Consulta de Saldo ---")
        print(f"Cliente: {cliente.nombre}")
        print(f"Saldo disponible: ${cliente.saldo}")

    def realizar_retiro(self, cliente):
        print(f"\n--- Retiro de Efectivo ---")
        
        # 1. Solicitar monto
        try:
            monto = float(input("Ingrese el monto a retirar: "))
        except ValueError:
            print("Error: Ingrese un número válido.")
            return

        # 2. Validar saldo disponible
        if monto > cliente.saldo:
            print("Operación rechazada: Saldo insuficiente.")
            return

        # 3. Pedir contraseña (crucial)
        password_input = input("Ingrese su contraseña para confirmar: ")
        
        if cliente.verificar_password(password_input):
            cliente.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${cliente.saldo}")
        else:
            print("Error: Contraseña incorrecta. Operación cancelada.")