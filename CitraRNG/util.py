import struct

from citra import Citra

def convertByte(data: bytes, start: int):
    return struct.unpack("B", data[start:start+1])[0]

def convertWord(data: bytes, start: int):
    return struct.unpack("<H", data[start:start+2])[0]

def convertDWord(data: bytes, start: int):
    return struct.unpack("<I", data[start:start+4])[0]

def readByte(citra: Citra, address: int):
    data = citra.read_memory(address, 1)
    return convertByte(data, 0)

def readWord(citra: Citra, address: int):
    data = citra.read_memory(address, 2)
    return convertWord(data, 0)

def readDWord(citra: Citra, address: int):
    data = citra.read_memory(address, 4)
    return convertDWord(data, 0)

def hexify(num: int):
    return hex(num)[2:].upper()

def colorIV(iv: int):
    if iv == 30 or iv == 31:
        return "<b><font color ='green'>" + str(iv) + "</font></b>"
    elif iv == 0 or iv == 1:
        return "<b><font color = 'red'>" + str(iv) + "</font></b>"
    else:
        return str(iv)

def colorPSV(psv: int, tsv: int):
    if psv == tsv:
        return "<b><font color ='green'>" + str(psv) + "</font></b>"
    else:
        return str(psv)

def uint(val: int):
    return val & 0xFFFFFFFF
