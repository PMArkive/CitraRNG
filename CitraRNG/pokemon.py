import lookup
from crypto import decryptArray
from util import convertByte, convertDWord, convertWord


class Pokemon:
    def __init__(self, data: bytes, flag: bool = True):
        if flag:
            self.data = decryptArray(data)
        else:
            self.data = data

    def encryptionConstant(self):
        return convertDWord(self.data, 0x0)

    def speciesNum(self):
        return convertWord(self.data, 0x8)

    def species(self):
        return lookup.species[self.speciesNum()]

    def heldItem(self):
        return lookup.items[convertWord(self.data, 0xA)]

    def TID(self):
        return convertWord(self.data, 0xC)

    def SID(self):
        return convertWord(self.data, 0xE)

    def TSV(self):
        return (self.TID() ^ self.SID()) >> 4

    def ability(self):
        return lookup.abilities[convertByte(self.data, 0x14)]

    def PID(self):
        return convertDWord(self.data, 0x18)

    def PSV(self):
        val = self.PID()
        return ((val >> 16) ^ (val & 0xffff)) >> 4

    def nature(self):
        return lookup.natures[convertByte(self.data, 0x1C)]

    def genderNum(self):
        return (convertByte(self.data, 0x1D) >> 1) & 3

    def gender(self):
        return lookup.genders[self.genderNum()]

    def EVHP(self):
        return convertByte(self.data, 0x1E)

    def EVAtk(self):
        return convertByte(self.data, 0x1F)

    def EVDef(self):
        return convertByte(self.data, 0x20)

    def EVSpA(self):
        return convertByte(self.data, 0x22)

    def EVSpD(self):
        return convertByte(self.data, 0x23)

    def EVSpe(self):
        return convertByte(self.data, 0x21)

    def move1(self):
        return lookup.moves[convertWord(self.data, 0x5A)]

    def move2(self):
        return lookup.moves[convertWord(self.data, 0x5C)]

    def move3(self):
        return lookup.moves[convertWord(self.data, 0x5E)]

    def move4(self):
        return lookup.moves[convertWord(self.data, 0x60)]

    def move1PP(self):
        return convertByte(self.data, 0x62)

    def move2PP(self):
        return convertByte(self.data, 0x63)

    def move3PP(self):
        return convertByte(self.data, 0x64)

    def move4PP(self):
        return convertByte(self.data, 0x65)

    def IV32(self):
        return convertDWord(self.data, 0x74)

    def IVHP(self):
        return self.IV32() & 0x1F

    def IVAtk(self):
        return (self.IV32() >> 5) & 0x1F

    def IVDef(self):
        return (self.IV32() >> 10) & 0x1F

    def IVSpA(self):
        return (self.IV32() >> 20) & 0x1F

    def IVSpD(self):
        return (self.IV32() >> 25) & 0x1F

    def IVSpe(self):
        return (self.IV32() >> 15) & 0x1F

    def hiddenPowerNum(self):
        return int((((self.IVHP() & 1) + (self.IVAtk() & 1) * 2 + (self.IVDef() & 1) * 4 + (self.IVSpe() & 1) * 8 + (self.IVSpA() & 1) * 16 + (self.IVSpD() & 1) * 32) * 15) / 63)

    def hiddenPower(self):
        return lookup.hiddenPowers[self.hiddenPowerNum()]

    def currentHandler(self):
        return convertByte(self.data, 0x93)

    def HTFriendship(self):
        return convertByte(self.data, 0xA2)

    def OTFriendship(self):
        return convertByte(self.data, 0xCA)

    def currentFriendship(self):
        if self.currentHandler() == 0:
            return self.OTFriendship()
        else:
            return self.HTFriendship()

    def level(self):
        return convertByte(self.data, 0xEC)

    def HPCurrent(self):
        return convertWord(self.data, 0xF0)

    def HP(self):
        return convertWord(self.data, 0xF2)

    def Atk(self):
        return convertWord(self.data, 0xF4)

    def Def(self):
        return convertWord(self.data, 0xF6)

    def SpA(self):
        return convertWord(self.data, 0xFA)

    def SpD(self):
        return convertWord(self.data, 0xFC)

    def Spe(self):
        return convertWord(self.data, 0xF8)
