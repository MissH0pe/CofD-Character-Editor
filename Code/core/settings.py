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
    def positionElementsSettings(self):
        self.widgetLib.addArraystoGridIndividual([self.widgetLib.makeBlankLabel(), self.settingsTitle, self.widgetLib.makeBlankLabel()], self.settingsTitleLayout)
        self.parent.splatManager.positionSettingsChecks(self.checks)

    def basicSettings(self):
        self.settingsTitleLayout = self.widgetLib.MakeGrid(3)
        self.settingsTitle = self.widgetLib.makeLabel("Settings")
        self.settingsTitle.setFont(self.parent.titlefont)
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
        self.widgetLib.addGridtoLayout(self.splatsSettingsLayout[0], self.settingsLayout)

        self.positionElementsSettings()

        self.settings.show()

    def __init__(self, parent):
        self.parent = parent

        self.widgetLib = self.parent.widgetLib
