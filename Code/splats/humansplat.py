import json



class HumanClass:
    def makeCheck(self, checks):
        self.parent.humanCheck = self.widgetLib.LabeledCheckBox("Is Human?", self.parent.splatManager.splats[1].splatDef)
        if self.parent.settingsdict['splats'][1] == True:
            self.parent.humanCheck[1].setChecked(True)
        return checks + [self.parent.humanCheck]

    def positionSplatElements(self, outline):
        if self.parent.settingsdict['splats'][1] == True:
            outline[1][0] = outline[1][0] + 5
            outline[1][1] = outline[1][1] + [[self.parent.virtue, self.parent.vice], [self.parent.groupname], [self.parent.faction], [self.parent.chronicle]]
        return outline

    def pullSplatData(self, data):
        if self.parent.settingsdict['splats'][1] == True:
            data["is human"] = True
            data = data | {"group name": self.parent.groupname[1].text(), "virtue": self.parent.virtue[1].text(), "vice": self.parent.vice[1].text(), "faction": self.parent.faction[1].text(), "chronicle": self.parent.chronicle[1].text()}
        else:
            data["is human"] = False
        return data

    def pushSplatData(self, data):
        if data['is human'] == True:
            if self.parent.settingsdict['splats'][1] == False:
                self.addSplat()
            self.parent.groupname[1].setText(data.get('group name'))
            self.parent.virtue[1].setText(data.get('virtue'))
            self.parent.vice[1].setText(data.get('vice'))
            self.parent.faction[1].setText(data.get('faction'))
            self.parent.chronicle[1].setText(data.get('chronicle'))
        else:
            if self.parent.settingsdict['splats'][1] == True:
                self.removeSplat()

    def addSplat(self):
        self.parent.settingsdict['splats'][1] = True
        self.parent.virtue = self.widgetLib.LabeledTextBox("Virtue")
        self.parent.vice = self.widgetLib.LabeledTextBox("Vice")
        self.parent.groupname = self.widgetLib.LabeledTextBox("Group Name")
        self.parent.faction = self.widgetLib.LabeledTextBox("Faction")
        self.parent.chronicle = self.widgetLib.LabeledTextBox("Chronicle")
        with open('settings.json', 'w') as f:
            json.dump(self.parent.settingsdict, f)

    def removeSplat(self):
        self.parent.settingsdict['splats'][1] = False
        self.widgetLib.deleteArray(self.parent.groupname, self.parent.charDetailsGrid)
        self.widgetLib.deleteArray(self.parent.virtue, self.parent.charDetailsGrid)
        self.widgetLib.deleteArray(self.parent.vice, self.parent.charDetailsGrid)
        self.widgetLib.deleteArray(self.parent.faction, self.parent.charDetailsGrid)
        self.widgetLib.deleteArray(self.parent.chronicle, self.parent.charDetailsGrid)
        with open('settings.json', 'w') as f:
            json.dump(self.parent.settingsdict, f)

    def splatDef(self):
        if self.parent.humanCheck[1].isChecked():
            self.parent.humanCheck[1].setChecked(True)
            self.addSplat()
        else:
            self.parent.humanCheck[1].setChecked(False)
            self.removeSplat()

        self.parent.splatManager.positionSplats()

        self.widgetLib.saveLoad.quickSave()

    def __init__(self, parent):
        self.parent = parent

        self.widgetLib = self.parent.widgetLib
