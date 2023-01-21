class TV():
    def __init__(self):
        self.IsOn = False
        self.IsMuted = False
        self.ChannelList = [1, 2, 3, 4, 5, 7, 9, 10, 11]
        self.NChannel = len(self.ChannelList)
        self.ChanIndex = 0
        self.VolMin = 0
        self.VolMax = 10
        self.volume = self.VolMax
    def power(self):
        self.IsOn = not self.IsOn
    def volumeUp(self):
        if not self.IsOn:
            return
        if self.IsMuted:
            self.IsMuted = False
        if self.volume < self.VolMax:
            self.volume += 1
    def volumeDown(self):
        if not self.IsOn:
            return
        if self.IsMuted:
            self.IsMuted = False
        if self.volume > self.VolMin:
            self.volume -= 1
    def channelUp(self):
        if not self.IsOn:
            return
        self.ChanIndex += 1
        if self.ChanIndex > self.NChannel:
            self.ChanIndex = 0
    def channelDown(self):
        if not self.IsOn:
            return
        self.ChanIndex -= 1
        if self.ChanIndex < 0:
            self.ChanIndex = self.nNChannel - 1
    def mute(self):
        if not self.IsOn:
            return
        self.IsMuted = not self.IsMuted
    def setChannel(self, NewChannel):
        if NewChannel in self.ChannelList:
            self.ChanIndex = self.ChannelList.index(NewChannel)
    def show(self):
        print()
        print(f'Tv status:')
        if self.IsOn:
            print('     Tv is: On')
            print(f'        Channel is: {self.ChannelList[self.ChanIndex]}')
            if self.IsMuted:
                print(f'    Volume is: {self.volume} (sound is muted)')
            else:
                print(f'        Volume is: {self.volume}')
        else:
            print('     Tv is: Off')
tv = TV()
tv.power()
tv.show()

tv.channelUp()
tv.channelUp()
tv.volumeUp()
tv.volumeUp()
tv.volumeDown()
tv.show()
tv.power()
tv.show()
tv.power()
tv.show()
tv.volumeDown()
tv.mute()
tv.show()
tv.setChannel(11)
        
