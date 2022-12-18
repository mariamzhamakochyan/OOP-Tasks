class Dog:
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

dog1 = Dog("Roxy", 7)
dog2 = Dog("Max", 5)
dog1.description()
dog1.bark("'wuf'")
dog1.breed("Dobermann")
dog1.sit()
dog2.stand()
