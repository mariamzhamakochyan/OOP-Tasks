class Pets:
    dogs = []
    def __init__(self, dogs):
        self.dogs = dogs

    def count(self):
        print(f"I have {len(my_pets.dogs)} dogs.")
        
    def eat(self):
        hungry = False
        for dog in self.dogs:
            if dog.is_hungry:
                hungry = True
        if hungry:
            print("My dogs are hungry.")
        else:
            print("My dogs are not hungry.")
    
class Dog:
    is_hungry = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} is {self.age} years old")

    def bark(self, sound):
        print(f"{self.name} says {sound}")

    def breed(self, breed):
        print(f"{self.name} is {breed}")
        
    def sit(self):
        print(f"{self.name} is now sitting.")
        
    def stand(self):
        print(f"{self.name}  is now standing")

    def eat(self):
        self.is_hungry = False



class Doberman(Dog):
    def run(self, speed):
        print(f"{self.name} runs {speed}")


Roxy = Dog("Roxy", 5)
Max = Dog("Max", 6)
Roxy.description()
Roxy.bark("'wuf'")
Roxy.breed("Doberman")
Roxy.sit()
Max.stand()
Rocky = Doberman("Rocky", 7)
Rocky.description()
Rocky.run("Fast")

my_dogs = [
    Doberman("Roxy", 7), 
    Dog("Max", 9),
    Doberman("Rocky", 7)
]
my_pets = Pets(my_dogs)
my_pets.count()
my_pets.eat()
