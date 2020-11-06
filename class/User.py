from abc import ABC, abstractmethod


class User():
    def __init__(self, userID, password):
        self.userID = userID
        self.password = password
        self.loginStatus = False

    def verifyLogin(self):
        return self.loginStatus

    @abstractmethod
    def login(self, passwordInput):
        if passwordInput == self.password:
            self.loginStatus = True

    @abstractmethod
    def updateProfile(self):
        pass
