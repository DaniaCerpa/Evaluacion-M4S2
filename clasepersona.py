class Persona:
    """Clase representativa a Personas.
       Sus atributos son:
       Nombre, Apellido, Sexo, Edad, Estatura y Peso.
       Se establece un metodo __str__ para representar las caracteristicas de la persona a traves de una cadena.
       Se establecen metodos get y set para conseguir y modificar respectivamente cada atributo. 
    """
    def __init__(self, nombre: str, apellido: str, sexo: str, edad: int, estatura: float, peso:float) -> None:
        self.__nombre = nombre.capitalize()
        self.__apellido = apellido.capitalize()
        self.__sexo = sexo
        self.__edad = edad
        self.__estatura = estatura
        self.__peso = peso

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} de sexo {self.sexo}, tiene una edad de {self.edad} años, mide {self.estatura} mts y pesa {self.peso} kg."

    @property
    def get_nombre(self):
        return self.__nombre
    
    @property
    def get_apellido(self):
        return self.__apellido
    
    @property
    def get_sexo(self):
        return self.__sexo
    
    @property
    def get_edad(self):
        return self.__edad
    
    @property
    def get_estatura(self):
        return self.__estatura

    @property
    def get_peso(self):
        return self.__peso
    
    
    @nombre.setter
    def set_nombre(self, nombre:str):
        self.__nombre = nombre.capitalize()
     
    @apellido.setter    
    def set_apellido(self, apellido:str):
        self.__apellido = apellido.capitalize()
    
    @sexo.setter
    def set_sexo(self, sexo:str):
        self.__sexo = sexo
        
    @edad.setter    
    def set_edad(self, edad:int):
        self.__edad = edad
        
    @estarura.setter    
    def set_estatura(self, estatura:float):
        self.__estatura = estatura    
    
    @peso.setter  
    def set_peso(self, peso:float):
        self.__peso = peso
    

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