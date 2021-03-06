import time
import threading

from Manager import Manager
from Util import hexify, colorIV, colorPSV
from ui_MainWindow import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSettings, Signal, Slot

class MainWindow(QMainWindow, Ui_MainWindow):
    update = Signal()

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadSettings()
        
        self.pushButtonConnect.clicked.connect(self.connectCitra)
        self.pushButtonDisconnect.clicked.connect(self.disconnectCitra)
        self.pushButtonUpdatePokemon.clicked.connect(self.updatePokemon)
        self.doubleSpinBoxDelay.valueChanged.connect(self.updateDelay)

        self.update.connect(self.updateMainRNG)
        self.update.connect(self.updateEggRNG)

    def closeEvent(self, event):
        self.saveSettings()
        #return super().closeEvent(event)

    def saveSettings(self):
        settings = QSettings()
        settings.setValue("delay", self.doubleSpinBoxDelay.value())

    def loadSettings(self):
        settings = QSettings()
        self.delay = float(settings.value("delay", 0.5))
        self.doubleSpinBoxDelay.setValue(self.delay)

    def connectCitra(self):
        index = self.comboBoxGameSelection.currentIndex()
        self.manager = Manager(index)
        self.allowUpdate = True

        self.toggleEnable(True)
        self.labelStatus.setText("Connected")
        self.pushButtonConnect.setEnabled(False)
        self.pushButtonDisconnect.setEnabled(True)

        t = threading.Thread(target=self.autoUpdate)
        time.sleep(1)
        t.start()

    def disconnectCitra(self):
        self.allowUpdate = False
        self.manager = None

        self.toggleEnable(False)
        self.pushButtonConnect.setEnabled(True)
        self.pushButtonDisconnect.setEnabled(False)

        self.labelStatus.setText("Disconnected")

    def toggleEnable(self, flag):
        self.comboBoxPokemon.setEnabled(flag)
        self.pushButtonUpdatePokemon.setEnabled(flag)
        self.doubleSpinBoxDelay.setEnabled(flag)

    @Slot()
    def updateMainRNG(self):
        values = self.manager.updateFrameCount()

        # Check to see if frame changed at all
        if values[0] == 0:
            return

        self.lineEditInitialSeed.setText(hexify(values[1]))
        self.lineEditCurrentSeed.setText(hexify(values[2]))
        self.lineEditFrame.setText(str(values[3]))
        self.lineEditTSV.setText(str(values[4]))

    def updateEggRNG(self):
        values = self.manager.eggStatus()

        if values[0] == 0:
            self.labelEggReadyStatus.setText("No egg yet")
        else:
            self.labelEggReadyStatus.setText("Egg ready")

        self.lineEditEggSeed3.setText(hexify(values[1]))
        self.lineEditEggSeed2.setText(hexify(values[2]))
        self.lineEditEggSeed1.setText(hexify(values[3]))
        self.lineEditEggSeed0.setText(hexify(values[4]))

    def updatePokemon(self):
        index = self.comboBoxPokemon.currentIndex()

        if index < 6:
            pkm = self.manager.partyPokemon(index)
        else:
            pkm = self.manager.wildPokemon()

        self.labelSpeciesValue.setText(pkm.Species())
        self.labelGenderValue.setText(pkm.Gender())
        self.labelNatureValue.setText(pkm.Nature())
        self.labelAbilityValue.setText(pkm.Ability())
        self.labelItemValue.setText(pkm.HeldItem())
        self.labelPSV.setText("PSV: " + colorPSV(pkm.PSV(), pkm.TSV()))
        self.labelTSV.setText("TSV: " + str(pkm.TSV()))
        self.labelHiddenPowerValue.setText(pkm.HiddenPower())
        self.labelFriendshipValue.setText(str(pkm.CurrentFriendship()))
        
        self.labelHPIV.setText("IV: " + colorIV(pkm.IVHP()))
        self.labelAtkIV.setText("IV: " + colorIV(pkm.IVAtk()))
        self.labelDefIV.setText("IV: " + colorIV(pkm.IVDef()))
        self.labelSpAIV.setText("IV: " + colorIV(pkm.IVSpA()))
        self.labelSpDIV.setText("IV: " + colorIV(pkm.IVSpD()))
        self.labelSpeIV.setText("IV: " + colorIV(pkm.IVSpe()))
        self.labelHPEV.setText("EV: " + str(pkm.EVHP()))
        self.labelAtkEV.setText("EV: " + str(pkm.EVAtk()))
        self.labelDefEV.setText("EV: " + str(pkm.EVDef()))
        self.labelSpAEV.setText("EV: " + str(pkm.EVSpA()))
        self.labelSpDEV.setText("EV: " + str(pkm.EVSpD()))
        self.labelSpeEV.setText("EV: " + str(pkm.EVSpe()))
    
        self.labelMove1Name.setText(pkm.Move1())
        self.labelMove2Name.setText(pkm.Move2())
        self.labelMove3Name.setText(pkm.Move3())
        self.labelMove4Name.setText(pkm.Move4())
        self.labelMove1PP.setText("PP: " + str(pkm.Move1PP()))
        self.labelMove2PP.setText("PP: " + str(pkm.Move2PP()))
        self.labelMove3PP.setText("PP: " + str(pkm.Move3PP()))
        self.labelMove4PP.setText("PP: " + str(pkm.Move4PP()))

    def updateDelay(self):
        val = self.doubleSpinBoxDelay.value()
        self.delay = val

    def autoUpdate(self):
        while self.allowUpdate == True:
            self.update.emit()
            time.sleep(self.delay)