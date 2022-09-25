from manager6 import Manager6
from util import readDWord


class ManagerORAS(Manager6):
    def __init__(self):
        Manager6.__init__(self)

    def getOffsets(self):
        self.partyAddress = 0x8cfb26c
        self.wildAddress = 0x81ffa6c

        self.initialSeed = None
        self.seedAddress = 0x8c59e40
        self.mtStart = 0x8c59e48
        self.mtIndex = 0x8c59e44

        self.tinyStart = 0x8c59e04

        self.eggReady = 0x8c88358
        self.eggAddress = 0x8c88360
        self.parent1Address = 0x8c88180
        self.parent2Address = 0x8c88270

        self.saveVariable = 0x8c71db8
