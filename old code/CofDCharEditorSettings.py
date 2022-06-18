import sys
import json
from os import path
from PySide6 import QtCore, QtWidgets, QtGui

def makeBlankLabel():
    label = QtWidgets.QLabel()
    label.setText(" ")
    return label

def makeLabel(text):
    label = QtWidgets.QLabel()
    label.setText(text)
    return label

def areColumnsFull(grid):
    if grid[2] == grid[1]:
        grid[2] = 0
        grid[3] = grid[3] + 1
    return grid

def addArraystoGridIndividual(element, grid):
    for k in range(len(element)):
        grid[0].addWidget(element[k], grid[3], grid[2])
        grid[2] = grid[2] + 1
        grid = areColumnsFull(grid)

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

app = QtWidgets.QApplication(sys.argv)

settings = ScrollableWindow()

settings.setGeometry(400, 150, 384, 512)
settings.setWindowTitle('Settings')

settingsLayout = [QtWidgets.QGridLayout(), 1, 0, 0]
settings.baseLayout.addLayout(settingsLayout[0], 0, 0)
settingsLayout[0].setContentsMargins(0,0,0,0)

settings.show()

titlefont = QtGui.QFont()
titlefont.setFamily("stcaiyun")  # Set Font
titlefont.setBold(True)  # Bold
titlefont.setPointSize(20)  # Set font size

# self.subtitlefont = QtGui.QFont()
# self.subtitlefont.setFamily("stcaiyun")  # Set Font
# self.subtitlefont.setBold(True)  # Bold
# self.subtitlefont.setPointSize(12)  # Set font size

settingsTitleLayout = [QtWidgets.QGridLayout(), 3, 0, 0]
settingsLayout[0].addLayout(settingsTitleLayout[0], 0, 0)
settingsTitle = makeLabel("Settings")
settingsTitle.setFont(titlefont)

addArraystoGridIndividual([makeBlankLabel(), settingsTitle, makeBlankLabel()], settingsTitleLayout)

sys.exit(app.exec())
