from manager7 import Manager7


class ManagerSM(Manager7):
    def __init__(self):
        Manager7.__init__(self)

    def getOffsets(self):
        self.partyAddress = 0x34195e10
        self.wildAddress = 0x3002f7b8
        self.sosAddress = 0x3002f7b8

        self.seedAddress = 0x325a3878
        self.sfmtStart = 0x33195b88
        self.sfmtIndex = 0x33196548

        self.sosSeedAddress = 0x30038c44
        self.sosSFMTStart = 0x30038c44
        self.sosSFMTIndex = 0x30039604
        self.sosChainLength = 0x3003960d

        self.eggReady = 0x3313edd8
        self.eggAddress = 0x3313eddc
        self.parent1Address = 0x3313ec01
        self.parent2Address = 0x3313ecea
