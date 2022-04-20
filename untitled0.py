#parentclassDOG
class Dog:
    def __init__(self, name,age,needyness): 
        self.name = name
        self.age = age
        self.needyness = needyness 

#Child class  types of dogs inherit name and age
class Minipin(Dog): 
    def __init__(self, name,age, needyness):
         super().__init__(name,age,needyness)

class Dacshund(Dog): 
    def __init__(self, name, age, needyness):
         super().__init__(name, age,needyness)

class Beagle(Dog): 
    def __init__(self, name, age, needyness):
         super().__init__(name,age,needyness)
        
Poochie = Minipin("poochie",5,11)
print(Poochie.name, Poochie.age, Poochie.needyness)
Baby_Buster = Dacshund('Baby Buster',1, 0)
print(Baby_Buster.name, Baby_Buster.age, Baby_Buster.needyness)


