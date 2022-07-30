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
        if self.parent.charDetailsSpacer[0] > 0:
            self.parent.widgetLib.deleteArray(self.parent.charDetailsSpacer[1], self.parent.charDetailsGrid)

        for k in range(len(self.parent.blankingGrids)):
            self.parent.blankingGrids[k][2] = 0
            self.parent.blankingGrids[k][3] = 0

        self.parent.widgetLib.addElementtoGrid(self.parent.title, self.parent.titleGrid)
        self.parent.widgetLib.addGridtoLayout(self.parent.titleGrid[0], self.parent.mainWindow.baseLayout)

        outline = [{}, [0, []], [], [[], [], []], [[], []]]
        for k in range(len(self.splats)):
            outline = self.splats[k].positionSplatElements(outline)

        self.parent.title.setPixmap(QtGui.QPixmap.fromImage(outline[0]['default']))

        self.parent.widgetLib.addGridtoLayout(self.parent.charDetailsGrid[0], self.parent.mainWindow.baseLayout)

        chardetailsr = outline[1][0] % 3

        for k in range(len(outline[1][1])):
            if chardetailsr == 0:
                self.parent.charDetailsSpacer = [0, []]
            elif (len(outline[1][1]) - k) == 2 and chardetailsr == 2:
                self.parent.charDetailsSpacer = [1, [self.parent.widgetLib.makeBlankLabel()]]
                self.parent.widgetLib.addArraystoGridIndividual(self.parent.charDetailsSpacer[1], self.parent.charDetailsGrid)
            elif (len(outline[1][1]) - k) == 1 and chardetailsr == 1:
                self.parent.charDetailsSpacer = [2, [self.parent.widgetLib.makeBlankLabel(), self.parent.widgetLib.makeBlankLabel()]]
                self.parent.widgetLib.addArraystoGridIndividual(self.parent.charDetailsSpacer[1], self.parent.charDetailsGrid)
            self.parent.widgetLib.addArraystoGridGroupGroups(outline[1][1][k], self.parent.charDetailsGrid)


        self.parent.widgetLib.addGridtoLayout(self.parent.attributesCatGrid[0], self.parent.mainWindow.baseLayout)
        self.parent.widgetLib.addGridtoLayout(self.parent.attributesTitleGrid[0], self.parent.attributesCatGrid)
        self.parent.widgetLib.addGridtoLayout(self.parent.attributesGrid[0], self.parent.attributesCatGrid)

        self.parent.widgetLib.addArraystoGridIndividual([self.parent.attributesTitle], self.parent.attributesTitleGrid)

        # self.parent.attributeSubGrids = []

        for j in range(3):
            for k in range(4):
                if k == 0:
                    self.parent.widgetLib.addElementtoGrid(outline[2][j][k], self.parent.attributesGrid)
                else:
                    # if self.parent.settingsdict["boxesordots"] == 'boxes':
                    # self.parent.attributeSubGrids = self.parent.attributeSubGrids + [self.parent.widgetLib.MakeGrid(2)]
                    self.parent.widgetLib.addGridtoLayout(outline[2][j][k].grid, self.parent.attributesGrid)
                    # self.parent.widgetLib.addArraystoGridGroupGroups(outline[2][j][k], self.parent.attributeSubGrids[k - 1])
                    # elif self.parent.settingsdict["boxesordots"] == 'dots':
                    #     self.parent.attributeSubGrids = self.parent.attributeSubGrids + [self.parent.widgetLib.MakeGrid(self.parent.settingsdict['boxesordotscount'] + 1)]
                    #     self.parent.widgetLib.addGridtoLayout(self.parent.attributeSubGrids[k - 1][0], self.parent.attributesGrid)
                    #     self.parent.widgetLib.addElementtoGrid(outline[2][j][k][0], self.parent.attributeSubGrids[k - 1])
                    #     self.parent.widgetLib.addArraystoGridGroup(outline[2][j][k][1], self.parent.attributeSubGrids[k - 1])

        # for k in range(len(outline[2]) - 1):
        #     self.parent.widgetLib.addArraystoGridGroupGroups(outline[2][k + 1], self.parent.attributesGrid)


        self.parent.widgetLib.addGridtoLayout(self.parent.miscGrid[0], self.parent.mainWindow.baseLayout)
        self.parent.widgetLib.addGridtoLayout(self.parent.skillsGrid[0], self.parent.miscGrid)
        self.parent.widgetLib.addElementtoGrid(self.parent.skillsTitle, self.parent.skillsGrid)
        self.parent.widgetLib.addElementtoGrid(self.parent.otherTitle, self.parent.middleColumn)
        self.parent.widgetLib.addElementtoGrid(self.parent.traitsTitle, self.parent.rightColumn)

        self.parent.widgetLib.addElementtoGrid(outline[3][0][0], self.parent.skillsGrid)
        self.parent.widgetLib.addElementtoGrid(outline[3][0][1], self.parent.skillsGrid)
        self.parent.widgetLib.addElementtoGrid(outline[3][0][2], self.parent.skillsGrid)
        self.parent.widgetLib.addGridtoLayout(self.parent.skillsMentalGrid[0], self.parent.skillsGrid)
        for k in range(len(outline[3][0]) - 3):
            self.parent.widgetLib.addGridtoLayout(outline[3][0][k + 3].grid, self.parent.skillsMentalGrid)

        self.parent.widgetLib.addElementtoGrid(outline[3][1][0], self.parent.skillsGrid)
        self.parent.widgetLib.addElementtoGrid(outline[3][1][1], self.parent.skillsGrid)
        self.parent.widgetLib.addElementtoGrid(outline[3][1][2], self.parent.skillsGrid)
        self.parent.widgetLib.addGridtoLayout(self.parent.skillsPhysicalGrid[0], self.parent.skillsGrid)
        for k in range(len(outline[3][1]) - 3):
            self.parent.widgetLib.addGridtoLayout(outline[3][1][k + 3].grid, self.parent.skillsPhysicalGrid)

        self.parent.widgetLib.addElementtoGrid(outline[3][2][0], self.parent.skillsGrid)
        self.parent.widgetLib.addElementtoGrid(outline[3][2][1], self.parent.skillsGrid)
        self.parent.widgetLib.addElementtoGrid(outline[3][2][2], self.parent.skillsGrid)
        self.parent.widgetLib.addGridtoLayout(self.parent.skillsSocialGrid[0], self.parent.skillsGrid)
        for k in range(len(outline[3][2]) - 3):
            self.parent.widgetLib.addGridtoLayout(outline[3][2][k + 3].grid, self.parent.skillsSocialGrid)


        self.parent.widgetLib.addGridtoLayout(self.parent.middleColumn[0], self.parent.miscGrid)
        self.parent.widgetLib.addGridtoLayout(self.parent.rightColumn[0], self.parent.miscGrid)


        self.parent.widgetLib.addGridtoLayout(self.parent.meritsTitleGrid[0], self.parent.middleColumn)
        self.parent.widgetLib.addElementtoGrid(self.parent.meritsTitle, self.parent.meritsTitleGrid)
        self.parent.widgetLib.addGridtoLayout(self.parent.meritsGrid[0], self.parent.meritsTitleGrid)

        for k in range(self.parent.settingsdict['meritcount']):
            self.parent.widgetLib.addArraystoGridGroup(self.parent.meritsArray[k], self.parent.meritsGrid)


        self.parent.widgetLib.addGridtoLayout(self.parent.healthGrid[0], self.parent.rightColumn)
        self.parent.widgetLib.addElementtoGrid(self.parent.healthTitle, self.parent.healthGrid)
        self.parent.widgetLib.addGridtoLayout(self.parent.healthBoxesGrid[0], self.parent.healthGrid)

        for k in range(self.parent.settingsdict['healthboxescount']):
            self.parent.widgetLib.addElementtoGrid(self.parent.healthBoxesArray[k][0], self.parent.healthBoxesGrid)

        for k in range(self.parent.settingsdict['healthboxescount']):
            self.parent.widgetLib.addElementtoGrid(self.parent.healthBoxesArray[k][1].getButton(), self.parent.healthBoxesGrid)

        self.parent.widgetLib.addGridtoLayout(self.parent.willpowerGrid[0], self.parent.rightColumn)
        self.parent.widgetLib.addElementtoGrid(self.parent.willpowerTitle, self.parent.willpowerGrid)
        self.parent.widgetLib.addGridtoLayout(self.parent.willpowerBoxesGrid[0], self.parent.willpowerGrid)

        for k in range(self.parent.settingsdict['willpowerboxescount']):
            self.parent.widgetLib.addElementtoGrid(self.parent.willpowerBoxesArray[k][0], self.parent.willpowerBoxesGrid)

        for k in range(self.parent.settingsdict['willpowerboxescount']):
            self.parent.widgetLib.addElementtoGrid(self.parent.willpowerBoxesArray[k][1], self.parent.willpowerBoxesGrid)

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
        self.blankingGrids = []
        self.BODs = []
        self.titleGrid = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.titleGrid]

        self.charDetailsGrid = self.widgetLib.MakeGrid(6)
        self.blankingGrids = self.blankingGrids + [self.charDetailsGrid]
        self.charDetailsSpacer = [0]

        self.attributesCatGrid = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.attributesCatGrid]
        self.attributesTitleGrid = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.attributesTitleGrid]
        self.attributesTitle = self.widgetLib.makeTitle("Attributes")
        self.attributesTitle.setFont(self.titlefont)
        self.attributesGrid = self.widgetLib.MakeGrid(4)
        self.blankingGrids = self.blankingGrids + [self.attributesGrid]

        self.miscGrid = self.widgetLib.MakeGrid(3)
        self.blankingGrids = self.blankingGrids + [self.miscGrid]
        self.skillsGrid = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.skillsGrid]
        self.skillsMentalGrid = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.skillsMentalGrid]
        self.skillsPhysicalGrid = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.skillsPhysicalGrid]
        self.skillsSocialGrid = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.skillsSocialGrid]
        self.otherTitle = self.widgetLib.makeTitle("Other")
        self.otherTitle.setFont(self.titlefont)
        self.traitsTitle = self.widgetLib.makeTitle("Traits")
        self.traitsTitle.setFont(self.titlefont)

        self.middleColumn = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.middleColumn]
        self.rightColumn = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.rightColumn]

        self.meritsTitleGrid = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.meritsTitleGrid]
        self.meritsTitle = self.widgetLib.makeTitle("Merits")
        self.meritsTitle.setFont(self.subtitlefont)
        self.meritsGrid = self.widgetLib.MakeGrid(2)
        self.blankingGrids = self.blankingGrids + [self.meritsGrid]

        self.meritsArray = []
        self.healthBoxesArray = []

        self.healthGrid = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.healthGrid]
        self.healthTitle = self.widgetLib.makeTitle("Health")
        self.healthTitle.setFont(self.subtitlefont)
        self.healthBoxesGrid = self.widgetLib.MakeGrid(self.settingsdict['healthboxescount'])
        self.blankingGrids = self.blankingGrids + [self.healthBoxesGrid]

        self.willpowerBoxesArray = []

        self.willpowerGrid = self.widgetLib.MakeGrid(1)
        self.blankingGrids = self.blankingGrids + [self.willpowerGrid]
        self.willpowerTitle = self.widgetLib.makeTitle("Willpower")
        self.willpowerTitle.setFont(self.subtitlefont)
        self.willpowerBoxesGrid = self.widgetLib.MakeGrid(self.settingsdict['willpowerboxescount'])
        self.blankingGrids = self.blankingGrids + [self.willpowerBoxesGrid]

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
            self.settingsdict['boxesordots'] = 'dots'
            self.settingsdict['boxesordotscount'] = 5
            self.settingsdict['dotsperrowcount'] = 10
            self.settingsdict['splats'] = [True, True]
            self.settingsdict['meritcount'] = 10
            self.settingsdict['healthboxescount'] = 10
            self.settingsdict['willpowerboxescount'] = 10
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

        self.title = QtWidgets.QLabel()
        self.title.setAlignment(QtGui.Qt.AlignCenter)

        self.splatManager = SplatManager(self)

        self.savepath = ""

        self.mainWindow.setGeometry(300, 75, 1024, 768)
        self.mainWindow.setWindowTitle('Chronicles of Darkness Interactive Character Sheet')
        self.mainWindow.show()

        self.mainWindow.baseLayout[0].setContentsMargins(0,0,0,0)

        self.charDetails()

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
