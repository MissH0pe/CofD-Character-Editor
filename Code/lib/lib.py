import json
from os import path
from PySide6 import QtCore, QtWidgets, QtGui



# class BundledGrid:
#     def __init__(self, columns):
#         self.grid = QtWidgets.QGridLayout()
#         self.columns = columns
#         self.nextOpenSlot = 0
#         self.currentRow = 0



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

    def MakeGrid(self, columns):
        return [QtWidgets.QGridLayout(), columns, 0, 0]
        # return BundledGrid(columns)

    def makeSkill(self, labelName, charsheetbool = True):
        checkbox = QtWidgets.QCheckBox()
        checkbox.clicked.connect(self.saveLoad.quickSave)
        label = self.makeLabel(labelName)
        box = QtWidgets.QLineEdit()
        if charsheetbool == True:
            box.textChanged.connect(self.saveLoad.quickSave)
        return [checkbox, label, box]

    def LabeledTextBox(self, labelName, charsheetbool = True): #pass charsheetbool = False when not using for charsheet
        label = self.makeLabel(labelName + ": ")
        box = QtWidgets.QLineEdit()
        if charsheetbool == True:
            box.textChanged.connect(self.saveLoad.quickSave)
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
