import sys
import json
from os import path
from PySide6 import QtCore, QtWidgets, QtGui

from lib import lib
from core import settings
from core import dialog
from splats import defaultsplat
from splats import humansplat

# errors
# AGG1 couldn't add array to grid in a group because the grid doesn't have as many elements as needed to add in a group
# SI1 settings file corrupted
# RDS1 attempted to remove default splat which is not possible
# DSD1 attempted to access default splat toggle

# LabeledTextBox array              label           box
# LabeledCheckBox array             label           checkbox
# grid  array                       gridlayout      columnsint     nextopenslotint  rowcount
# outline array of arrays           array1
# array1                            each grouped set of char details



class SplatManager:
    def makeSettingsChecks(self):
        checks = []
        for k in range(len(self.splats)):
            checks = self.splats[k].makeCheck(checks)

        return checks

    def pullSplatData(self):
        data = {"name": ""}
        for k in range(len(self.splats)):
            data = self.splats[k].pullSplatData(data)
        return data

    def pushSplatData(self, path):
        with open(path) as f:
            data = json.load(f)
            for k in range(len(self.splats)):
                self.splats[k].pushSplatData(data)
        self.positionSplats()

    def addAllSplats(self):
        for k in range(len(self.splats)):
            self.splats[k].addSplat()

    def removeAllSplats(self):
        for k in range(len(self.splats)):
            self.splats[k].removeSplat()

    def positionSettingsChecks(self, checks):
        self.parent.widgetLib.addArraystoGridIndividualGroups(checks, self.parent.settingsClass.splatsSettingsLayout)

    def positionSplats(self):
        self.parent.charDetailsGrid[2] = 0
        self.parent.charDetailsGrid[3] = 0

        self.parent.attributesCatGrid[2] = 0
        self.parent.attributesCatGrid[3] = 0

        self.parent.attributesTitleGrid[2] = 0
        self.parent.attributesTitleGrid[3] = 0

        self.parent.attributesGrid[2] = 0
        self.parent.attributesGrid[3] = 0

        self.parent.otherTraitsGrid[2] = 0
        self.parent.otherTraitsGrid[3] = 0

        self.parent.skillsGrid[2] = 0
        self.parent.skillsGrid[3] = 0

        outline = [[], [], [], [], []]
        for k in range(len(self.splats)):
            outline = self.splats[k].positionSplatElements(outline)

        for k in range(len(outline[0])):
            self.parent.widgetLib.addArraystoGridGroupGroups(outline[0][k], self.parent.charDetailsGrid)

        self.parent.widgetLib.addArraystoGridIndividual([self.parent.widgetLib.makeBlankLabel(), self.parent.attributesTitle, self.parent.widgetLib.makeBlankLabel()], self.parent.attributesTitleGrid)

        for k in range(len(outline[1])):
            self.parent.widgetLib.addArraystoGridGroupGroups(outline[1][k], self.parent.attributesGrid)

        self.parent.widgetLib.addArraystoGridIndividual([self.parent.widgetLib.makeBlankLabel(), self.parent.skillsTitle, self.parent.widgetLib.makeBlankLabel()], self.parent.skillsGrid)

        for k in range(len(outline[2])):
            self.parent.widgetLib.addArraystoGridIndividual(outline[2][k], self.parent.skillsGrid)

        for k in range(len(outline[3])):
            self.parent.widgetLib.addArraystoGridIndividual(outline[3][k], self.parent.skillsGrid)

        for k in range(len(outline[4])):
            self.parent.widgetLib.addArraystoGridIndividual(outline[4][k], self.parent.skillsGrid)

    def __init__(self, parent):
        self.parent = parent

        self.splats = [defaultsplat.DefaultClass(self.parent), humansplat.HumanClass(self.parent)]



class ScrollableWindowWithMenu(QtWidgets.QMainWindow):
    def settingsdef(self):
        self.parent.settingsClass.makeWindow()

    def makeMenu(self):
        self.saveAction = QtGui.QAction('&Save')
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.setStatusTip('Save Character')
        self.saveAction.triggered.connect(self.saveload.save)

        self.saveAsAction = QtGui.QAction('&Save As')
        self.saveAsAction.setShortcut('Ctrl+Shift+S')
        self.saveAsAction.setStatusTip('Save Character As...')
        self.saveAsAction.triggered.connect(self.saveload.saveas)

        self.loadAction = QtGui.QAction('&Open')
        self.loadAction.setShortcut('Ctrl+O')
        self.loadAction.setStatusTip('Open Character')
        self.loadAction.triggered.connect(self.saveload.open)

        self.quitAction = QtGui.QAction('&Quit')
        self.quitAction.setShortcut('Ctrl+Q')
        self.quitAction.setStatusTip('Quit')
        self.quitAction.triggered.connect(QtWidgets.QApplication.instance().quit)

        self.settingsAction = QtGui.QAction('&Settings')
        self.settingsAction.setShortcut('Ctrl+I')
        self.settingsAction.setStatusTip('Settings')
        self.settingsAction.triggered.connect(self.settingsdef)

        self.menubar = QtWidgets.QMenuBar()
        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.saveAsAction)
        self.fileMenu.addAction(self.loadAction)
        self.fileMenu.addAction(self.quitAction)
        self.settingsMenu = self.menubar.addMenu('&Settings')
        self.settingsMenu.addAction(self.settingsAction)
        self.baseLayout[0].addWidget(self.menubar, 0, 0)

    def makeScrollBar(self):
        self.scroll = QtWidgets.QScrollArea()

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.baseWidget)

        self.setCentralWidget(self.scroll)

    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.widgetLib = self.parent.widgetLib
        self.saveload = self.widgetLib.saveLoad

        self.baseWidget = QtWidgets.QWidget()
        self.baseLayout = [QtWidgets.QGridLayout(), 1, 0, 1]
        self.baseWidget.setLayout(self.baseLayout[0])

        self.makeScrollBar()
        self.makeMenu()



class CharEditorClass:
    def charDetails(self):
        self.charDetailsGrid = self.widgetLib.MakeGrid(6)

        self.attributesCatGrid = self.widgetLib.MakeGrid(1)
        self.attributesTitleGrid = self.widgetLib.MakeGrid(3)
        self.attributesTitle = self.widgetLib.makeLabel("Attributes")
        self.attributesTitle.setFont(self.titlefont)
        self.attributesGrid = self.widgetLib.MakeGrid(7)
        self.otherTraitsGrid = self.widgetLib.MakeGrid(3)
        self.skillsGrid = self.widgetLib.MakeGrid(3)

        for k in range(len(self.splatManager.splats)):
            if self.settingsdict['splats'][k] == True:
                self.splatManager.splats[k].addSplat()

        self.splatManager.positionSplats()

    def settingsInit(self):
        if path.exists('settings.json'):
            with open('settings.json') as f:
                self.settingsdict = json.load(f)
            if self.settingsdict['settingsVersion'] < 0:
                print("error code: SI1")
        else:
            self.settingsdict = {'settingsVersion': 0}
            self.settingsdict['splats'] = [True, True]
            with open('settings.json', 'w') as f:
                json.dump(self.settingsdict, f)

    def __init__(self):
        self.settingsInit()

        self.titlefont = QtGui.QFont()
        self.titlefont.setFamily("stcaiyun")  # Set Font
        self.titlefont.setBold(True)  # Bold
        self.titlefont.setPointSize(20)  # Set font size

        self.subtitlefont = QtGui.QFont()
        self.subtitlefont.setFamily("stcaiyun")  # Set Font
        self.subtitlefont.setBold(True)  # Bold
        self.subtitlefont.setPointSize(12)  # Set font size

        self.widgetLib = lib.WidgetLibrary(self)

        self.settingsClass = settings.SettingsClass(self)

        self.app = QtWidgets.QApplication(sys.argv)
        self.mainWindow = ScrollableWindowWithMenu(self)

        self.splatManager = SplatManager(self)

        self.savepath = ""

        self.mainWindow.setGeometry(300, 75, 1024, 768)
        self.mainWindow.setWindowTitle('Chronicles of Darkness Interactive Character Sheet')
        self.mainWindow.show()

        self.mainWindow.baseLayout[0].setContentsMargins(0,0,0,0)

        self.charDetails()

        self.widgetLib.addGridtoLayout(self.charDetailsGrid[0], self.mainWindow.baseLayout)

        self.widgetLib.addGridtoLayout(self.attributesCatGrid[0], self.mainWindow.baseLayout)
        self.widgetLib.addGridtoLayout(self.attributesTitleGrid[0], self.attributesCatGrid)
        self.widgetLib.addGridtoLayout(self.attributesGrid[0], self.attributesCatGrid)

        self.widgetLib.addGridtoLayout(self.otherTraitsGrid[0], self.mainWindow.baseLayout)
        self.widgetLib.addGridtoLayout(self.skillsGrid[0], self.otherTraitsGrid)

        self.splatManager.positionSplats()

        if path.exists('quicksave.json'):
            with open('quicksave.json') as f:
                data = json.load(f)

            if data['quicksave'] == True:
                dlg = dialog.CustomDialog()
                if dlg.exec():
                    self.splatManager.pushSplatData('quicksave.json')

        sys.exit(self.app.exec())

charEditor = CharEditorClass()
