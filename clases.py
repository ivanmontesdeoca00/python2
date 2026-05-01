class Ivan:
    def __init__(self, edad, altura, signoZodiacal):
        self.edad = edad
        self.altura = altura
        self.signoZodiacal = signoZodiacal
    def descripcion(self):
        return (f"Hola, soy Ivan y tengo {self.edad} años, mido actualmente {self.altura} metros y soy de mi signo {self.signoZodiacal} porque naci el 12 de enero del 2000.")

presentacion = Ivan("26", "1,66", "capricornio")
print(presentacion.descripcion)