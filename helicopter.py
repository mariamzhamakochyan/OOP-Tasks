class Helicopter:
    speed = 0
    started = False
    def __init__(self,manufacturer, name, year, price):
        self.manufacturer = manufacturer
        self.name = name
        self.year = year
        self.price = price

    def start(self):
        self.started = True
        print("Helicopter started, we are flying!")

    def increase_speed(self, speed_):
        if self.started:
            self.speed = self.speed + speed_
            print('swish/swash/swish/swash.')
        else:
            print("You need to start the Helicopter first")

    def stop(self):
        self.speed = 0
        print('Take off')
    
    def showDescription(self):
        print(f"Manufacturer: {self.manufacturer} \nHelicopter name: {self.name} \nIntroduction:  {self.year} \nPrice: {self.price}")
        
        
h = Helicopter("Bell Helicopter","2018", "Bell 429", "$6,975,000")
h.showDescription()
h.increase_speed(10)
h.start()
h.increase_speed(40)
h.stop()
