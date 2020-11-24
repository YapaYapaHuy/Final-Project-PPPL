class Consultation:
    def __init__(self, consultID, studentID, time, consultType, studentForm=None, pID=None):
        self.consultID = consultID
        self.consultTime = time
        self.studentID = studentID
        self.pID = pID
        self.consultType = consultType
        self.consultDone = False
        self.result = None
        self.studentForm = studentForm

    def printDetail(self):
        print(str("StudentID: " + str(self.studentID) + " | Time: " +
                  str(self.consultTime) + " | Consultant: " + str(self.pID)))

    def kirimHasil(self):
        print("Hasil konsultasi: " + self.result)
