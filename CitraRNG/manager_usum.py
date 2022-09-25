from manager7 import Manager7


class ManagerUSUM(Manager7):
    def __init__(self):
        Manager7.__init__(self)

    def getOffsets(self):
        self.partyAddress = 0x33f7fa44
        self.wildAddress = 0x3002f9a0
        self.sosAddress = 0x3002f9a0

        self.seedAddress = 0x32663bf0
        self.sfmtStart = 0x330d35d8
        self.sfmtIndex = 0x330d3f98

        self.sosSeedAddress = 0x30038E30
        self.sosSFMTStart = 0x30038E30
        self.sosSFMTIndex = 0x300397f0
        self.sosChainLength = 0x300397f9

        self.eggReady = 0x3307b1e8
        self.eggAddress = 0x3307b1ec
        self.parent1Address = 0x3307b011
        self.parent2Address = 0x3307b0fa
