class Consultation:
    def __init__(self, consultID, studentID, time, consultType, pID=None, studentForm=None):
        self.consultID = consultID
        self.consultTime = time
        self.studentID = studentID
        self.pID = pID
        self.consultType = consultType
        self.consultDone = False
        self.result = None
        self.studentForm = studentForm

    def printDetail(self):
        return str("StudentID: " + str(self.studentID) + " | Time: " + self.consultTime)

    def kirimHasil(self):
        print("Hasil konsultasi: " + self.result)
