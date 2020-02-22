
class Person:
    # __name=None 
    _phone=None 
    counter=0
    def __init__(self,name,phone):
        self.__name=name
        self._phone=phone
        Person.counter+=1

    def display(self):
        print(self.__name)
        print(self._phone)
        Person.name="Padma"
        

obj1=Person("Mukesh Kumar",7737713067)
obj2=Person("Padma",9828095055)
obj3=Person("Ganesh",8890732636)
obj1.display()
print(obj1._phone)
print(obj1.__name)
print(Person.counter)