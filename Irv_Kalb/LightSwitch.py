class LightSwitch:
    def __init__(self):
        self.on = False
    def TurnOn(self):
        self.on = True
        print('Switch is on')
    def TurnOff(self):
        self.on = False
        print('Switch is off')
L = LightSwitch()
L.TurnOn()
L.TurnOff()
