class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def description(self):
        print(f"{self.name} is {self.age} years old")

    def speak(self, sound):
        print(f"{self.name} says {sound}")
    
    def Breed(self, breed):
        print(f"{self.name} breed is {breed}")
        
    def sit(self):
        print(f"{self.name} is now sitting.")
        
    def stand(self):
        print(f"{self.name}  is now standing")

dog1 = Dog("Lucy", 9)
dog2 = Dog("Max", 5)
dog1.description()
dog1.speak("'wuf'")
dog1.Breed("Pitbul")
dog1.sit()
dog2.stand()
