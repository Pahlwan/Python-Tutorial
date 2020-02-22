class celsius:

    def __init__(self,temerature):
        self.__temperature=temerature

    def to_fahrenheit(self):
        return self.__temperature*1.8 + 32

    def temp_setter(self,temperature):
        print("Setting temerature")
        self.___temperature = temperature
    
    def temp_getter(self):
        print("getting temperature")
        return self.___temperature

    __temperature=property(temp_getter,temp_setter)

#See this weired code
# How this code works 
c1=celsius(45)
c1.name="HariRam"

print(c1.name)