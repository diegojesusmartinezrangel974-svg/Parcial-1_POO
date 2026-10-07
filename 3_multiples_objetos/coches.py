
#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares (marca, color , modelo, velocidad, potencia, asientos) y von las operaciones de acelerar y frenar 
print("\033c")
class Coches:
    marca=""
    color="Blanco"
    modelo=""
    velocidad= 100 
    potencia= 0
    asientos= 0

    def acelerar(self):
        self.velocidad+=1
        print(f"Ahora la velovidad es: {self.velocidad}")

    def frenar(self):
        self.velocidad-=1
        print(f"Ahora la velovidad es: {self.velocidad}")
        
#Multiples objetos o instancias a partir de una clase
coche1=Coches()   
coche2=Coches()     

print(f"El color del coche 1 es: {coche1.color}")
print(f"El color del coche 2 es: {coche2.color}")

for i in range(1,11):
    coche1.acelerar()