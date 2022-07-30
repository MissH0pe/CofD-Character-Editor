class DefaultClass:
    def makeCheck(self, checks):
        return checks

    def positionSplatElements(self, outline):
        outline[0]['default'] = 'resources/default/CofD.png'
        outline[1][0] = outline[1][0] + 4
        outline[1][1] = outline[1][1] + [[self.parent.name], [self.parent.player], [self.parent.concept], [self.parent.age]]
        outline[2] = outline[2] + [[self.parent.powerSubtitle, self.parent.intelligence, self.parent.strength, self.parent.presence], [self.parent.finesseSubtitle, self.parent.wits, self.parent.dexterity, self.parent.manipulation], [self.parent.resistanceSubtitle, self.parent.resolve, self.parent.stamina, self.parent.composure]]
        outline[3][0] = outline[3][0] + [self.parent.widgetLib.makeBlankLabel(), self.parent.mentalSubtitle, self.parent.mentalPenalty, self.parent.academics, self.parent.computer, self.parent.crafts, self.parent.investigation, self.parent.medicine, self.parent.occult, self.parent.politics, self.parent.science]
        outline[3][1] = outline[3][1] + [self.parent.widgetLib.makeBlankLabel(), self.parent.physicalSubtitle, self.parent.physicalPenalty, self.parent.athletics, self.parent.brawl, self.parent.drive, self.parent.firearms, self.parent.larceny, self.parent.stealth, self.parent.survival, self.parent.weaponry]
        outline[3][2] = outline[3][2] + [self.parent.widgetLib.makeBlankLabel(), self.parent.socialSubtitle, self.parent.socialPenalty, self.parent.animalken, self.parent.empathy, self.parent.expression, self.parent.intimidation, self.parent.persuasion, self.parent.socialize, self.parent.streetwise, self.parent.subterfuge]
        outline[4][0] = outline[4][0] + self.parent.healthBoxesArray
        outline[4][1] = outline[4][1] + self.parent.willpowerBoxesArray
        return outline

    def pullSplatData(self, data):
        data = {"name": self.parent.name[1].text(), "player": self.parent.player[1].text(), "concept": self.parent.concept[1].text(), "age": self.parent.age[1].text(), "strength": self.parent.strength.pullData(), "intelligence": self.parent.intelligence.pullData(), "presence": self.parent.presence.pullData(), "dexterity": self.parent.dexterity.pullData(), "wits": self.parent.wits.pullData(), "manipulation": self.parent.manipulation.pullData(), "stamina": self.parent.stamina.pullData(), "resolve": self.parent.resolve.pullData(), "composure": self.parent.composure.pullData(), "academics": self.parent.academics.pullData()[1], "computer": self.parent.computer.pullData()[1], "crafts": self.parent.crafts.pullData()[1], "investigation": self.parent.investigation.pullData()[1], "medicine": self.parent.medicine.pullData()[1], "occult": self.parent.occult.pullData()[1], "politics": self.parent.politics.pullData()[1], "science": self.parent.science.pullData()[1], "athletics": self.parent.athletics.pullData()[1], "brawl": self.parent.brawl.pullData()[1], "drive": self.parent.drive.pullData()[1], "firearms": self.parent.firearms.pullData()[1], "larceny": self.parent.larceny.pullData()[1], "stealth": self.parent.stealth.pullData()[1], "survival": self.parent.survival.pullData()[1], "weaponry": self.parent.weaponry.pullData()[1], "animal ken": self.parent.animalken.pullData()[1], "empathy": self.parent.empathy.pullData()[1], "expression": self.parent.expression.pullData()[1], "intimidation": self.parent.intimidation.pullData()[1], "persuasion": self.parent.persuasion.pullData()[1], "socialize": self.parent.socialize.pullData()[1], "streetwise": self.parent.streetwise.pullData()[1], "subterfuge": self.parent.subterfuge.pullData()[1], "academicsspec": self.parent.academics.pullData()[0], "computerspec": self.parent.computer.pullData()[0], "craftsspec": self.parent.crafts.pullData()[0], "investigationspec": self.parent.investigation.pullData()[0], "medicinespec": self.parent.medicine.pullData()[0], "occultspec": self.parent.occult.pullData()[0], "politicsspec": self.parent.politics.pullData()[0], "sciencespec": self.parent.science.pullData()[0], "athleticsspec": self.parent.athletics.pullData()[0], "brawlspec": self.parent.brawl.pullData()[0], "drivespec": self.parent.drive.pullData()[0], "firearmsspec": self.parent.firearms.pullData()[0], "larcenyspec": self.parent.larceny.pullData()[0], "stealthspec": self.parent.stealth.pullData()[0], "survivalspec": self.parent.survival.pullData()[0], "weaponryspec": self.parent.weaponry.pullData()[0], "animal kenspec": self.parent.animalken.pullData()[0], "empathyspec": self.parent.empathy.pullData()[0], "expressionspec": self.parent.expression.pullData()[0], "intimidationspec": self.parent.intimidation.pullData()[0], "persuasionspec": self.parent.persuasion.pullData()[0], "socializespec": self.parent.socialize.pullData()[0], "streetwisespec": self.parent.streetwise.pullData()[0], "subterfugespec": self.parent.subterfuge.pullData()[0]}
        array = []
        for k in range(self.parent.settingsdict['meritcount']):
            array = array + [[self.parent.meritsArray[k][0].text(), self.parent.meritsArray[k][1].text()]]
        data = data | {'meritsArray': array}
        array = []
        for k in range(self.parent.settingsdict['healthboxescount']):
            array = array + [[self.parent.healthBoxesArray[k][0].isChecked(), self.parent.healthBoxesArray[k][1].getState()]]
        data = data | {'healthboxesArray': array}
        array = []
        for k in range(self.parent.settingsdict['willpowerboxescount']):
            array = array + [[self.parent.willpowerBoxesArray[k][0].isChecked(), self.parent.willpowerBoxesArray[k][1].isChecked()]]
        data = data | {'willpowerboxesArray': array}
        return data

    def pushSplatData(self, data):
        self.parent.name[1].setText(data.get('name'))
        self.parent.player[1].setText(data.get('player'))
        self.parent.concept[1].setText(data.get('concept'))
        self.parent.age[1].setText(data.get('age'))

        # if data.get("boxesordots") == 'boxes':
        self.parent.strength.pushData(int(data.get('strength')))
        self.parent.intelligence.pushData(int(data.get('intelligence')))
        self.parent.presence.pushData(int(data.get('presence')))
        self.parent.dexterity.pushData(int(data.get('dexterity')))
        self.parent.wits.pushData(int(data.get('wits')))
        self.parent.manipulation.pushData(int(data.get('manipulation')))
        self.parent.stamina.pushData(int(data.get('stamina')))
        self.parent.resolve.pushData(int(data.get('resolve')))
        self.parent.composure.pushData(int(data.get('composure')))
        # elif data.get("boxesordots") == 'dots':
        #     for k in range(int(data.get("strength"))):
        #         self.parent.strength[1][k].setChecked(True)
        #     for k in range(int(data.get("intelligence"))):
        #         self.parent.intelligence[1][k].setChecked(True)
        #     for k in range(int(data.get("presence"))):
        #         self.parent.presence[1][k].setChecked(True)
        #     for k in range(int(data.get("dexterity"))):
        #         self.parent.dexterity[1][k].setChecked(True)
        #     for k in range(int(data.get("wits"))):
        #         self.parent.wits[1][k].setChecked(True)
        #     for k in range(int(data.get("manipulation"))):
        #         self.parent.manipulation[1][k].setChecked(True)
        #     for k in range(int(data.get("stamina"))):
        #         self.parent.stamina[1][k].setChecked(True)
        #     for k in range(int(data.get("resolve"))):
        #         self.parent.resolve[1][k].setChecked(True)
        #     for k in range(int(data.get("composure"))):
        #         self.parent.composure[1][k].setChecked(True)

        self.parent.academics.pushData(int(data.get('academics')), bool = data.get('academicsspec'))
        self.parent.computer.pushData(int(data.get('computer')), bool = data.get('computerspec'))
        self.parent.crafts.pushData(int(data.get('crafts')), bool = data.get('craftsspec'))
        self.parent.investigation.pushData(int(data.get('investigation')), bool = data.get('investigationspec'))
        self.parent.medicine.pushData(int(data.get('medicine')), bool = data.get('medicinespec'))
        self.parent.occult.pushData(int(data.get('occult')), bool = data.get('occultspec'))
        self.parent.politics.pushData(int(data.get('politics')), bool = data.get('politicsspec'))
        self.parent.science.pushData(int(data.get('science')), bool = data.get('sciencespec'))

        self.parent.athletics.pushData(int(data.get('athletics')), bool = data.get('athleticsspec'))
        self.parent.brawl.pushData(int(data.get('brawl')), bool = data.get('brawlspec'))
        self.parent.drive.pushData(int(data.get('drive')), bool = data.get('drivespec'))
        self.parent.firearms.pushData(int(data.get('firearms')), bool = data.get('firearmsspec'))
        self.parent.larceny.pushData(int(data.get('larceny')), bool = data.get('larcenyspec'))
        self.parent.stealth.pushData(int(data.get('stealth')), bool = data.get('stealthspec'))
        self.parent.survival.pushData(int(data.get('survival')), bool = data.get('survivalspec'))
        self.parent.weaponry.pushData(int(data.get('weaponry')), bool = data.get('weaponryspec'))

        self.parent.animalken.pushData(int(data.get('animal ken')), bool = data.get('animal kenspec'))
        self.parent.empathy.pushData(int(data.get('empathy')), bool = data.get('empathyspec'))
        self.parent.expression.pushData(int(data.get('expression')), bool = data.get('expressionspec'))
        self.parent.intimidation.pushData(int(data.get('intimidation')), bool = data.get('intimidationspec'))
        self.parent.persuasion.pushData(int(data.get('persuasion')), bool = data.get('persuasionspec'))
        self.parent.socialize.pushData(int(data.get('socialize')), bool = data.get('socializespec'))
        self.parent.streetwise.pushData(int(data.get('streetwise')), bool = data.get('streetwisespec'))
        self.parent.subterfuge.pushData(int(data.get('subterfuge')), bool = data.get('subterfugespec'))

        # self.parent.academics[0].setChecked(data.get('academicsspec'))
        # self.parent.computer[0].setChecked(data.get('computerspec'))
        # self.parent.crafts[0].setChecked(data.get('craftsspec'))
        # self.parent.investigation[0].setChecked(data.get('investigationspec'))
        # self.parent.medicine[0].setChecked(data.get('medicinespec'))
        # self.parent.occult[0].setChecked(data.get('occultspec'))
        # self.parent.politics[0].setChecked(data.get('politicsspec'))
        # self.parent.science[0].setChecked(data.get('sciencespec'))
        #
        # self.parent.athletics[0].setChecked(data.get('athleticsspec'))
        # self.parent.brawl[0].setChecked(data.get('brawlspec'))
        # self.parent.drive[0].setChecked(data.get('drivespec'))
        # self.parent.firearms[0].setChecked(data.get('firearmsspec'))
        # self.parent.larceny[0].setChecked(data.get('larcenyspec'))
        # self.parent.stealth[0].setChecked(data.get('stealthspec'))
        # self.parent.survival[0].setChecked(data.get('survivalspec'))
        # self.parent.weaponry[0].setChecked(data.get('weaponryspec'))
        #
        # self.parent.animalken[0].setChecked(data.get('animal kenspec'))
        # self.parent.empathy[0].setChecked(data.get('empathyspec'))
        # self.parent.expression[0].setChecked(data.get('expressionspec'))
        # self.parent.intimidation[0].setChecked(data.get('intimidationspec'))
        # self.parent.persuasion[0].setChecked(data.get('persuasionspec'))
        # self.parent.socialize[0].setChecked(data.get('socializespec'))
        # self.parent.streetwise[0].setChecked(data.get('streetwisespec'))
        # self.parent.subterfuge[0].setChecked(data.get('subterfugespec'))

        for k in range(self.parent.settingsdict['meritcount']):
            self.parent.meritsArray[k][0].setText(data.get('meritsArray')[k][0])
            self.parent.meritsArray[k][1].setText(data.get('meritsArray')[k][1])

        for k in range(self.parent.settingsdict['healthboxescount']):
            self.parent.healthBoxesArray[k][0].setChecked(data.get('healthboxesArray')[k][0])
            self.parent.healthBoxesArray[k][1].setState(int(data.get('healthboxesArray')[k][1]))

        for k in range(self.parent.settingsdict['willpowerboxescount']):
            self.parent.willpowerBoxesArray[k][0].setChecked(data.get('willpowerboxesArray')[k][0])
            self.parent.willpowerBoxesArray[k][1].setChecked(data.get('willpowerboxesArray')[k][1])

    def addBOD(self):
        self.parent.intelligence = self.widgetLib.makeLabeledBOD("Intelligence")
        self.parent.BODs = self.parent.BODs + [self.parent.intelligence]
        self.parent.strength = self.widgetLib.makeLabeledBOD("Strength")
        self.parent.BODs = self.parent.BODs + [self.parent.strength]
        self.parent.presence = self.widgetLib.makeLabeledBOD("Presence")
        self.parent.BODs = self.parent.BODs + [self.parent.presence]
        self.parent.wits = self.widgetLib.makeLabeledBOD("Wits")
        self.parent.BODs = self.parent.BODs + [self.parent.wits]
        self.parent.dexterity = self.widgetLib.makeLabeledBOD("Dexterity")
        self.parent.BODs = self.parent.BODs + [self.parent.dexterity]
        self.parent.manipulation = self.widgetLib.makeLabeledBOD("Manipulation")
        self.parent.BODs = self.parent.BODs + [self.parent.manipulation]
        self.parent.resolve = self.widgetLib.makeLabeledBOD("Resolve")
        self.parent.BODs = self.parent.BODs + [self.parent.resolve]
        self.parent.stamina = self.widgetLib.makeLabeledBOD("Stamina")
        self.parent.BODs = self.parent.BODs + [self.parent.stamina]
        self.parent.composure = self.widgetLib.makeLabeledBOD("Composure")
        self.parent.BODs = self.parent.BODs + [self.parent.composure]

        self.parent.academics = self.widgetLib.makeSkill("Academics")
        self.parent.BODs = self.parent.BODs + [self.parent.academics]
        self.parent.computer = self.widgetLib.makeSkill("Computer")
        self.parent.BODs = self.parent.BODs + [self.parent.computer]
        self.parent.crafts = self.widgetLib.makeSkill("Crafts")
        self.parent.BODs = self.parent.BODs + [self.parent.crafts]
        self.parent.investigation = self.widgetLib.makeSkill("Investigation")
        self.parent.BODs = self.parent.BODs + [self.parent.investigation]
        self.parent.medicine = self.widgetLib.makeSkill("Medicine")
        self.parent.BODs = self.parent.BODs + [self.parent.medicine]
        self.parent.occult = self.widgetLib.makeSkill("Occult")
        self.parent.BODs = self.parent.BODs + [self.parent.occult]
        self.parent.politics = self.widgetLib.makeSkill("Politics")
        self.parent.BODs = self.parent.BODs + [self.parent.politics]
        self.parent.science = self.widgetLib.makeSkill("Science")
        self.parent.BODs = self.parent.BODs + [self.parent.science]
        self.parent.athletics = self.widgetLib.makeSkill("Athletics")
        self.parent.BODs = self.parent.BODs + [self.parent.athletics]
        self.parent.brawl = self.widgetLib.makeSkill("Brawl")
        self.parent.BODs = self.parent.BODs + [self.parent.brawl]
        self.parent.drive = self.widgetLib.makeSkill("Drive")
        self.parent.BODs = self.parent.BODs + [self.parent.drive]
        self.parent.firearms = self.widgetLib.makeSkill("Firearms")
        self.parent.BODs = self.parent.BODs + [self.parent.firearms]
        self.parent.larceny = self.widgetLib.makeSkill("Larceny")
        self.parent.BODs = self.parent.BODs + [self.parent.larceny]
        self.parent.stealth = self.widgetLib.makeSkill("Stealth")
        self.parent.BODs = self.parent.BODs + [self.parent.stealth]
        self.parent.survival = self.widgetLib.makeSkill("Survival")
        self.parent.BODs = self.parent.BODs + [self.parent.survival]
        self.parent.weaponry = self.widgetLib.makeSkill("Weaponry")
        self.parent.BODs = self.parent.BODs + [self.parent.weaponry]
        self.parent.animalken = self.widgetLib.makeSkill("Animal Ken")
        self.parent.BODs = self.parent.BODs + [self.parent.animalken]
        self.parent.empathy = self.widgetLib.makeSkill("Empathy")
        self.parent.BODs = self.parent.BODs + [self.parent.empathy]
        self.parent.expression = self.widgetLib.makeSkill("Expression")
        self.parent.BODs = self.parent.BODs + [self.parent.expression]
        self.parent.intimidation = self.widgetLib.makeSkill("Intimidation")
        self.parent.BODs = self.parent.BODs + [self.parent.intimidation]
        self.parent.persuasion = self.widgetLib.makeSkill("Persuasion")
        self.parent.BODs = self.parent.BODs + [self.parent.persuasion]
        self.parent.socialize = self.widgetLib.makeSkill("Socialize")
        self.parent.BODs = self.parent.BODs + [self.parent.socialize]
        self.parent.streetwise = self.widgetLib.makeSkill("Streetwise")
        self.parent.BODs = self.parent.BODs + [self.parent.streetwise]
        self.parent.subterfuge = self.widgetLib.makeSkill("Subterfuge")
        self.parent.BODs = self.parent.BODs + [self.parent.subterfuge]

    def addSplat(self):
        self.parent.name = self.widgetLib.LabeledTextBox("Name")
        self.parent.player = self.widgetLib.LabeledTextBox("Player")
        self.parent.concept = self.widgetLib.LabeledTextBox("Concept")
        self.parent.age = self.widgetLib.LabeledTextBox("Age")



        self.addBOD()



        self.parent.powerSubtitle = self.widgetLib.makeTitle("Power")
        self.parent.powerSubtitle.setFont(self.parent.subtitlefont)
        # self.parent.intelligence = self.widgetLib.makeLabeledBOD("Intelligence")
        # self.parent.BODs = self.parent.BODs + [self.parent.intelligence]
        # self.parent.strength = self.widgetLib.makeLabeledBOD("Strength")
        # self.parent.BODs = self.parent.BODs + [self.parent.strength]
        # self.parent.presence = self.widgetLib.makeLabeledBOD("Presence")
        # self.parent.BODs = self.parent.BODs + [self.parent.presence]

        self.parent.finesseSubtitle = self.widgetLib.makeTitle("Finesse")
        self.parent.finesseSubtitle.setFont(self.parent.subtitlefont)
        # self.parent.wits = self.widgetLib.makeLabeledBOD("Wits")
        # self.parent.BODs = self.parent.BODs + [self.parent.wits]
        # self.parent.dexterity = self.widgetLib.makeLabeledBOD("Dexterity")
        # self.parent.BODs = self.parent.BODs + [self.parent.dexterity]
        # self.parent.manipulation = self.widgetLib.makeLabeledBOD("Manipulation")
        # self.parent.BODs = self.parent.BODs + [self.parent.manipulation]

        self.parent.resistanceSubtitle = self.widgetLib.makeTitle("Resistance")
        self.parent.resistanceSubtitle.setFont(self.parent.subtitlefont)
        # self.parent.resolve = self.widgetLib.makeLabeledBOD("Resolve")
        # self.parent.BODs = self.parent.BODs + [self.parent.resolve]
        # self.parent.stamina = self.widgetLib.makeLabeledBOD("Stamina")
        # self.parent.BODs = self.parent.BODs + [self.parent.stamina]
        # self.parent.composure = self.widgetLib.makeLabeledBOD("Composure")
        # self.parent.BODs = self.parent.BODs + [self.parent.composure]



        self.parent.skillsTitle = self.widgetLib.makeTitle("Skills")
        self.parent.skillsTitle.setFont(self.parent.titlefont)

        self.parent.mentalSubtitle = self.widgetLib.makeTitle("Mental")
        self.parent.mentalSubtitle.setFont(self.parent.subtitlefont)
        self.parent.mentalPenalty = self.widgetLib.makeTitle("-3 unskilled")
        # self.parent.academics = self.widgetLib.makeSkill("Academics")
        # self.parent.BODs = self.parent.BODs + [self.parent.academics]
        # self.parent.computer = self.widgetLib.makeSkill("Computer")
        # self.parent.BODs = self.parent.BODs + [self.parent.computer]
        # self.parent.crafts = self.widgetLib.makeSkill("Crafts")
        # self.parent.BODs = self.parent.BODs + [self.parent.crafts]
        # self.parent.investigation = self.widgetLib.makeSkill("Investigation")
        # self.parent.BODs = self.parent.BODs + [self.parent.investigation]
        # self.parent.medicine = self.widgetLib.makeSkill("Medicine")
        # self.parent.BODs = self.parent.BODs + [self.parent.medicine]
        # self.parent.occult = self.widgetLib.makeSkill("Occult")
        # self.parent.BODs = self.parent.BODs + [self.parent.occult]
        # self.parent.politics = self.widgetLib.makeSkill("Politics")
        # self.parent.BODs = self.parent.BODs + [self.parent.politics]
        # self.parent.science = self.widgetLib.makeSkill("Science")
        # self.parent.BODs = self.parent.BODs + [self.parent.science]

        self.parent.physicalSubtitle = self.widgetLib.makeTitle("Physical")
        self.parent.physicalSubtitle.setFont(self.parent.subtitlefont)
        self.parent.physicalPenalty = self.widgetLib.makeTitle("-1 unskilled")
        # self.parent.athletics = self.widgetLib.makeSkill("Athletics")
        # self.parent.BODs = self.parent.BODs + [self.parent.athletics]
        # self.parent.brawl = self.widgetLib.makeSkill("Brawl")
        # self.parent.BODs = self.parent.BODs + [self.parent.brawl]
        # self.parent.drive = self.widgetLib.makeSkill("Drive")
        # self.parent.BODs = self.parent.BODs + [self.parent.drive]
        # self.parent.firearms = self.widgetLib.makeSkill("Firearms")
        # self.parent.BODs = self.parent.BODs + [self.parent.firearms]
        # self.parent.larceny = self.widgetLib.makeSkill("Larceny")
        # self.parent.BODs = self.parent.BODs + [self.parent.larceny]
        # self.parent.stealth = self.widgetLib.makeSkill("Stealth")
        # self.parent.BODs = self.parent.BODs + [self.parent.stealth]
        # self.parent.survival = self.widgetLib.makeSkill("Survival")
        # self.parent.BODs = self.parent.BODs + [self.parent.survival]
        # self.parent.weaponry = self.widgetLib.makeSkill("Weaponry")
        # self.parent.BODs = self.parent.BODs + [self.parent.weaponry]

        self.parent.socialSubtitle = self.widgetLib.makeTitle("Social")
        self.parent.socialSubtitle.setFont(self.parent.subtitlefont)
        self.parent.socialPenalty = self.widgetLib.makeTitle("-1 unskilled")
        # self.parent.animalken = self.widgetLib.makeSkill("Animal Ken")
        # self.parent.BODs = self.parent.BODs + [self.parent.animalken]
        # self.parent.empathy = self.widgetLib.makeSkill("Empathy")
        # self.parent.BODs = self.parent.BODs + [self.parent.empathy]
        # self.parent.expression = self.widgetLib.makeSkill("Expression")
        # self.parent.BODs = self.parent.BODs + [self.parent.expression]
        # self.parent.intimidation = self.widgetLib.makeSkill("Intimidation")
        # self.parent.BODs = self.parent.BODs + [self.parent.intimidation]
        # self.parent.persuasion = self.widgetLib.makeSkill("Persuasion")
        # self.parent.BODs = self.parent.BODs + [self.parent.persuasion]
        # self.parent.socialize = self.widgetLib.makeSkill("Socialize")
        # self.parent.BODs = self.parent.BODs + [self.parent.socialize]
        # self.parent.streetwise = self.widgetLib.makeSkill("Streetwise")
        # self.parent.BODs = self.parent.BODs + [self.parent.streetwise]
        # self.parent.subterfuge = self.widgetLib.makeSkill("Subterfuge")
        # self.parent.BODs = self.parent.BODs + [self.parent.subterfuge]

        for k in range(self.parent.settingsdict['meritcount']):
            self.parent.meritsArray = self.parent.meritsArray + [self.widgetLib.makeMerit()]

        for k in range(self.parent.settingsdict['healthboxescount']):
            self.parent.healthBoxesArray = self.parent.healthBoxesArray + [self.widgetLib.makeCheckBoxQuadCheckBox()]

        for k in range(self.parent.settingsdict['willpowerboxescount']):
            self.parent.willpowerBoxesArray = self.parent.willpowerBoxesArray + [[self.widgetLib.makeCheckBox(self.parent.widgetLib.saveLoad.quickSave)[0], self.widgetLib.makeCheckBox(self.parent.widgetLib.saveLoad.quickSave)[0]]]

    def removeSplat(self):
        print("error code: RDS1")

    def splatDef(self):
        print("error code: DSD1")

    def __init__(self, parent):
        self.parent = parent

        self.widgetLib = self.parent.widgetLib
