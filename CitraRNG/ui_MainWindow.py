# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui',
# licensing of 'MainWindow.ui' applies.
#
# Created: Mon Oct  1 19:36:09 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 640)
        MainWindow.setMinimumSize(QtCore.QSize(770, 640))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBoxEggRNG = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBoxEggRNG.sizePolicy().hasHeightForWidth())
        self.groupBoxEggRNG.setSizePolicy(sizePolicy)
        self.groupBoxEggRNG.setObjectName("groupBoxEggRNG")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxEggRNG)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelEggReadyStatus = QtWidgets.QLabel(self.groupBoxEggRNG)
        self.labelEggReadyStatus.setObjectName("labelEggReadyStatus")
        self.gridLayout_4.addWidget(self.labelEggReadyStatus, 0, 1, 1, 1)
        self.labelEggReady = QtWidgets.QLabel(self.groupBoxEggRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelEggReady.sizePolicy().hasHeightForWidth())
        self.labelEggReady.setSizePolicy(sizePolicy)
        self.labelEggReady.setObjectName("labelEggReady")
        self.gridLayout_4.addWidget(self.labelEggReady, 0, 0, 1, 1)
        self.labelEggSeed1 = QtWidgets.QLabel(self.groupBoxEggRNG)
        self.labelEggSeed1.setObjectName("labelEggSeed1")
        self.gridLayout_4.addWidget(self.labelEggSeed1, 2, 0, 1, 1)
        self.labelEggSeed2 = QtWidgets.QLabel(self.groupBoxEggRNG)
        self.labelEggSeed2.setObjectName("labelEggSeed2")
        self.gridLayout_4.addWidget(self.labelEggSeed2, 1, 2, 1, 1)
        self.labelEggSeed0 = QtWidgets.QLabel(self.groupBoxEggRNG)
        self.labelEggSeed0.setObjectName("labelEggSeed0")
        self.gridLayout_4.addWidget(self.labelEggSeed0, 2, 2, 1, 1)
        self.labelEggSeed3 = QtWidgets.QLabel(self.groupBoxEggRNG)
        self.labelEggSeed3.setObjectName("labelEggSeed3")
        self.gridLayout_4.addWidget(self.labelEggSeed3, 1, 0, 1, 1)
        self.lineEditEggSeed3 = QtWidgets.QLineEdit(self.groupBoxEggRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditEggSeed3.sizePolicy().hasHeightForWidth())
        self.lineEditEggSeed3.setSizePolicy(sizePolicy)
        self.lineEditEggSeed3.setMaxLength(8)
        self.lineEditEggSeed3.setReadOnly(True)
        self.lineEditEggSeed3.setObjectName("lineEditEggSeed3")
        self.gridLayout_4.addWidget(self.lineEditEggSeed3, 1, 1, 1, 1)
        self.lineEditEggSeed1 = QtWidgets.QLineEdit(self.groupBoxEggRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditEggSeed1.sizePolicy().hasHeightForWidth())
        self.lineEditEggSeed1.setSizePolicy(sizePolicy)
        self.lineEditEggSeed1.setMaxLength(8)
        self.lineEditEggSeed1.setReadOnly(True)
        self.lineEditEggSeed1.setObjectName("lineEditEggSeed1")
        self.gridLayout_4.addWidget(self.lineEditEggSeed1, 2, 1, 1, 1)
        self.lineEditEggSeed2 = QtWidgets.QLineEdit(self.groupBoxEggRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditEggSeed2.sizePolicy().hasHeightForWidth())
        self.lineEditEggSeed2.setSizePolicy(sizePolicy)
        self.lineEditEggSeed2.setMaxLength(8)
        self.lineEditEggSeed2.setReadOnly(True)
        self.lineEditEggSeed2.setObjectName("lineEditEggSeed2")
        self.gridLayout_4.addWidget(self.lineEditEggSeed2, 1, 3, 1, 1)
        self.lineEditEggSeed0 = QtWidgets.QLineEdit(self.groupBoxEggRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditEggSeed0.sizePolicy().hasHeightForWidth())
        self.lineEditEggSeed0.setSizePolicy(sizePolicy)
        self.lineEditEggSeed0.setMaxLength(8)
        self.lineEditEggSeed0.setReadOnly(True)
        self.lineEditEggSeed0.setObjectName("lineEditEggSeed0")
        self.gridLayout_4.addWidget(self.lineEditEggSeed0, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBoxEggRNG, 2, 1, 1, 1)
        self.groupBoxMainRNG = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBoxMainRNG.sizePolicy().hasHeightForWidth())
        self.groupBoxMainRNG.setSizePolicy(sizePolicy)
        self.groupBoxMainRNG.setObjectName("groupBoxMainRNG")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxMainRNG)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelInitialSeed = QtWidgets.QLabel(self.groupBoxMainRNG)
        self.labelInitialSeed.setObjectName("labelInitialSeed")
        self.gridLayout_3.addWidget(self.labelInitialSeed, 0, 0, 1, 1)
        self.lineEditInitialSeed = QtWidgets.QLineEdit(self.groupBoxMainRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditInitialSeed.sizePolicy().hasHeightForWidth())
        self.lineEditInitialSeed.setSizePolicy(sizePolicy)
        self.lineEditInitialSeed.setMaxLength(8)
        self.lineEditInitialSeed.setReadOnly(True)
        self.lineEditInitialSeed.setObjectName("lineEditInitialSeed")
        self.gridLayout_3.addWidget(self.lineEditInitialSeed, 0, 1, 1, 1)
        self.labelCurrentSeed = QtWidgets.QLabel(self.groupBoxMainRNG)
        self.labelCurrentSeed.setObjectName("labelCurrentSeed")
        self.gridLayout_3.addWidget(self.labelCurrentSeed, 1, 0, 1, 1)
        self.lineEditCurrentSeed = QtWidgets.QLineEdit(self.groupBoxMainRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCurrentSeed.sizePolicy().hasHeightForWidth())
        self.lineEditCurrentSeed.setSizePolicy(sizePolicy)
        self.lineEditCurrentSeed.setMaxLength(16)
        self.lineEditCurrentSeed.setReadOnly(True)
        self.lineEditCurrentSeed.setObjectName("lineEditCurrentSeed")
        self.gridLayout_3.addWidget(self.lineEditCurrentSeed, 1, 1, 1, 1)
        self.labelFrame = QtWidgets.QLabel(self.groupBoxMainRNG)
        self.labelFrame.setObjectName("labelFrame")
        self.gridLayout_3.addWidget(self.labelFrame, 2, 0, 1, 1)
        self.lineEditFrame = QtWidgets.QLineEdit(self.groupBoxMainRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFrame.sizePolicy().hasHeightForWidth())
        self.lineEditFrame.setSizePolicy(sizePolicy)
        self.lineEditFrame.setReadOnly(True)
        self.lineEditFrame.setObjectName("lineEditFrame")
        self.gridLayout_3.addWidget(self.lineEditFrame, 2, 1, 1, 1)
        self.labelSaveTSV = QtWidgets.QLabel(self.groupBoxMainRNG)
        self.labelSaveTSV.setObjectName("labelSaveTSV")
        self.gridLayout_3.addWidget(self.labelSaveTSV, 3, 0, 1, 1)
        self.lineEditTSV = QtWidgets.QLineEdit(self.groupBoxMainRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTSV.sizePolicy().hasHeightForWidth())
        self.lineEditTSV.setSizePolicy(sizePolicy)
        self.lineEditTSV.setMaxLength(4)
        self.lineEditTSV.setReadOnly(True)
        self.lineEditTSV.setObjectName("lineEditTSV")
        self.gridLayout_3.addWidget(self.lineEditTSV, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBoxMainRNG, 1, 1, 1, 1)
        self.groupBoxConnection = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBoxConnection.sizePolicy().hasHeightForWidth())
        self.groupBoxConnection.setSizePolicy(sizePolicy)
        self.groupBoxConnection.setObjectName("groupBoxConnection")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxConnection)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBoxGameSelection = QtWidgets.QComboBox(self.groupBoxConnection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxGameSelection.sizePolicy().hasHeightForWidth())
        self.comboBoxGameSelection.setSizePolicy(sizePolicy)
        self.comboBoxGameSelection.setObjectName("comboBoxGameSelection")
        self.comboBoxGameSelection.addItem("")
        self.comboBoxGameSelection.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxGameSelection, 0, 0, 1, 1)
        self.pushButtonConnect = QtWidgets.QPushButton(self.groupBoxConnection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonConnect.sizePolicy().hasHeightForWidth())
        self.pushButtonConnect.setSizePolicy(sizePolicy)
        self.pushButtonConnect.setObjectName("pushButtonConnect")
        self.gridLayout_2.addWidget(self.pushButtonConnect, 0, 1, 1, 1)
        self.pushButtonDisconnect = QtWidgets.QPushButton(self.groupBoxConnection)
        self.pushButtonDisconnect.setEnabled(False)
        self.pushButtonDisconnect.setObjectName("pushButtonDisconnect")
        self.gridLayout_2.addWidget(self.pushButtonDisconnect, 0, 2, 1, 1)
        self.labelUpdateDelay = QtWidgets.QLabel(self.groupBoxConnection)
        self.labelUpdateDelay.setObjectName("labelUpdateDelay")
        self.gridLayout_2.addWidget(self.labelUpdateDelay, 1, 0, 1, 1)
        self.spinBoxDelay = QtWidgets.QSpinBox(self.groupBoxConnection)
        self.spinBoxDelay.setEnabled(False)
        self.spinBoxDelay.setMinimum(300)
        self.spinBoxDelay.setMaximum(2000)
        self.spinBoxDelay.setProperty("value", 500)
        self.spinBoxDelay.setObjectName("spinBoxDelay")
        self.gridLayout_2.addWidget(self.spinBoxDelay, 1, 1, 1, 1)
        self.labelStatus = QtWidgets.QLabel(self.groupBoxConnection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStatus.sizePolicy().hasHeightForWidth())
        self.labelStatus.setSizePolicy(sizePolicy)
        self.labelStatus.setObjectName("labelStatus")
        self.gridLayout_2.addWidget(self.labelStatus, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBoxConnection, 0, 0, 1, 2)
        self.groupBoxPokemon = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBoxPokemon.sizePolicy().hasHeightForWidth())
        self.groupBoxPokemon.setSizePolicy(sizePolicy)
        self.groupBoxPokemon.setObjectName("groupBoxPokemon")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBoxPokemon)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelSpecies = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpecies.setObjectName("labelSpecies")
        self.gridLayout_5.addWidget(self.labelSpecies, 0, 0, 1, 1)
        self.labelSpeciesValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpeciesValue.setObjectName("labelSpeciesValue")
        self.gridLayout_5.addWidget(self.labelSpeciesValue, 0, 1, 1, 1)
        self.labelGender = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelGender.setObjectName("labelGender")
        self.gridLayout_5.addWidget(self.labelGender, 1, 0, 1, 1)
        self.labelGenderValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelGenderValue.setObjectName("labelGenderValue")
        self.gridLayout_5.addWidget(self.labelGenderValue, 1, 1, 1, 1)
        self.labelNature = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelNature.setObjectName("labelNature")
        self.gridLayout_5.addWidget(self.labelNature, 2, 0, 1, 1)
        self.labelNatureValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelNatureValue.setObjectName("labelNatureValue")
        self.gridLayout_5.addWidget(self.labelNatureValue, 2, 1, 1, 1)
        self.labelAbility = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelAbility.setObjectName("labelAbility")
        self.gridLayout_5.addWidget(self.labelAbility, 3, 0, 1, 1)
        self.labelAbilityValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelAbilityValue.setObjectName("labelAbilityValue")
        self.gridLayout_5.addWidget(self.labelAbilityValue, 3, 1, 1, 1)
        self.labelItem = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelItem.setObjectName("labelItem")
        self.gridLayout_5.addWidget(self.labelItem, 4, 0, 1, 1)
        self.labelItemValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelItemValue.setObjectName("labelItemValue")
        self.gridLayout_5.addWidget(self.labelItemValue, 4, 1, 1, 1)
        self.labelPSV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelPSV.setObjectName("labelPSV")
        self.gridLayout_5.addWidget(self.labelPSV, 5, 0, 1, 1)
        self.labelTSV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelTSV.setObjectName("labelTSV")
        self.gridLayout_5.addWidget(self.labelTSV, 5, 1, 1, 1)
        self.labelHiddenPower = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelHiddenPower.setObjectName("labelHiddenPower")
        self.gridLayout_5.addWidget(self.labelHiddenPower, 6, 0, 1, 1)
        self.labelHiddenPowerValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelHiddenPowerValue.setObjectName("labelHiddenPowerValue")
        self.gridLayout_5.addWidget(self.labelHiddenPowerValue, 6, 1, 1, 1)
        self.labelFriendship = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelFriendship.setObjectName("labelFriendship")
        self.gridLayout_5.addWidget(self.labelFriendship, 7, 0, 1, 1)
        self.labelFriendshipValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelFriendshipValue.setObjectName("labelFriendshipValue")
        self.gridLayout_5.addWidget(self.labelFriendshipValue, 7, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 1, 0, 1, 2)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.labelAtk = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelAtk.setObjectName("labelAtk")
        self.gridLayout_7.addWidget(self.labelAtk, 1, 0, 1, 1)
        self.labelDefEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelDefEV.setObjectName("labelDefEV")
        self.gridLayout_7.addWidget(self.labelDefEV, 2, 2, 1, 1)
        self.labelSpAIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpAIV.setObjectName("labelSpAIV")
        self.gridLayout_7.addWidget(self.labelSpAIV, 3, 1, 1, 1)
        self.labelSpA = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpA.setObjectName("labelSpA")
        self.gridLayout_7.addWidget(self.labelSpA, 3, 0, 1, 1)
        self.labelDefIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelDefIV.setObjectName("labelDefIV")
        self.gridLayout_7.addWidget(self.labelDefIV, 2, 1, 1, 1)
        self.labelHP = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelHP.setObjectName("labelHP")
        self.gridLayout_7.addWidget(self.labelHP, 0, 0, 1, 1)
        self.labelSpAEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpAEV.setObjectName("labelSpAEV")
        self.gridLayout_7.addWidget(self.labelSpAEV, 3, 2, 1, 1)
        self.labelSpD = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpD.setObjectName("labelSpD")
        self.gridLayout_7.addWidget(self.labelSpD, 4, 0, 1, 1)
        self.labelHPIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelHPIV.setObjectName("labelHPIV")
        self.gridLayout_7.addWidget(self.labelHPIV, 0, 1, 1, 1)
        self.labelHPEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelHPEV.setObjectName("labelHPEV")
        self.gridLayout_7.addWidget(self.labelHPEV, 0, 2, 1, 1)
        self.labelAtkEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelAtkEV.setObjectName("labelAtkEV")
        self.gridLayout_7.addWidget(self.labelAtkEV, 1, 2, 1, 1)
        self.labelDef = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelDef.setObjectName("labelDef")
        self.gridLayout_7.addWidget(self.labelDef, 2, 0, 1, 1)
        self.labelAtkIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelAtkIV.setObjectName("labelAtkIV")
        self.gridLayout_7.addWidget(self.labelAtkIV, 1, 1, 1, 1)
        self.labelSpDIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpDIV.setObjectName("labelSpDIV")
        self.gridLayout_7.addWidget(self.labelSpDIV, 4, 1, 1, 1)
        self.labelSpeEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpeEV.setObjectName("labelSpeEV")
        self.gridLayout_7.addWidget(self.labelSpeEV, 5, 2, 1, 1)
        self.labelSpeIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpeIV.setObjectName("labelSpeIV")
        self.gridLayout_7.addWidget(self.labelSpeIV, 5, 1, 1, 1)
        self.labelSpDEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpDEV.setObjectName("labelSpDEV")
        self.gridLayout_7.addWidget(self.labelSpDEV, 4, 2, 1, 1)
        self.labelSpe = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpe.setObjectName("labelSpe")
        self.gridLayout_7.addWidget(self.labelSpe, 5, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 3, 0, 1, 2)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.labelMove1 = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove1.setObjectName("labelMove1")
        self.gridLayout_6.addWidget(self.labelMove1, 0, 0, 1, 1)
        self.labelMove1Name = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove1Name.setObjectName("labelMove1Name")
        self.gridLayout_6.addWidget(self.labelMove1Name, 0, 1, 1, 1)
        self.labelMove1PP = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove1PP.setObjectName("labelMove1PP")
        self.gridLayout_6.addWidget(self.labelMove1PP, 0, 2, 1, 1)
        self.labelMove2 = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove2.setObjectName("labelMove2")
        self.gridLayout_6.addWidget(self.labelMove2, 1, 0, 1, 1)
        self.labelMove2Name = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove2Name.setObjectName("labelMove2Name")
        self.gridLayout_6.addWidget(self.labelMove2Name, 1, 1, 1, 1)
        self.labelMove2PP = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove2PP.setObjectName("labelMove2PP")
        self.gridLayout_6.addWidget(self.labelMove2PP, 1, 2, 1, 1)
        self.labelMove3 = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove3.setObjectName("labelMove3")
        self.gridLayout_6.addWidget(self.labelMove3, 2, 0, 1, 1)
        self.labelMove3Name = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove3Name.setObjectName("labelMove3Name")
        self.gridLayout_6.addWidget(self.labelMove3Name, 2, 1, 1, 1)
        self.labelMove3PP = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove3PP.setObjectName("labelMove3PP")
        self.gridLayout_6.addWidget(self.labelMove3PP, 2, 2, 1, 1)
        self.labelMove4 = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove4.setObjectName("labelMove4")
        self.gridLayout_6.addWidget(self.labelMove4, 3, 0, 1, 1)
        self.labelMove4Name = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove4Name.setObjectName("labelMove4Name")
        self.gridLayout_6.addWidget(self.labelMove4Name, 3, 1, 1, 1)
        self.labelMove4PP = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove4PP.setObjectName("labelMove4PP")
        self.gridLayout_6.addWidget(self.labelMove4PP, 3, 2, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_6, 5, 0, 1, 2)
        self.comboBoxPokemon = QtWidgets.QComboBox(self.groupBoxPokemon)
        self.comboBoxPokemon.setEnabled(False)
        self.comboBoxPokemon.setObjectName("comboBoxPokemon")
        self.comboBoxPokemon.addItem("")
        self.comboBoxPokemon.addItem("")
        self.comboBoxPokemon.addItem("")
        self.comboBoxPokemon.addItem("")
        self.comboBoxPokemon.addItem("")
        self.comboBoxPokemon.addItem("")
        self.comboBoxPokemon.addItem("")
        self.gridLayout_8.addWidget(self.comboBoxPokemon, 0, 0, 1, 1)
        self.pushButtonUpdatePokemon = QtWidgets.QPushButton(self.groupBoxPokemon)
        self.pushButtonUpdatePokemon.setEnabled(False)
        self.pushButtonUpdatePokemon.setObjectName("pushButtonUpdatePokemon")
        self.gridLayout_8.addWidget(self.pushButtonUpdatePokemon, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem1, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxPokemon, 1, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "CitraRNG 1.2.0", None, -1))
        self.groupBoxEggRNG.setTitle(QtWidgets.QApplication.translate("MainWindow", "Egg RNG", None, -1))
        self.labelEggReadyStatus.setText(QtWidgets.QApplication.translate("MainWindow", "No egg yet", None, -1))
        self.labelEggReady.setText(QtWidgets.QApplication.translate("MainWindow", "Egg Ready:", None, -1))
        self.labelEggSeed1.setText(QtWidgets.QApplication.translate("MainWindow", "[1]", None, -1))
        self.labelEggSeed2.setText(QtWidgets.QApplication.translate("MainWindow", "[2]", None, -1))
        self.labelEggSeed0.setText(QtWidgets.QApplication.translate("MainWindow", "[0]", None, -1))
        self.labelEggSeed3.setText(QtWidgets.QApplication.translate("MainWindow", "[3]", None, -1))
        self.groupBoxMainRNG.setTitle(QtWidgets.QApplication.translate("MainWindow", "Main RNG", None, -1))
        self.labelInitialSeed.setText(QtWidgets.QApplication.translate("MainWindow", "Initial Seed:", None, -1))
        self.labelCurrentSeed.setText(QtWidgets.QApplication.translate("MainWindow", "Current Seed:", None, -1))
        self.labelFrame.setText(QtWidgets.QApplication.translate("MainWindow", "Frame:", None, -1))
        self.labelSaveTSV.setText(QtWidgets.QApplication.translate("MainWindow", "TSV:", None, -1))
        self.groupBoxConnection.setTitle(QtWidgets.QApplication.translate("MainWindow", "Connection", None, -1))
        self.comboBoxGameSelection.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Sun/Moon", None, -1))
        self.comboBoxGameSelection.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Ultra Sun/Ultra Moon", None, -1))
        self.pushButtonConnect.setText(QtWidgets.QApplication.translate("MainWindow", "Connect", None, -1))
        self.pushButtonDisconnect.setText(QtWidgets.QApplication.translate("MainWindow", "Disconnect", None, -1))
        self.labelUpdateDelay.setText(QtWidgets.QApplication.translate("MainWindow", "Auto update delay(milliseconds):", None, -1))
        self.labelStatus.setText(QtWidgets.QApplication.translate("MainWindow", "Status: Not Connected", None, -1))
        self.groupBoxPokemon.setTitle(QtWidgets.QApplication.translate("MainWindow", "Pokemon", None, -1))
        self.labelSpecies.setText(QtWidgets.QApplication.translate("MainWindow", "Species:", None, -1))
        self.labelSpeciesValue.setText(QtWidgets.QApplication.translate("MainWindow", "None", None, -1))
        self.labelGender.setText(QtWidgets.QApplication.translate("MainWindow", "Gender:", None, -1))
        self.labelGenderValue.setText(QtWidgets.QApplication.translate("MainWindow", "None", None, -1))
        self.labelNature.setText(QtWidgets.QApplication.translate("MainWindow", "Nature:", None, -1))
        self.labelNatureValue.setText(QtWidgets.QApplication.translate("MainWindow", "Hardy", None, -1))
        self.labelAbility.setText(QtWidgets.QApplication.translate("MainWindow", "Ability:", None, -1))
        self.labelAbilityValue.setText(QtWidgets.QApplication.translate("MainWindow", "None", None, -1))
        self.labelItem.setText(QtWidgets.QApplication.translate("MainWindow", "Item:", None, -1))
        self.labelItemValue.setText(QtWidgets.QApplication.translate("MainWindow", "None", None, -1))
        self.labelPSV.setText(QtWidgets.QApplication.translate("MainWindow", "PSV: 0000", None, -1))
        self.labelTSV.setText(QtWidgets.QApplication.translate("MainWindow", "TSV: 0000", None, -1))
        self.labelHiddenPower.setText(QtWidgets.QApplication.translate("MainWindow", "Hidden Power:", None, -1))
        self.labelHiddenPowerValue.setText(QtWidgets.QApplication.translate("MainWindow", "Fighting", None, -1))
        self.labelFriendship.setText(QtWidgets.QApplication.translate("MainWindow", "Friendship:", None, -1))
        self.labelFriendshipValue.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.labelAtk.setText(QtWidgets.QApplication.translate("MainWindow", "Atk:", None, -1))
        self.labelDefEV.setText(QtWidgets.QApplication.translate("MainWindow", "EV: 0", None, -1))
        self.labelSpAIV.setText(QtWidgets.QApplication.translate("MainWindow", "IV: 0", None, -1))
        self.labelSpA.setText(QtWidgets.QApplication.translate("MainWindow", "SpA:", None, -1))
        self.labelDefIV.setText(QtWidgets.QApplication.translate("MainWindow", "IV: 0", None, -1))
        self.labelHP.setText(QtWidgets.QApplication.translate("MainWindow", "HP:", None, -1))
        self.labelSpAEV.setText(QtWidgets.QApplication.translate("MainWindow", "EV: 0", None, -1))
        self.labelSpD.setText(QtWidgets.QApplication.translate("MainWindow", "SpD:", None, -1))
        self.labelHPIV.setText(QtWidgets.QApplication.translate("MainWindow", "IV: 0", None, -1))
        self.labelHPEV.setText(QtWidgets.QApplication.translate("MainWindow", "EV: 0", None, -1))
        self.labelAtkEV.setText(QtWidgets.QApplication.translate("MainWindow", "EV: 0", None, -1))
        self.labelDef.setText(QtWidgets.QApplication.translate("MainWindow", "Def:", None, -1))
        self.labelAtkIV.setText(QtWidgets.QApplication.translate("MainWindow", "IV: 0", None, -1))
        self.labelSpDIV.setText(QtWidgets.QApplication.translate("MainWindow", "IV: 0", None, -1))
        self.labelSpeEV.setText(QtWidgets.QApplication.translate("MainWindow", "EV: 0", None, -1))
        self.labelSpeIV.setText(QtWidgets.QApplication.translate("MainWindow", "IV: 0", None, -1))
        self.labelSpDEV.setText(QtWidgets.QApplication.translate("MainWindow", "EV: 0", None, -1))
        self.labelSpe.setText(QtWidgets.QApplication.translate("MainWindow", "Spe:", None, -1))
        self.labelMove1.setText(QtWidgets.QApplication.translate("MainWindow", "Move 1:", None, -1))
        self.labelMove1Name.setText(QtWidgets.QApplication.translate("MainWindow", "None", None, -1))
        self.labelMove1PP.setText(QtWidgets.QApplication.translate("MainWindow", "PP: 0", None, -1))
        self.labelMove2.setText(QtWidgets.QApplication.translate("MainWindow", "Move 2:", None, -1))
        self.labelMove2Name.setText(QtWidgets.QApplication.translate("MainWindow", "None", None, -1))
        self.labelMove2PP.setText(QtWidgets.QApplication.translate("MainWindow", "PP: 0", None, -1))
        self.labelMove3.setText(QtWidgets.QApplication.translate("MainWindow", "Move 3:", None, -1))
        self.labelMove3Name.setText(QtWidgets.QApplication.translate("MainWindow", "None", None, -1))
        self.labelMove3PP.setText(QtWidgets.QApplication.translate("MainWindow", "PP: 0", None, -1))
        self.labelMove4.setText(QtWidgets.QApplication.translate("MainWindow", "Move 4:", None, -1))
        self.labelMove4Name.setText(QtWidgets.QApplication.translate("MainWindow", "None", None, -1))
        self.labelMove4PP.setText(QtWidgets.QApplication.translate("MainWindow", "PP: 0", None, -1))
        self.comboBoxPokemon.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Party 1", None, -1))
        self.comboBoxPokemon.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Party 2", None, -1))
        self.comboBoxPokemon.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Party 3", None, -1))
        self.comboBoxPokemon.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Party 4", None, -1))
        self.comboBoxPokemon.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "Party 5", None, -1))
        self.comboBoxPokemon.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "Party 6", None, -1))
        self.comboBoxPokemon.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "Wild", None, -1))
        self.pushButtonUpdatePokemon.setText(QtWidgets.QApplication.translate("MainWindow", "Update", None, -1))
