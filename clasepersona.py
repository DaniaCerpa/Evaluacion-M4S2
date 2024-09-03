class Persona:
    """Clase representativa a Personas.
       Sus atributos son:
       Nombre, Apellido, Sexo, Edad, Estatura y Peso.
       Se establece un metodo __str__ para representar las caracteristicas de la persona a traves de una cadena.
       Se establecen metodos get y set para conseguir y modificar respectivamente cada atributo. 
    """
    def __init__(self, nombre: str, apellido: str, sexo: str, edad: int, estatura: float, peso:float) -> None:
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} de sexo {self.sexo}, tiene una edad de {self.edad} años, mide {self.estatura} mts y pesa {self.peso} kg."

    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_sexo(self):
        return self.sexo
    
    def get_edad(self):
        return self.edad
    
    def get_estatura(self):
        return self.estatura

    def get_peso(self):
        return self.peso
    
    def set_nombre(self, nombre:str):
        self.nombre = nombre.capitalize()
        
    def set_apellido(self, apellido:str):
        self.apellido = apellido.capitalize()
    
    def set_sexo(self, sexo:str):
        self.sexo = sexo
        
    def set_edad(self, edad:int):
        self.edad = edad
        
    def set_estatura(self, estatura:float):
        self.estatura = estatura    
    
    def set_peso(self, peso:float):
        self.peso = peso
    

#Creación de objetos de clase Personas con sus respectivos atributos
persona_1 = Persona("pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "camargo", "Masculino", 18, 1.8, 75)
print(persona_1)
print(persona_2)



#Modificacion de los atributos edad y apellido con metodo set.
persona_1.set_edad(21)
persona_2.set_apellido("santiago")

print()
print("Ciertos datos han sido modificados. La informacion actualizada es:")
print()

print(persona_1)
print(persona_2)