from User import User
from Student import Student


class Professionals(User):
    def __init__(self, userID, password, name, email, pID, account, schedule):
        User.__init__(self, userID, password)
        self.pName = name
        self.pEmail = email
        self.pID = pID
        self.pAccount = account
        self.schedule = schedule

    def login(self, passwordInput):
        super().login(passwordInput)

    def updateProfile(self, nameInput=None, emailInput=None):
        if nameInput != None:
            self.pName = nameInput
        if emailInput != None:
            self.pEmail = emailInput

    def giveAccountNum(self):
        return self.pAccount

    def berikanKonsultasi(self, student, consultID):
        student.consultList[consultID].pID = self.pID
        print('Konsultasi ' + student.studentName +
              ' (ID: ' + str(consultID) + ') akan dilayani oleh: ' + self.pName)
