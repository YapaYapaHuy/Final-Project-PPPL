from User import User
from Form import Form
from Consultation import Consultation
from random import randint


class Student(User):
    def __init__(self, userID, password, name, email, idNum, desc):
        User.__init__(self, userID, password)
        self.studentName = name
        self.sEmail = email
        self.idNum = idNum
        self.desc = desc
        self.form = None
        self.consultList = {}

    def login(self, passwordInput):
        super().login(passwordInput)

    def updateProfile(self, nameInput=None, emailInput=None, descInput=None):
        if nameInput != None:
            self.studentName = nameInput
        if emailInput != None:
            self.sEmail = emailInput
        if descInput != None:
            self.desc = descInput

    def buatForm(self, result):
        self.form = Form(self.idNum, self.userID, result)

    def mintaKonsultasi(self, schedule, consultType):
        consultID = len(self.consultList) + 1
        self.consultList[consultID] = Consultation(
            consultID, self.idNum, schedule, consultType, self.form)

    def giveConsultList(self):
        return self.consultList
