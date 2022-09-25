from manager6 import Manager6
from util import readDWord


class ManagerXY(Manager6):
    def __init__(self):
        Manager6.__init__(self)

    def getOffsets(self):
        self.partyAddress = 0x8ce1cf8
        self.wildAddress = 0x81ff744

        self.initialSeed = None
        self.seedAddress = 0x8c52844
        self.mtStart = 0x8c5284C
        self.mtIndex = 0x8c52848

        self.tinyStart = 0x8c52808

        self.eggReady = 0x8c80124
        self.eggAddress = 0x8c8012c
        self.parent1Address = 0x8c7ff4c
        self.parent2Address = 0x8c8003c

        self.saveVariable = 0x8c6a6a4
