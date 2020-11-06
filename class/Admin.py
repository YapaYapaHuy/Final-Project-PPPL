from User import User
from Student import Student


class Admin(User):
    def __init__(self, userID, password, adminName, email):
        User.__init__(self, userID, password)
        self.adminName = adminName
        self.adminEmail = email

    def login(self, passwordInput):
        super().login(passwordInput)

    def bayarTP(self, pID, amount):
        print('Paid ' + str(amount) + ' to Professional ID: ' + str(pID))

    def siapkanKonsultasi(self, student, consultID):
        student.consultList[consultID].consultDone = True
        self.catatKonsultasi(student, consultID, "Baik")
        self.bayarTP(student.consultList[consultID].pID, 50000)

    def catatKonsultasi(self, student, consultID, result):
        student.consultList[consultID].result = result
        print('Konsultasi ' + student.studentName +
              ' (ID: ' + str(consultID) + ') sudah direkam.')
