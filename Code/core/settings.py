import json
from PySide6 import QtCore, QtWidgets, QtGui



class ScrollableWindow(QtWidgets.QMainWindow):
    def makeScrollBar(self):
        self.scroll = QtWidgets.QScrollArea()

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.baseWidget)

        self.setCentralWidget(self.scroll)

    def __init__(self):
        super().__init__()

        self.baseWidget = QtWidgets.QWidget()
        self.baseLayout = QtWidgets.QGridLayout()
        self.baseWidget.setLayout(self.baseLayout)

        self.makeScrollBar()



class SettingsClass:
    def reloadSettings(self): # todo make sure to copy over data from existing merits and add back in if there is enough space
        if self.parent.settingsClass.meritCountSettings[1].text() != "":
            array = []
            for k in range(len(self.parent.meritsArray)):
                if self.parent.meritsArray[k][0].text() != "" or self.parent.meritsArray[k][1].text() != "":
                    array = array + [[self.parent.meritsArray[k][0].text(), self.parent.meritsArray[k][1].text()]]

            for k in range(len(self.parent.meritsArray)):
                self.widgetLib.deleteArray(self.parent.meritsArray[k], self.parent.meritsGrid)

            self.parent.meritsArray = []

            self.parent.settingsdict['meritcount'] = int(self.parent.settingsClass.meritCountSettings[1].text())

            for k in range(self.parent.settingsdict['meritcount']):
                self.parent.meritsArray = self.parent.meritsArray + [self.widgetLib.makeMerit()]

            with open('settings.json', 'w') as f:
                json.dump(self.parent.settingsdict, f)

            for k in range(self.parent.settingsdict['meritcount']):
                if k + 1 <= len(array):
                    self.parent.meritsArray[k][0].setText(array[k][0])
                    self.parent.meritsArray[k][1].setText(array[k][1])

            self.parent.splatManager.positionSplats()
            #
            # self.parent.saveLoad.quickSave()

    def positionElementsSettings(self):
        self.widgetLib.addArraystoGridIndividual([self.widgetLib.makeBlankLabel(), self.settingsTitle, self.widgetLib.makeBlankLabel()], self.settingsTitleLayout)
        self.widgetLib.addElementtoGridWithWidth(self.basicSettingsTitle, self.basicSettingsLayout, 6)
        self.widgetLib.addArraystoGridGroup(self.meritCountSettings, self.basicSettingsLayout)
        # self.meritCountSettings[1].setText(self.parent.settingsdict['meritcount'])
        self.widgetLib.addElementtoGridWithWidth(self.splatsSettingsTitle, self.splatsSettingsLayout, 6)
        self.parent.splatManager.positionSettingsChecks(self.checks)

    def basicSettings(self):
        self.settingsTitleLayout = self.widgetLib.MakeGrid(3)
        self.settingsTitle = self.widgetLib.makeTitle("Settings")
        self.settingsTitle.setFont(self.parent.titlefont)
        self.basicSettingsTitle = self.widgetLib.makeTitle("Basic Settings")
        self.basicSettingsTitle.setFont(self.parent.subtitlefont)
        self.basicSettingsLayout = self.widgetLib.MakeGrid(6)
        self.meritCountSettings = self.widgetLib.LabeledTextBox("Merit Boxes", window = "settings")
        self.splatsSettingsTitle = self.widgetLib.makeTitle("Splat Settings")
        self.splatsSettingsTitle.setFont(self.parent.subtitlefont)
        self.splatsSettingsLayout = self.widgetLib.MakeGrid(6)
        self.checks = self.parent.splatManager.makeSettingsChecks()

    def makeWindow(self):
        self.settings = ScrollableWindow()

        self.settings.setGeometry(400, 150, 384, 512)
        self.settings.setWindowTitle('Settings')

        self.settingsLayout = self.widgetLib.MakeGrid(1)
        self.widgetLib.addGridtoLayout(self.settingsLayout[0], [self.settings.baseLayout, 1, 0, 0])
        self.settingsLayout[0].setContentsMargins(0,0,0,0)

        self.basicSettings()

        self.widgetLib.addGridtoLayout(self.settingsTitleLayout[0], self.settingsLayout)
        self.widgetLib.addGridtoLayout(self.basicSettingsLayout[0], self.settingsLayout)
        self.widgetLib.addGridtoLayout(self.splatsSettingsLayout[0], self.settingsLayout)

        self.positionElementsSettings()

        self.settings.show()

    def __init__(self, parent):
        self.parent = parent

        self.widgetLib = self.parent.widgetLib
