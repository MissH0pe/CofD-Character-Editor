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
    def reloadSettings(self):
        if self.parent.settingsClass.dotsCountSettings[1].text() != "":
            self.widgetLib.saveLoad.quickSave()

            for k in range(len(self.parent.BODs)):
                self.parent.BODs[k] = self.parent.BODs[k].deleteSelf()

            self.parent.settingsdict['boxesordotscount'] = int(self.parent.settingsClass.dotsCountSettings[1].text())

            with open('settings.json', 'w') as f:
                json.dump(self.parent.settingsdict, f)

            self.parent.BODs = []

            self.parent.splatManager.splats[0].addBOD()

            self.parent.splatManager.pushSplatData('quicksave.json')

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

        if self.parent.settingsClass.healthBoxesCountSettings[1].text() != "":
            array = []
            for k in range(len(self.parent.healthBoxesArray)):
                if self.parent.healthBoxesArray[k][0].isChecked():
                    array = array + [[self.parent.healthBoxesArray[k][0].isChecked(), self.parent.healthBoxesArray[k][1].getState()]]

            for k in range(len(self.parent.healthBoxesArray)):
                self.parent.healthBoxesGrid[0].removeWidget(self.parent.healthBoxesArray[k][0])
                self.parent.healthBoxesArray[k][0].deleteLater()
                self.parent.healthBoxesArray[k][0] = None

            for k in range(len(self.parent.healthBoxesArray)):
                self.parent.healthBoxesGrid[0].removeWidget(self.parent.healthBoxesArray[k][1].button)
                self.parent.healthBoxesArray[k][1].button.deleteLater()
                self.parent.healthBoxesArray[k][1].button = None

            self.parent.healthBoxesArray = []

            self.parent.settingsdict['healthboxescount'] = int(self.parent.settingsClass.healthBoxesCountSettings[1].text())

            self.parent.healthBoxesGrid[1] = self.parent.settingsdict['healthboxescount']

            for k in range(self.parent.settingsdict['healthboxescount']):
                self.parent.healthBoxesArray = self.parent.healthBoxesArray + [self.widgetLib.makeCheckBoxQuadCheckBox()]

            with open('settings.json', 'w') as f:
                json.dump(self.parent.settingsdict, f)

            for k in range(self.parent.settingsdict['healthboxescount']):
                if k + 1 <= len(array):
                    self.parent.healthBoxesArray[k][0].setChecked(array[k][0])
                    self.parent.healthBoxesArray[k][1].setState(int(array[k][1]))

        if self.parent.settingsClass.willpowerBoxesCountSettings[1].text() != "":
            array = []
            for k in range(len(self.parent.willpowerBoxesArray)):
                if self.parent.willpowerBoxesArray[k][0].isChecked():
                    array = array + [[self.parent.willpowerBoxesArray[k][0].isChecked(), self.parent.willpowerBoxesArray[k][1].isChecked()]]

            for k in range(len(self.parent.willpowerBoxesArray)):
                self.widgetLib.deleteArray(self.parent.willpowerBoxesArray[k], self.parent.willpowerBoxesGrid)

            self.parent.willpowerBoxesArray = []

            self.parent.settingsdict['willpowerboxescount'] = int(self.parent.settingsClass.willpowerBoxesCountSettings[1].text())

            self.parent.willpowerBoxesGrid[1] = self.parent.settingsdict['willpowerboxescount']

            for k in range(self.parent.settingsdict['willpowerboxescount']):
                self.parent.willpowerBoxesArray = self.parent.willpowerBoxesArray + [[self.widgetLib.makeCheckBox(self.parent.widgetLib.saveLoad.quickSave)[0], self.widgetLib.makeCheckBox(self.parent.widgetLib.saveLoad.quickSave)[0]]]

            with open('settings.json', 'w') as f:
                json.dump(self.parent.settingsdict, f)

            for k in range(self.parent.settingsdict['willpowerboxescount']):
                if k + 1 <= len(array):
                    self.parent.willpowerBoxesArray[k][0].setChecked(array[k][0])
                    self.parent.willpowerBoxesArray[k][1].setChecked(array[k][1])

        self.parent.splatManager.positionSplats()

    def positionElementsSettings(self):
        # self.widgetLib.addArraystoGridIndividual([self.settingsTitle)
        # self.widgetLib.addElementtoGridWithWidth(self.basicSettingsTitle, self.basicSettingsLayout, 6)
        self.widgetLib.addArraystoGridGroup(self.dotsCountSettings, self.basicSettingsLayout)
        self.widgetLib.addArraystoGridGroup(self.dotsPerRowSettings, self.basicSettingsLayout)
        self.widgetLib.addArraystoGridGroup(self.meritCountSettings, self.basicSettingsLayout)
        self.widgetLib.addArraystoGridGroup(self.healthBoxesCountSettings, self.basicSettingsLayout)
        self.widgetLib.addArraystoGridGroup(self.willpowerBoxesCountSettings, self.basicSettingsLayout)
        # self.meritCountSettings[1].setText(self.parent.settingsdict['meritcount'])
        # self.widgetLib.addElementtoGridWithWidth(self.splatsSettingsTitle, self.splatsSettingsLayout, 6)
        self.parent.splatManager.positionSettingsChecks(self.checks)

    def basicSettings(self):
        # self.settingsTitleLayout = self.widgetLib.MakeGrid(3)
        self.settingsTitle = self.widgetLib.makeTitle("Settings")
        self.settingsTitle.setFont(self.parent.titlefont)
        self.basicSettingsTitle = self.widgetLib.makeTitle("Basic Settings")
        self.basicSettingsTitle.setFont(self.parent.subtitlefont)
        self.basicSettingsLayout = self.widgetLib.MakeGrid(6)
        self.dotsCountSettings = self.widgetLib.LabeledTextBox("Number of Dots", window = "settings", text = str(self.parent.settingsdict['boxesordotscount']))
        self.dotsPerRowSettings = self.widgetLib.LabeledTextBox("Dots per Row", window = "settings", text = str(self.parent.settingsdict['dotsperrowcount']))
        self.meritCountSettings = self.widgetLib.LabeledTextBox("Merit Boxes", window = "settings", text = str(self.parent.settingsdict['meritcount']))
        self.healthBoxesCountSettings = self.widgetLib.LabeledTextBox("Health Boxes", window = "settings", text = str(self.parent.settingsdict['healthboxescount']))
        self.willpowerBoxesCountSettings = self.widgetLib.LabeledTextBox("Willpower Boxes", window = "settings", text = str(self.parent.settingsdict['willpowerboxescount']))
        # self.dotsCountSettings[1].setText(str(self.parent.settingsdict['boxesordotscount']))
        # self.dotsPerRowSettings[1].setText(str(self.parent.settingsdict['dotsperrowcount']))
        # self.meritCountSettings[1].setText(str(self.parent.settingsdict['meritcount']))
        # self.healthBoxesCountSettings[1].setText(str(self.parent.settingsdict['healthboxescount']))
        # self.willpowerBoxesCountSettings[1].setText(str(self.parent.settingsdict['willpowerboxescount']))
        self.splatsSettingsTitle = self.widgetLib.makeTitle("Splat Settings")
        self.splatsSettingsTitle.setFont(self.parent.subtitlefont)
        self.splatsSettingsLayout = self.widgetLib.MakeGrid(6)
        self.checks = self.parent.splatManager.makeSettingsChecks()

    def makeWindow(self):
        self.settings = ScrollableWindow()

        self.settings.setGeometry(100, 100, 684, 512)
        self.settings.setWindowTitle('Settings')

        self.settingsLayout = self.widgetLib.MakeGrid(1)
        self.widgetLib.addGridtoLayout(self.settingsLayout[0], [self.settings.baseLayout, 1, 0, 0])
        self.settingsLayout[0].setContentsMargins(0,0,0,0)

        self.basicSettings()

        # self.widgetLib.addGridtoLayout(self.settingsTitleLayout[0], self.settingsLayout)
        self.widgetLib.addElementtoGrid(self.settingsTitle, self.settingsLayout)
        self.widgetLib.addElementtoGrid(self.basicSettingsTitle, self.settingsLayout)
        self.widgetLib.addGridtoLayout(self.basicSettingsLayout[0], self.settingsLayout)
        self.widgetLib.addElementtoGrid(self.splatsSettingsTitle, self.settingsLayout)
        self.widgetLib.addGridtoLayout(self.splatsSettingsLayout[0], self.settingsLayout)

        self.positionElementsSettings()

        self.settings.show()

    def __init__(self, parent):
        self.parent = parent

        self.widgetLib = self.parent.widgetLib
