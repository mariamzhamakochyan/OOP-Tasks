class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
    def turnOn(self):
        self.switchIsOn = True
    def turnOff(self):
        self.switchIsOn = False
    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1
    def show(self):
        print(f'Switch is on? {self.switchIsOn}')
        if self.switchIsOn == True:
            print(f'Brightness is: {self.brightness}')
        else:
            print("Switch is off")
D = DimmerSwitch()
D.turnOn()
D.raiseLevel()
D.raiseLevel()
D.raiseLevel()
D.raiseLevel()
D.raiseLevel()
D.show()
D.lowerLevel()
D.lowerLevel()
D.lowerLevel()
D.lowerLevel()
D.show()
D.turnOff()
D.show()
   
           
        
