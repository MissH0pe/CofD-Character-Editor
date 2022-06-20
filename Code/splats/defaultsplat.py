class DefaultClass:
    def makeCheck(self, checks):
        return checks

    def positionSplatElements(self, outline):
        outline[0]['default'] = 'resources/default/CofD.png'
        outline[1][0] = outline[1][0] + 4
        outline[1][1] = outline[1][1] + [[self.parent.name], [self.parent.player], [self.parent.concept], [self.parent.age]]
        outline[2] = outline[2] + [[[self.parent.powerSubtitle], self.parent.intelligence, self.parent.strength, self.parent.presence], [[self.parent.finesseSubtitle], self.parent.wits, self.parent.dexterity, self.parent.manipulation], [[self.parent.resistanceSubtitle], self.parent.resolve, self.parent.stamina, self.parent.composure]]
        outline[3][0] = outline[3][0] + [self.parent.widgetLib.makeBlankLabel(), self.parent.mentalSubtitle, self.parent.mentalPenalty, self.parent.academics, self.parent.computer, self.parent.crafts, self.parent.investigation, self.parent.medicine, self.parent.occult, self.parent.politics, self.parent.science]
        outline[3][1] = outline[3][1] + [self.parent.widgetLib.makeBlankLabel(), self.parent.physicalSubtitle, self.parent.physicalPenalty, self.parent.athletics, self.parent.brawl, self.parent.drive, self.parent.firearms, self.parent.larceny, self.parent.stealth, self.parent.survival, self.parent.weaponry]
        outline[3][2] = outline[3][2] + [self.parent.widgetLib.makeBlankLabel(), self.parent.socialSubtitle, self.parent.socialPenalty, self.parent.animalken, self.parent.empathy, self.parent.expression, self.parent.intimidation, self.parent.persuasion, self.parent.socialize, self.parent.streetwise, self.parent.subterfuge]
        outline[4][0] = outline[4][0] + self.parent.healthBoxesArray
        return outline

    def pullSplatData(self, data):
        data = {"name": self.parent.name[1].text(), "player": self.parent.player[1].text(), "concept": self.parent.concept[1].text(), "age": self.parent.age[1].text(), "strength": self.parent.strength[1].text(), "intelligence": self.parent.intelligence[1].text(), "presence": self.parent.presence[1].text(), "dexterity": self.parent.dexterity[1].text(), "wits": self.parent.wits[1].text(), "manipulation": self.parent.manipulation[1].text(), "stamina": self.parent.stamina[1].text(), "resolve": self.parent.resolve[1].text(), "composure": self.parent.composure[1].text(), "academics": self.parent.academics[2].text(), "computer": self.parent.computer[2].text(), "crafts": self.parent.crafts[2].text(), "investigation": self.parent.investigation[2].text(), "medicine": self.parent.medicine[2].text(), "occult": self.parent.occult[2].text(), "politics": self.parent.politics[2].text(), "science": self.parent.science[2].text(), "athletics": self.parent.athletics[2].text(), "brawl": self.parent.brawl[2].text(), "drive": self.parent.drive[2].text(), "firearms": self.parent.firearms[2].text(), "larceny": self.parent.larceny[2].text(), "stealth": self.parent.stealth[2].text(), "survival": self.parent.survival[2].text(), "weaponry": self.parent.weaponry[2].text(), "animal ken": self.parent.animalken[2].text(), "empathy": self.parent.empathy[2].text(), "expression": self.parent.expression[2].text(), "intimidation": self.parent.intimidation[2].text(), "persuasion": self.parent.persuasion[2].text(), "socialize": self.parent.socialize[2].text(), "streetwise": self.parent.streetwise[2].text(), "subterfuge": self.parent.subterfuge[2].text(), "academicsspec": self.parent.academics[0].isChecked(), "computerspec": self.parent.computer[0].isChecked(), "craftsspec": self.parent.crafts[0].isChecked(), "investigationspec": self.parent.investigation[0].isChecked(), "medicinespec": self.parent.medicine[0].isChecked(), "occultspec": self.parent.occult[0].isChecked(), "politicsspec": self.parent.politics[0].isChecked(), "sciencespec": self.parent.science[0].isChecked(), "athleticsspec": self.parent.athletics[0].isChecked(), "brawlspec": self.parent.brawl[0].isChecked(), "drivespec": self.parent.drive[0].isChecked(), "firearmsspec": self.parent.firearms[0].isChecked(), "larcenyspec": self.parent.larceny[0].isChecked(), "stealthspec": self.parent.stealth[0].isChecked(), "survivalspec": self.parent.survival[0].isChecked(), "weaponryspec": self.parent.weaponry[0].isChecked(), "animal kenspec": self.parent.animalken[0].isChecked(), "empathyspec": self.parent.empathy[0].isChecked(), "expressionspec": self.parent.expression[0].isChecked(), "intimidationspec": self.parent.intimidation[0].isChecked(), "persuasionspec": self.parent.persuasion[0].isChecked(), "socializespec": self.parent.socialize[0].isChecked(), "streetwisespec": self.parent.streetwise[0].isChecked(), "subterfugespec": self.parent.subterfuge[0].isChecked()}
        array = []
        for k in range(self.parent.settingsdict['meritcount']):
            array = array + [[self.parent.meritsArray[k][0].text(), self.parent.meritsArray[k][1].text()]]
        data = data | {'meritsArray': array}
        array = []
        for k in range(self.parent.settingsdict['healthboxescount']):
            array = array + [[self.parent.healthBoxesArray[k][0].isChecked(), self.parent.healthBoxesArray[k][1].getState()]]
        data = data | {'healthboxesArray': array}
        return data

    def pushSplatData(self, data):
        self.parent.name[1].setText(data.get('name'))
        self.parent.player[1].setText(data.get('player'))
        self.parent.concept[1].setText(data.get('concept'))
        self.parent.age[1].setText(data.get('age'))

        self.parent.strength[1].setText(data.get('strength'))
        self.parent.intelligence[1].setText(data.get('intelligence'))
        self.parent.presence[1].setText(data.get('presence'))
        self.parent.dexterity[1].setText(data.get('dexterity'))
        self.parent.wits[1].setText(data.get('wits'))
        self.parent.manipulation[1].setText(data.get('manipulation'))
        self.parent.stamina[1].setText(data.get('stamina'))
        self.parent.resolve[1].setText(data.get('resolve'))
        self.parent.composure[1].setText(data.get('composure'))

        self.parent.academics[2].setText(data.get('academics'))
        self.parent.computer[2].setText(data.get('computer'))
        self.parent.crafts[2].setText(data.get('crafts'))
        self.parent.investigation[2].setText(data.get('investigation'))
        self.parent.medicine[2].setText(data.get('medicine'))
        self.parent.occult[2].setText(data.get('occult'))
        self.parent.politics[2].setText(data.get('politics'))
        self.parent.science[2].setText(data.get('science'))

        self.parent.athletics[2].setText(data.get('athletics'))
        self.parent.brawl[2].setText(data.get('brawl'))
        self.parent.drive[2].setText(data.get('drive'))
        self.parent.firearms[2].setText(data.get('firearms'))
        self.parent.larceny[2].setText(data.get('larceny'))
        self.parent.stealth[2].setText(data.get('stealth'))
        self.parent.survival[2].setText(data.get('survival'))
        self.parent.weaponry[2].setText(data.get('weaponry'))

        self.parent.animalken[2].setText(data.get('animal ken'))
        self.parent.empathy[2].setText(data.get('empathy'))
        self.parent.expression[2].setText(data.get('expression'))
        self.parent.intimidation[2].setText(data.get('intimidation'))
        self.parent.persuasion[2].setText(data.get('persuasion'))
        self.parent.socialize[2].setText(data.get('socialize'))
        self.parent.streetwise[2].setText(data.get('streetwise'))
        self.parent.subterfuge[2].setText(data.get('subterfuge'))

        self.parent.academics[0].setChecked(data.get('academicsspec'))
        self.parent.computer[0].setChecked(data.get('computerspec'))
        self.parent.crafts[0].setChecked(data.get('craftsspec'))
        self.parent.investigation[0].setChecked(data.get('investigationspec'))
        self.parent.medicine[0].setChecked(data.get('medicinespec'))
        self.parent.occult[0].setChecked(data.get('occultspec'))
        self.parent.politics[0].setChecked(data.get('politicsspec'))
        self.parent.science[0].setChecked(data.get('sciencespec'))

        self.parent.athletics[0].setChecked(data.get('athleticsspec'))
        self.parent.brawl[0].setChecked(data.get('brawlspec'))
        self.parent.drive[0].setChecked(data.get('drivespec'))
        self.parent.firearms[0].setChecked(data.get('firearmsspec'))
        self.parent.larceny[0].setChecked(data.get('larcenyspec'))
        self.parent.stealth[0].setChecked(data.get('stealthspec'))
        self.parent.survival[0].setChecked(data.get('survivalspec'))
        self.parent.weaponry[0].setChecked(data.get('weaponryspec'))

        self.parent.animalken[0].setChecked(data.get('animal kenspec'))
        self.parent.empathy[0].setChecked(data.get('empathyspec'))
        self.parent.expression[0].setChecked(data.get('expressionspec'))
        self.parent.intimidation[0].setChecked(data.get('intimidationspec'))
        self.parent.persuasion[0].setChecked(data.get('persuasionspec'))
        self.parent.socialize[0].setChecked(data.get('socializespec'))
        self.parent.streetwise[0].setChecked(data.get('streetwisespec'))
        self.parent.subterfuge[0].setChecked(data.get('subterfugespec'))

        for k in range(self.parent.settingsdict['meritcount']):
            self.parent.meritsArray[k][0].setText(data.get('meritsArray')[k][0])
            self.parent.meritsArray[k][1].setText(data.get('meritsArray')[k][1])

        for k in range(self.parent.settingsdict['healthboxescount']):
            self.parent.healthBoxesArray[k][0].setChecked(data.get('healthboxesArray')[k][0])
            self.parent.healthBoxesArray[k][1].setState(int(data.get('healthboxesArray')[k][1]))

    def addSplat(self):
        self.parent.name = self.widgetLib.LabeledTextBox("Name")
        self.parent.player = self.widgetLib.LabeledTextBox("Player")
        self.parent.concept = self.widgetLib.LabeledTextBox("Concept")
        self.parent.age = self.widgetLib.LabeledTextBox("Age")



        self.parent.powerSubtitle = self.widgetLib.makeTitle("Power")
        self.parent.powerSubtitle.setFont(self.parent.subtitlefont)
        self.parent.intelligence = self.widgetLib.LabeledTextBox("Intelligence")
        self.parent.strength = self.widgetLib.LabeledTextBox("Strength")
        self.parent.presence = self.widgetLib.LabeledTextBox("Presence")

        self.parent.finesseSubtitle = self.widgetLib.makeTitle("Finesse")
        self.parent.finesseSubtitle.setFont(self.parent.subtitlefont)
        self.parent.wits = self.widgetLib.LabeledTextBox("Wits")
        self.parent.dexterity = self.widgetLib.LabeledTextBox("Dexterity")
        self.parent.manipulation = self.widgetLib.LabeledTextBox("Manipulation")

        self.parent.resistanceSubtitle = self.widgetLib.makeTitle("Resistance")
        self.parent.resistanceSubtitle.setFont(self.parent.subtitlefont)
        self.parent.resolve = self.widgetLib.LabeledTextBox("Resolve")
        self.parent.stamina = self.widgetLib.LabeledTextBox("Stamina")
        self.parent.composure = self.widgetLib.LabeledTextBox("Composure")



        self.parent.skillsTitle = self.widgetLib.makeTitle("Skills")
        self.parent.skillsTitle.setFont(self.parent.titlefont)

        self.parent.mentalSubtitle = self.widgetLib.makeTitle("Mental")
        self.parent.mentalSubtitle.setFont(self.parent.subtitlefont)
        self.parent.mentalPenalty = self.widgetLib.makeTitle("-3 unskilled")
        self.parent.academics = self.widgetLib.makeSkill("Academics")
        self.parent.computer = self.widgetLib.makeSkill("Computer")
        self.parent.crafts = self.widgetLib.makeSkill("Crafts")
        self.parent.investigation = self.widgetLib.makeSkill("Investigation")
        self.parent.medicine = self.widgetLib.makeSkill("Medicine")
        self.parent.occult = self.widgetLib.makeSkill("Occult")
        self.parent.politics = self.widgetLib.makeSkill("Politics")
        self.parent.science = self.widgetLib.makeSkill("Science")

        self.parent.physicalSubtitle = self.widgetLib.makeTitle("Physical")
        self.parent.physicalSubtitle.setFont(self.parent.subtitlefont)
        self.parent.physicalPenalty = self.widgetLib.makeTitle("-1 unskilled")
        self.parent.athletics = self.widgetLib.makeSkill("Athletics")
        self.parent.brawl = self.widgetLib.makeSkill("Brawl")
        self.parent.drive = self.widgetLib.makeSkill("Drive")
        self.parent.firearms = self.widgetLib.makeSkill("Firearms")
        self.parent.larceny = self.widgetLib.makeSkill("Larceny")
        self.parent.stealth = self.widgetLib.makeSkill("Stealth")
        self.parent.survival = self.widgetLib.makeSkill("Survival")
        self.parent.weaponry = self.widgetLib.makeSkill("Weaponry")

        self.parent.socialSubtitle = self.widgetLib.makeTitle("Social")
        self.parent.socialSubtitle.setFont(self.parent.subtitlefont)
        self.parent.socialPenalty = self.widgetLib.makeTitle("-1 unskilled")
        self.parent.animalken = self.widgetLib.makeSkill("Animal Ken")
        self.parent.empathy = self.widgetLib.makeSkill("Empathy")
        self.parent.expression = self.widgetLib.makeSkill("Expression")
        self.parent.intimidation = self.widgetLib.makeSkill("Intimidation")
        self.parent.persuasion = self.widgetLib.makeSkill("Persuasion")
        self.parent.socialize = self.widgetLib.makeSkill("Socialize")
        self.parent.streetwise = self.widgetLib.makeSkill("Streetwise")
        self.parent.subterfuge = self.widgetLib.makeSkill("Subterfuge")

        for k in range(self.parent.settingsdict['meritcount']):
            self.parent.meritsArray = self.parent.meritsArray + [self.widgetLib.makeMerit()]

        for k in range(self.parent.settingsdict['healthboxescount']):
            self.parent.healthBoxesArray = self.parent.healthBoxesArray + [self.widgetLib.makeCheckBoxQuadCheckBox()]

    def removeSplat(self):
        print("error code: RDS1")

    def splatDef(self):
        print("error code: DSD1")

    def __init__(self, parent):
        self.parent = parent

        self.widgetLib = self.parent.widgetLib
