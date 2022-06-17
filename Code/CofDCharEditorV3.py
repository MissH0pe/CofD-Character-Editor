import sys
import json
from os import path
from PySide6 import QtCore, QtWidgets, QtGui

# errors
# AGG1 couldn't add array to grid in a group because the grid doesn't have as many elements as needed to add in a group
# SI1 settings file corrupted

# LabeledTextBox array              label           box
# LabeledCheckBox array             label           checkbox
# grid  array                       gridlayout      columnsint     nextopenslotint  rowcount

class WidgetLibrary:
    def quickSave(self):
        data = self.pullData()
        data["quicksave"] = True
        with open('quicksave.json', 'w') as f:
            json.dump(data, f)

    def pullData(self):
        data = {"name": self.parent.name[1].text(), "player": self.parent.player[1].text(), "chronicle": self.parent.chronicle[1].text(), "concept": self.parent.concept[1].text(), "age": self.parent.age[1].text()}
        #, "strength": self.parent.strength[1].text(), "intelligence": self.parent.intelligence[1].text(), "presence": self.parent.presence[1].text(), "dexterity": self.parent.dexterity[1].text(), "wits": self.parent.wits[1].text(), "manipulation": self.parent.manipulation[1].text(), "stamina": self.parent.stamina[1].text(), "resolve": self.parent.resolve[1].text(), "composure": self.parent.composure[1].text()
        if self.parent.settingsdict['isHuman'] == True:
            data["is human"] = True
            data = data | {"group name": self.parent.groupname[1].text(), "virtue": self.parent.virtue[1].text(), "vice": self.parent.vice[1].text(), "faction": self.parent.faction[1].text()}
        else:
            data["is human"] = False
        return data

    def deleteArray(self, array, grid):
        for k in range(len(array)):
            grid[0].removeWidget(array[k])
            array[k].deleteLater()
            array[k] = None
        return None

    def makeBlankLabel(self):
        label = QtWidgets.QLabel()
        label.setText(" ")
        return label

    def makeLabel(self, text):
        label = QtWidgets.QLabel()
        label.setText(text)
        return label

    def MakeGrid(self, columns):
        return [QtWidgets.QGridLayout(), columns, 0, 0]

    def LabeledTextBox(self, labelName, charsheetbool = True): #pass charsheetbool = False when not using for charsheet
        label = self.makeLabel(labelName + ": ")
        box = QtWidgets.QLineEdit()
        if charsheetbool == True:
            box.textChanged.connect(self.quickSave)
        return [label, box]

    def LabeledCheckBox(self, labelName, checkdef):
        checkbox = QtWidgets.QCheckBox()
        checkbox.clicked.connect(checkdef)
        return [self.makeLabel(labelName + " "), checkbox]

    def areColumnsFull(self, grid):
        if grid[2] == grid[1]:
            grid[2] = 0
            grid[3] = grid[3] + 1
        return grid

    def forLoopWOColumnsCheck(self, element, grid):
        for k in range(len(element)):
            grid[0].addWidget(element[k], grid[3], grid[2])
            grid[2] = grid[2] + 1
        return grid

    def addElementtoGrid(self, element, grid):
        grid[0].addWidget(element, grid[3], grid[2])
        grid[2] = grid[2] + 1
        grid = self.areColumnsFull(grid)

    def addGridtoLayout(self, element, grid):
        grid[0].addLayout(element, grid[3], grid[2])
        grid[2] = grid[2] + 1
        grid = self.areColumnsFull(grid)

    def addArraystoGridGroup(self, element, grid):
        if len(element) <= grid[1]:
            if grid[2] < grid[1] - (len(element) - 1):
                grid = self.forLoopWOColumnsCheck(element, grid)
                grid = self.areColumnsFull(grid)
            else:
                grid[2] = 0
                grid[3] = grid[3] + 1
                grid = self.forLoopWOColumnsCheck(element, grid)
        else:
            print("error code: AGG1")

    def addArraystoGridIndividualGroups(self, element, grid):
        for k in range(len(element)):
            self.addArraystoGridGroup(element[k], grid)
            grid = self.areColumnsFull(grid)

    def addArraystoGridIndividual(self, element, grid):
        for k in range(len(element)):
            grid[0].addWidget(element[k], grid[3], grid[2])
            grid[2] = grid[2] + 1
            grid = self.areColumnsFull(grid)

    def __init__(self, parent):
        self.parent = parent
        # print("Library Loaded")



#https://www.pythonguis.com/tutorials/pyside6-dialogs/
class CustomDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Program Previously Closed Without Saving")

        QBtn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("Would you like to load the quicksave?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)



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



class ScrollableWindowWithMenu(QtWidgets.QMainWindow):
    def saveas(self):
        with open('quicksave.json', 'w') as f:
            json.dump({'quicksave': False}, f)
        data = self.widgetLib.pullData()
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save as', "", "*.json")
        self.parent.savepath = path[0]
        if path[0][-5] + path[0][-4] + path[0][-3] + path[0][-2] + path[0][-1] == ".json":
            with open(self.parent.savepath, 'w') as f:
                json.dump(data, f)
        else:
            self.parent.savepath = self.parent.savepath + ".json"
            with open(self.parent.savepath, 'w') as f:
                json.dump(data, f)

    def save(self):
        if self.parent.savepath == "":
            self.saveas()
        else:
            data = self.widgetLib.pullData()
            with open(self.parent.savepath, 'w') as f:
                json.dump(data, f)
            with open('quicksave.json', 'w') as f:
                json.dump({'quicksave': False}, f)

    def loadData(self, path):
        with open(path) as f:
            data = json.load(f)

            self.parent.name[1].setText(data.get('name'))
            self.parent.player[1].setText(data.get('player'))
            self.parent.chronicle[1].setText(data.get('chronicle'))
            self.parent.concept[1].setText(data.get('concept'))
            self.parent.age[1].setText(data.get('age'))
            # self.strength[1].setText(data.get('strength'))
            # self.intelligence[1].setText(data.get('intelligence'))
            # self.presence[1].setText(data.get('presence'))
            # self.dexterity[1].setText(data.get('dexterity'))
            # self.wits[1].setText(data.get('wits'))
            # self.manipulation[1].setText(data.get('manipulation'))
            # self.stamina[1].setText(data.get('stamina'))
            # self.resolve[1].setText(data.get('resolve'))
            # self.composure[1].setText(data.get('composure'))

            if data['is human'] == True:
                if self.parent.settingsdict['isHuman'] == False:
                    self.addHuman()
                self.parent.groupname[1].setText(data.get('group name'))
                self.parent.virtue[1].setText(data.get('virtue'))
                self.parent.vice[1].setText(data.get('vice'))
                self.parent.faction[1].setText(data.get('faction'))
            else:
                if self.parent.settingsdict['isHuman'] == True:
                    self.removeHuman()

    def open(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', '', 'Json Files (*.json)')
        self.parent.savepath = path[0]
        if self.parent.savepath != ('', 'json'):
            self.loadData(self.parent.savepath)

    def positionElementsSettings(self):
        self.widgetLib.addArraystoGridIndividual([self.widgetLib.makeBlankLabel(), self.settingsTitle, self.widgetLib.makeBlankLabel()], self.settingsTitleLayout)
        self.widgetLib.addArraystoGridIndividualGroups([self.humanCheck], self.basicSettingsLayout)

    def addHuman(self):
        self.parent.settingsdict['isHuman'] = True
        self.parent.groupname = self.widgetLib.LabeledTextBox("Group Name")
        self.parent.virtue = self.widgetLib.LabeledTextBox("Virtue")
        self.parent.vice = self.widgetLib.LabeledTextBox("Vice")
        self.parent.faction = self.widgetLib.LabeledTextBox("Faction")
        with open('settings.json', 'w') as f:
            json.dump(self.parent.settingsdict, f)
        self.parent.positionElements()

    def removeHuman(self):
        self.parent.settingsdict['isHuman'] = False
        self.widgetLib.deleteArray(self.parent.groupname, self.parent.charDetailsGrid)
        self.widgetLib.deleteArray(self.parent.virtue, self.parent.charDetailsGrid)
        self.widgetLib.deleteArray(self.parent.vice, self.parent.charDetailsGrid)
        self.widgetLib.deleteArray(self.parent.faction, self.parent.charDetailsGrid)
        with open('settings.json', 'w') as f:
            json.dump(self.parent.settingsdict, f)
        self.parent.positionElements()

    def humanDef(self):
        if self.humanCheck[1].isChecked():
            self.humanCheck[1].setChecked(True)
            self.addHuman()
            self.widgetLib.quickSave()
        else:
            self.humanCheck[1].setChecked(False)
            self.removeHuman()
            self.widgetLib.quickSave()

    def basicSettings(self):
        self.basicSettingsLayout = self.widgetLib.MakeGrid(6)
        self.humanCheck = self.widgetLib.LabeledCheckBox("Is Human?", self.humanDef)
        if self.parent.settingsdict['isHuman'] == True:
            self.humanCheck[1].setChecked(True)

    def settingsdef(self):
        self.settings = ScrollableWindow()

        self.settings.setGeometry(400, 150, 384, 512)
        self.settings.setWindowTitle('Settings')

        self.settingsLayout = self.widgetLib.MakeGrid(1)
        self.widgetLib.addGridtoLayout(self.settingsLayout[0], [self.settings.baseLayout, 1, 0, 0])
        self.settingsLayout[0].setContentsMargins(0,0,0,0)

        self.settingsTitleLayout = self.widgetLib.MakeGrid(3)
        self.settingsTitle = self.widgetLib.makeLabel("Settings")
        self.settingsTitle.setFont(self.titlefont)

        self.basicSettings()

        self.widgetLib.addGridtoLayout(self.settingsTitleLayout[0], self.settingsLayout)
        self.widgetLib.addGridtoLayout(self.basicSettingsLayout[0], self.settingsLayout)

        self.positionElementsSettings()

        self.settings.show()

    def makeMenu(self):
        self.saveAction = QtGui.QAction('&Save')
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.setStatusTip('Save Character')
        self.saveAction.triggered.connect(self.save)

        self.saveAsAction = QtGui.QAction('&Save As')
        self.saveAsAction.setShortcut('Ctrl+Shift+S')
        self.saveAsAction.setStatusTip('Save Character As...')
        self.saveAsAction.triggered.connect(self.saveas)

        self.loadAction = QtGui.QAction('&Open')
        self.loadAction.setShortcut('Ctrl+O')
        self.loadAction.setStatusTip('Open Character')
        self.loadAction.triggered.connect(self.open)

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
        # self.settingsdict = parent.settingsdict

        self.widgetLib = WidgetLibrary(self.parent)

        self.baseWidget = QtWidgets.QWidget()
        self.baseLayout = [QtWidgets.QGridLayout(), 1, 0, 1]
        self.baseWidget.setLayout(self.baseLayout[0])

        self.titlefont = QtGui.QFont()
        self.titlefont.setFamily("stcaiyun")  # Set Font
        self.titlefont.setBold(True)  # Bold
        self.titlefont.setPointSize(20)  # Set font size

        self.subtitlefont = QtGui.QFont()
        self.subtitlefont.setFamily("stcaiyun")  # Set Font
        self.subtitlefont.setBold(True)  # Bold
        self.subtitlefont.setPointSize(12)  # Set font size

        self.makeScrollBar()
        self.makeMenu()



class CharEditorClass:
    def positionElements(self):
        self.charDetailsGrid[2] = 0
        self.charDetailsGrid[3] = 0
        self.widgetLib.addArraystoGridIndividualGroups([self.name, self.player, self.chronicle, self.concept, self.age], self.charDetailsGrid)
        if self.settingsdict['isHuman'] == True:
            self.widgetLib.addArraystoGridIndividualGroups([self.groupname, self.virtue, self.vice, self.faction], self.charDetailsGrid)

    def charDetails(self):
        self.charDetailsGrid = self.widgetLib.MakeGrid(6)

        self.name = self.widgetLib.LabeledTextBox("Name")
        self.player = self.widgetLib.LabeledTextBox("Player")
        self.chronicle = self.widgetLib.LabeledTextBox("Chronicle")
        self.concept = self.widgetLib.LabeledTextBox("Concept")
        self.age = self.widgetLib.LabeledTextBox("Age")

        if self.settingsdict['isHuman'] == True:
            self.groupname = self.widgetLib.LabeledTextBox("Group Name")
            self.virtue = self.widgetLib.LabeledTextBox("Virtue")
            self.vice = self.widgetLib.LabeledTextBox("Vice")
            self.faction = self.widgetLib.LabeledTextBox("Faction")

    def settingsInit(self):
        if path.exists('settings.json'):
            with open('settings.json') as f:
                self.settingsdict = json.load(f)
            if self.settingsdict['settingsVersion'] < 0:
                print("error code: SI1")
        else:
            self.settingsdict = {'settingsVersion': 0}
            self.settingsdict['isHuman'] = True
            with open('settings.json', 'w') as f:
                json.dump(self.settingsdict, f)

    def __init__(self):
        self.settingsInit()

        self.app = QtWidgets.QApplication(sys.argv)
        self.mainWindow = ScrollableWindowWithMenu(self)

        self.savepath = ""

        self.widgetLib = WidgetLibrary(self)

        self.mainWindow.setGeometry(300, 75, 1024, 768)
        self.mainWindow.setWindowTitle('Chronicles of Darkness Interactive Character Sheet')
        self.mainWindow.show()

        self.mainWindow.baseLayout[0].setContentsMargins(0,0,0,0)

        self.charDetails()

        self.widgetLib.addGridtoLayout(self.charDetailsGrid[0], self.mainWindow.baseLayout)

        self.positionElements()

        if path.exists('quicksave.json'):
            with open('quicksave.json') as f:
                data = json.load(f)

            if data['quicksave'] == True:
                dlg = CustomDialog()
                if dlg.exec():
                    self.mainWindow.loadData('quicksave.json')

        sys.exit(self.app.exec())

charEditor = CharEditorClass()
