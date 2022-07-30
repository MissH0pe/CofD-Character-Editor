import json
from os import path
from PySide6 import QtCore, QtWidgets, QtGui



titlefont = QtGui.QFont()
titlefont.setFamily("stcaiyun")  # Set Font
titlefont.setBold(True)  # Bold
titlefont.setPointSize(20)  # Set font size

subtitlefont = QtGui.QFont()
subtitlefont.setFamily("stcaiyun")  # Set Font
subtitlefont.setBold(True)  # Bold
subtitlefont.setPointSize(12)  # Set font size


# class BundledGrid:
#     def __init__(self, columns):
#         self.grid = QtWidgets.QGridLayout()
#         self.columns = columns
#         self.nextOpenSlot = 0
#         self.currentRow = 0

















# pull each and everything out into a class for each widget so that it is universal between them
# pull the methods of making data into categories for each thing and then  each specific one both sets of names are added to an array to populate settings menu so that you can toggle each on independently or groups which form each splat and each subthing like vampires vs ghouls vs revenants
# add an in function delete method that properly routes deletion and deletes all extre data in each element
# add a universal get widget method in function for adding and deleting from grid purposes
# look into how to properly delete a class to make sure i'm deleting the remnants properly
# make a string interpreter that reads through an array of strings and parses it into widgets so you essentially write a sentence spread between an array that makes the widgets
# when the string interpreter loads the module it first reads the metadata like any prerequisites before it can be enabled in settings the checks are greyed out and the label is edited to say requires: whatever
# make sure that code can still support multiple things being added to settings (and can load custom functions in py files but normally have disabled and make it have to be enabled in settings and pops up a dialog explaining the risk of running unknown code) and write the text files so that each one says what is toggled on an off for each toggle in settings.
# Make the code also by default make a toggle for each thing in the settings window so one for name one for whatever and put those in advanced under overrides. also save whether or not those overrides are changed when that template is active and in saves but not between toggling that template off and back on
# also make sure that in each text file to load, that each thing added is given a name for it to allow access and smart usages this name could also be added to a list in the text file to say what gets toggled on in what parts of settings. this name is also added to a list of everything in whatever category its being placed in
# make a default simple function in settings that can be called by the string interpreter to allow variable numbers of boxes for its categories
# save everything added to the char sheet to an array that is iterated through for loading and saving
#make it so loading the settings checks each line for corruption or missing and if it is load the default
















class Label: #add way to support images
    def __del__(self):
        num = 0

    def deleteSelf(self, grid=None):
        grid.removeWidget(self.label)
        self.label.deleteLater()
        self.label = None

    def pushData(self, text):
        if self.iconbool == False:
            self.label.setText(text)
        else:
            self.label.setPixmap(QtGui.QPixmap.fromImage(text))

    def pullData(self):
        return self.text

    def getType(self):
        return self.type

    def getSelf(self):
        return self.label

    def __init__(self, text="", title=False, subtitle=False, iconbool=False):
        self.text = text
        self.type = "label"
        if iconbool == False:
            self.label = QtWidgets.QLabel(self.text)
        else:
            self.label = QtWidgets.QLabel()
        if title == True:
            self.label.setAlignment(QtGui.Qt.AlignCenter)
            self.label.setFont(titlefont)
        elif subtitle == True:
            self.label.setAlignment(QtGui.Qt.AlignCenter)
            self.label.setFont(subtitlefont)



class PushButton:
    def __del__(self):
        num = 0

    def deleteSelf(self, grid=None):
        grid.removeWidget(self.button)
        self.button.deleteLater()
        self.button = None

    def pushData(self, text):
        if self.iconbool == True:
            self.button.setIcon(QtGui.QIcon(text))
        else:
            self.button.setText(text)

    def pullData(self):
        return self.text

    def defaultDef(self):
        num = 0

    def getType(self):
        return self.type

    def getSelf(self):
        return self.button

    def __init__(self, iconbool=False, text="", def=self.defaultDef):
        self.text = text
        self.type = "button"
        self.iconbool = iconbool
        self.button = QtWidgets.QPushButton()
        self.button.clicked.connect(def)
        if self.iconbool == True:
            self.button.setIcon(QtGui.QIcon(self.text))
        else:
            self.button.setText(self.text)



class TextBox:
    def __del__(self):
        num = 0

    def deleteSelf(self, grid=None):
        grid.removeWidget(self.box)
        self.box.deleteLater()
        self.box = None

    def pushData(self, text):
        self.box.setText(text)

    def pullData(self):
        return self.box.text()

    def defaultDef(self):
        num = 0

    def getType(self):
        return self.type

    def getSelf(self):
        return self.box

    def __init__(self, def=self.defaultDef, placeholderText=""):
        self.type = "textbox"
        self.box = QtWidgets.QLineEdit()
        self.box.setText(placeholderText)
        self.box.textChanged.connect(def)



class CheckBox:
    def __del__(self):
        num = 0

    def deleteSelf(self, grid=None):
        grid.removeWidget(self.checkbox)
        self.checkbox.deleteLater()
        self.checkbox = None

    def pushData(self, state):
        self.checkbox.setChecked(state)

    def pullData(self):
        return self.checkbox.isChecked()

    def defaultDef(self):
        num = 0

    def getType(self):
        return self.type

    def getSelf(self):
        return self.checkbox

    def __init__(self, def=self.defaultDef):
        self.type = "checkbox"
        self.checkbox = QtWidgets.QCheckBox()
        self.checkbox.clicked.connect(def)



class QuadToggle:
    def __del__(self):
        num = 0

    def deleteSelf(self, grid=None):
        self.button.deleteSelf(grid=grid)
        del self.button

    def toggleQuadBox(self):
        if self.counter == 0:
            self.button.pushData("resources/default/BashingBox.png")
            # self.button.setIcon(QtGui.QIcon('resources/default/BashingBox.png'))
            self.counter = 1
        elif self.counter == 1:
            self.button.pushData("resources/default/LethalBox")
            # self.button.setIcon(QtGui.QIcon('resources/default/LethalBox.png'))
            self.counter = 2
        elif self.counter == 2:
            self.button.pushData("resources/default/AggravatedBox.png")
            # self.button.setIcon(QtGui.QIcon('resources/default/AggravatedBox.png'))
            self.counter = 3
        else:
            self.button.pushData("resources/default/BlankBox.png")
            # self.button.setIcon(QtGui.QIcon('resources/default/BlankBox.png'))
            self.counter = 0

    def getButton(self):
        return self.button

    def getType(self):
        return self.type

    def pullData(self):
        return str(self.counter)

    def pushData(self, counter):
        self.counter = int(counter)
        if self.counter == 0:
            self.button.pushData("resources/default/BlankBox.png")
            # self.button.setIcon(QtGui.QIcon('resources/default/BlankBox.png'))
        elif self.counter == 1:
            self.button.pushData("resources/default/BashingBox.png")
            # self.button.setIcon(QtGui.QIcon('resources/default/BashingBox.png'))
        elif self.counter == 2:
            self.button.pushData("resources/default/LethalBox")
            # self.button.setIcon(QtGui.QIcon('resources/default/LethalBox.png'))
        else:
            self.button.pushData("resources/default/AggravatedBox.png")
            # self.button.setIcon(QtGui.QIcon('resources/default/AggravatedBox.png'))


    def __init__(self):
        self.type = "quadtoggle"
        self.button = PushButton(iconbool=True, text="resources/default/BlankBox.png", def=self.toggleQuadBox)
        # self.button = QtWidgets.QPushButton()
        # self.button.clicked.connect(self.toggleQuadBox)
        # self.button.setIcon(QtGui.QIcon('resources/default/BlankBox.png'))
        self.counter = 0



class Grid:
    def __del__(self):
        num = 0

    def deleteElement(self, element):
        element.deleteSelf(grid=self.grid)
        del element

    def deleteAllElements(self):
        for k in range(len(self.elements)):
            self.deleteElement(self.elements[k])
        self.elements = 0

    def deleteSubgrid(self, grid):
        grid = grid.deleteSelf()

    def deleteAllSubgrids(self):
        for k in range(len(self.subgrids)):
            self.subgrids[k] = self.subgrids[k].deleteSelf()

    def deleteSelf(self, grid=None):
        self.deleteAllElements()
        self.deleteAllSubgrids()
        self.grid.setEnabled(False)
        self.grid.setParent(None)
        return None

    def areColumnsFull(self):
        if self.nextOpenSlot == self.columns:
            self.nextOpenSlot = 0
            self.currentRow = self.currentRow + 1

    def addElement(self, element):
        self.grid.addWidget(element, self.currentRow, self.nextOpenSlot)
        self.nextOpenSlot = self.nextOpenSlot + 1
        self.elements.append(element)
        self.areColumnsFull()

    def addGrid(self, grid):
        self.grid.addLayout(grid, self.currentRow, self.nextOpenSlot)
        self.nextOpenSlot = self.nextOpenSlot + 1
        self.subgrids.append(grid)
        self.areColumnsFull()

    def getNextOpenSlot(self):
        return (self.nextOpenSlot, self.currentRow)

    def getType(self):
        return self.type

    def getSelf(self):
        return self.grid

    def __init__(self, columns):
        self.columns = columns
        self.type = "grid"
        self.grid = QtWidgets.QGridLayout()
        self.nextOpenSlot = 0
        self.currentRow = 0
        self.elements = []
        self.subgrids = []



class Element: # see about condensing data into each widget
    def __del__(self):
        num = 0

    def deleteSelf(self, grid=None):
        self.widget.deleteSelf(self.parentGrid)
        del self.widget

    def addToGrid(self, grid):
        self.parentGrid = grid
        if self.type == "grid":
            self.parentGrid.addGrid(self.widget)
        else:
            self.parentGrid.addElement(self.widget)

    def getType(self):
        return self.type

    def getSelf(self):
        return self.widget

    def __init__(self, type="", widget=None):
        self.type = type
        self.widget = widget
        self.parentGrid = None



class makeElements:#see if you can make this only one loop but when it encounters a list it recursively instantiates itself to create that grid
    def __init__(self, numOfElements, string, defs=[]): #string is [[element], [element], [element, element]] subarrays are grids inside the main grid
    #pass back a dict of the widgets added at the same time as the grid so that its easier to access the added widgets
        mainGrid = Element(type="grid", widget=Grid(numOfElements))
        counter = 0
        for j in range(len(string)):
            for k in range(len(string[j])):
                if len(string[j]) > 1:
                    print("grid")
                type = string[j][k]
                if type[0] + type[1] + type[2] + type[3] + type[4] + type[5] == "label:":
                    type = type[6:]
                    if type[0] + type[1] + type[2] + type[3] + type[4] + type[5] + type[6] + type[7] + type[8] == "subtitle:":
                        type = type[9:]
                        if type[0] + type[1] + type[2] + type[3] + type[4] == "text:":
                            element = Element(type="label", widget=Label(text=type[5:], subtitle=True))
                            element.addToGrid(mainGrid)
                        elif type[0] + type[1] + type[2] + type[3] + type[4] == "icon:":
                            element = Element(type="label", widget=Label(iconbool=True, subtitle=True))
                            element.addToGrid(mainGrid)
                    elif type[0] + type[1] + type[2] + type[3] + type[4] + type[5] == "title:":
                        type = type[6:]
                        if type[0] + type[1] + type[2] + type[3] + type[4] == "text:":
                            element = Element(type="label", widget=Label(text=type[5:], title=True))
                            element.addToGrid(mainGrid)
                        elif type[0] + type[1] + type[2] + type[3] + type[4] == "icon:":
                            element = Element(type="label", widget=Label(iconbool=True, title=True))
                            element.addToGrid(mainGrid)
                    elif type[0] + type[1] + type[2] + type[3] + type[4] == "text:":
                        element = Element(type="label", widget=Label(text=type[5:]))
                        element.addToGrid(mainGrid)
                    elif type[0] + type[1] + type[2] + type[3] + type[4] == "icon:":
                        element = Element(type="label", widget=Label(iconbool=True))
                        element.addToGrid(mainGrid)
                elif type[0] + type[1] + type[2] + type[3] + type[4] + type[5] + type[6] + type[7] == "textbox:":
                    type = type[8:]
                    if type[0] + type[1] + type[2] + type[3] + type[4] + type[5] + type[6] + type[7] + type[8] == "def:true:":
                        type = type[9:]
                        if type == "":
                            element = Element(type="textbox", widget=TextBox(def=defs[counter]))
                            counter = counter + 1
                            element.addToGrid(mainGrid)
                        elif type[0] + type[1] + type[2] + type[3] + type[4] == "text:":
                            element = Element(type="textbox", widget=TextBox(def=defs[counter], placeholderText=type[5:]))
                            counter = counter + 1
                            element.addToGrid(mainGrid)
                    elif type[0] + type[1] + type[2] + type[3] + type[4] + type[5] + type[6] + type[7] + type[8] + type[9] == "def:false:":
                        type = type[10:]
                        if type == "":
                            element = Element(type="textbox", widget=TextBox())
                            element.addToGrid(mainGrid)
                        elif type[0] + type[1] + type[2] + type[3] + type[4] == "text:":
                            element = Element(type="textbox", widget=TextBox(placeholderText=type[5:]))
                            element.addToGrid(mainGrid)
        return mainGrid

# class makeElement:
#     def __init__(self, parent, label=False, title=False, subtitle=False, labeledTextBox=False, texts=[], defs=[]):
#         self.parent = parent
#         self.elements = []
#         self.elementsCount = 0
#         if label == True:
#             self.label = True
#             if title == True:



class LabeledBOD:
    def deleteSelf(self):
        if self.skill == True:
            self.grid.removeWidget(self.checkbox)
            self.checkbox.deleteLater()
            self.checkbox = None
        self.grid.removeWidget(self.label)
        self.label.deleteLater()
        self.label = None
        if self.BOD == 'boxes':
            self.dotGrid.removeWidget(self.box)
            self.box.deleteLater()
            self.box = None
        elif self.BOD == 'dots':
            for k in range(len(self.box)):
                self.dotGrid.removeWidget(self.box[k])
                self.box[k].deleteLater()
                self.box[k] = None
        else:
            print("error code: BODS " + self.labelName)
        return None

    def pushData(self, val, bool=False):
        if self.skill == True:
            self.checkbox.setChecked(bool)
        if self.BOD == 'boxes':
            self.box.setText(str(val))
        elif self.BOD == 'dots':
            for k in range(val):
                self.box[k].setChecked(True)
        else:
            print("error code: BODS " + self.labelName)

    def pullData(self):
        if self.BOD == 'boxes':
            if self.box.text() == "":
                return 0
            else:
                if self.skill == True:
                    return [self.checkbox.isChecked(), int(self.box.text())]
                return int(self.box.text())
        elif self.BOD == 'dots':
            counter = 0
            for k in range(self.BODCount):
                if self.box[k].isChecked():
                    counter = counter + 1
            if self.skill == True:
                return [self.checkbox.isChecked(), counter]
            return counter
        else:
            print("error code: BODL " + self.labelName)
            return 0

    def __init__(self, parent, labelName, window, saveload, skill = False):
        self.parent = parent
        self.label = QtWidgets.QLabel(labelName + ": ")
        self.labelName = labelName
        self.skill = skill
        self.BOD = self.parent.settingsdict['boxesordots']
        self.BODCount = 0
        self.grid = QtWidgets.QGridLayout()
        self.dotGrid = QtWidgets.QGridLayout()
        if self.skill == True:
            self.checkbox = QtWidgets.QCheckBox()
            self.checkbox.clicked.connect(saveload.quickSave)
            self.grid.addWidget(self.checkbox, 0, 0)
            self.grid.addWidget(self.label, 0, 1)
            self.grid.addLayout(self.dotGrid, 0, 2)
        else:
            self.grid.addWidget(self.label, 0, 0)
            self.grid.addLayout(self.dotGrid, 0, 1)
        self.dotsperrow = self.parent.settingsdict['dotsperrowcount']
        if self.BOD == 'boxes':
            self.box = QtWidgets.QLineEdit()
            self.dotGrid.addWidget(self.box, 0, 0)
            if window == "charsheet":
                self.box.textChanged.connect(saveload.quickSave)
        elif self.BOD == 'dots':
            self.box = []
            self.BODCount = self.parent.settingsdict['boxesordotscount']
            counter = -1
            for k in range(self.BODCount):
                self.box = self.box + [QtWidgets.QCheckBox()]
                if k % self.parent.settingsdict['dotsperrowcount'] == 0:
                    counter = counter + 1
                self.dotGrid.addWidget(self.box[k], counter, k % self.parent.settingsdict['dotsperrowcount'])
                if window == "charsheet":
                    self.box[k].clicked.connect(saveload.quickSave)
        else:
            print("error code: BODM " + self.labelName)



class SaveLoad:
    def quickSave(self):
        data = self.parent.splatManager.pullSplatData()
        data["quicksave"] = True
        with open('quicksave.json', 'w') as f:
            json.dump(data, f)

    def saveas(self):
        with open('quicksave.json', 'w') as f:
            json.dump({'quicksave': False}, f)
        data = self.parent.splatManager.pullSplatData()
        path = QtWidgets.QFileDialog.getSaveFileName(self.parent.mainWindow, 'Save as', "", "*.json")
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
            data = self.parent.splatManager.pullSplatData()
            with open(self.parent.savepath, 'w') as f:
                json.dump(data, f)
            with open('quicksave.json', 'w') as f:
                json.dump({'quicksave': False}, f)

    def open(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self.parent.mainWindow, 'Open a file', '', 'Json Files (*.json)')
        self.parent.savepath = path[0]
        if self.parent.savepath != ('', 'json'):
            self.parent.splatManager.pushSplatData(self.parent.savepath)

    def __init__(self, parent):
        self.parent = parent



class WidgetLibrary:
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

    def makeTitle(self, text):
        label = self.makeLabel(text)
        label.setAlignment(QtGui.Qt.AlignCenter)
        return label

    def MakeGrid(self, columns):
        return [QtWidgets.QGridLayout(), columns, 0, 0]
        # return BundledGrid(columns)

    def makeCheckBoxQuadCheckBox(self, window = "charsheet"):
        checkbox = QtWidgets.QCheckBox()
        quadcheckbox = QuadToggle()
        if window == "charsheet":
            checkbox.clicked.connect(self.saveLoad.quickSave)
        return [checkbox, quadcheckbox]

    def makeMerit(self, window = "charsheet"):
        box1 = QtWidgets.QLineEdit()
        box2 = QtWidgets.QLineEdit()
        if window == "charsheet":
            box1.textChanged.connect(self.saveLoad.quickSave)
            box2.textChanged.connect(self.saveLoad.quickSave)
        return [box1, box2]

    def makeSkill(self, labelName, window = "charsheet"):
        return LabeledBOD(self.parent, labelName, window, self.saveLoad, skill = True)

    def makeLabeledBOD(self, labelName, window = "charsheet"):
        return LabeledBOD(self.parent, labelName, window, self.saveLoad)

    def LabeledTextBox(self, labelName, window = "charsheet", text = ""): #pass charsheet to window when using for charsheet or settings
        label = self.makeLabel(labelName + ": ")
        box = QtWidgets.QLineEdit()
        box.setText(text)
        if window == "charsheet":
            box.textChanged.connect(self.saveLoad.quickSave)
        elif window == "settings":
            box.textChanged.connect(self.parent.settingsClass.reloadSettings)
        return [label, box]

    def makeCheckBox(self, checkdef):
        checkbox = QtWidgets.QCheckBox()
        checkbox.clicked.connect(checkdef)
        return [checkbox]

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

    def addArraystoGridGroupGroups(self, element, grid):
        sum = 0
        for k in range(len(element)):
            sum = sum + len(element[k])
        if sum <= grid[1]:
            if grid[2] < grid[1] - (sum - 1):
                for k in range(len(element)):
                    self.addArraystoGridGroup(element[k], grid)
            else:
                grid[2] = 0
                grid[3] = grid[3] + 1
                for k in range(len(element)):
                    self.addArraystoGridGroup(element[k], grid)
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
        self.saveLoad = SaveLoad(self.parent)
