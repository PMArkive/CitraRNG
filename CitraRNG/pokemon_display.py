from PySide6.QtWidgets import QWidget

from pokemon import Pokemon
from ui_PokemonDisplay import Ui_PokemonDisplay
from util import colorIV, colorPSV


class PokemonDisplay(QWidget, Ui_PokemonDisplay):
    def __init__(self, parent=None):
        super(PokemonDisplay, self).__init__(parent)
        self.setupUi(self)

    def updateInformation(self, pkm: Pokemon):
        self.labelSpeciesValue.setText(pkm.species())
        self.labelGenderValue.setText(pkm.gender())
        self.labelNatureValue.setText(pkm.nature())
        self.labelAbilityValue.setText(pkm.ability())
        self.labelItemValue.setText(pkm.heldItem())
        self.labelSVValue.setText(f"PSV/TSV: {colorPSV(pkm.PSV(), pkm.TSV())}/{pkm.TSV()}")
        self.labelHiddenPowerValue.setText(pkm.hiddenPower())
        self.labelFriendshipValue.setText(str(pkm.currentFriendship()))

        self.labelHP.setText(f"HP: {pkm.HPCurrent()}/{pkm.HP()}")
        self.labelAtk.setText(f"Atk: {pkm.Atk()}")
        self.labelDef.setText(f"Def: {pkm.Def()}")
        self.labelSpA.setText(f"SpA: {pkm.SpA()}")
        self.labelSpD.setText(f"SpD: {pkm.SpD()}")
        self.labelSpe.setText(f"Spe: {pkm.Spe()}")
        self.labelHPIV.setText(f"IV: {colorIV(pkm.IVHP())}")
        self.labelAtkIV.setText(f"IV: {colorIV(pkm.IVAtk())}")
        self.labelDefIV.setText(f"IV: {colorIV(pkm.IVDef())}")
        self.labelSpAIV.setText(f"IV: {colorIV(pkm.IVSpA())}")
        self.labelSpDIV.setText(f"IV: {colorIV(pkm.IVSpD())}")
        self.labelSpeIV.setText(f"IV: {colorIV(pkm.IVSpe())}")
        self.labelHPEV.setText(f"EV: {pkm.EVHP()}")
        self.labelAtkEV.setText(f"EV: {pkm.EVAtk()}")
        self.labelDefEV.setText(f"EV: {pkm.EVDef()}")
        self.labelSpAEV.setText(f"EV: {pkm.EVSpA()}")
        self.labelSpDEV.setText(f"EV: {pkm.EVSpD()}")
        self.labelSpeEV.setText(f"EV: {pkm.EVSpe()}")

        self.labelMove1Name.setText(pkm.move1())
        self.labelMove2Name.setText(pkm.move2())
        self.labelMove3Name.setText(pkm.move3())
        self.labelMove4Name.setText(pkm.move4())
        self.labelMove1PP.setText(f"PP: {pkm.move1PP()}")
        self.labelMove2PP.setText(f"PP: {pkm.move2PP()}")
        self.labelMove3PP.setText(f"PP: {pkm.move3PP()}")
        self.labelMove4PP.setText(f"PP: {pkm.move4PP()}")

    def setTitle(self, name: str):
        self.groupBoxPokemon.setTitle(name)
