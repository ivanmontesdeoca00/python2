"""Ejercicio de cajero automatico en este ejercicio vamos a aplicar todos los conocimientos de clases, poo, metodos y constructores crearemos una clase cajero con los siguientes metodos:

constructor: que reciba el saldo inicial
depositar: que reciba la cantidad a depositar
retirar: que reciba la cantidad a retirar
consultar_saldo: que muestre el saldo actual
menu: que muestre un menu con las opciones de depositar, retirar y consultar saldo
salir: que muestre un mensaje de despedida """


class Cajero:
    def __init__ (self, saldo_inicial):
        self.saldo = saldo_inicial
        print(f" --- BIENVENIDOS AL CAJERO AUTOMATICO REY ---")
        print(f"Cuenta activada con un saldo de : ${self.saldo}")
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"deposito exitoso, has sumado ${cantidad}")
        else:
            print("Error: La cantidad a depositar debe ser mayor a 0.")
            
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f"Saldo insuficiente. Tu saldo actual es de ${self.saldo}.")
        elif cantidad <= 0:
            print(f"Error: Cantidad no valida.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso, tu saldo actual es ${cantidad}")
    
    def consultar_saldo(self):
        print(f"\n>>> Saldo disponible: ${self.saldo}")
        
    def salir(self):
        print("Gracias por usar nuestro cajero, no vuelvas mas xd")
    
    def menu(self):
        opcion = 0
        while opcion != 4:
            print("\n--- MENU DE OPCIONES")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Salir")

            try:
                opcion = int(input("Seleccione una opcion: "))
                if opcion == 1:
                    self.consultar_saldo()
                elif opcion == 2:
                    monto = float(input("Monto a depositar: "))
                    self.depositar(monto)
                elif opcion == 3:
                    monto = float(input("Monto a retirar: "))
                    self.retirar(monto)
                elif opcion == 4:
                    self.salir()
                else:
                    print("Opción no válida, intente de nuevo.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
                
mi_cajero = Cajero(1000)
mi_cajero.menu()