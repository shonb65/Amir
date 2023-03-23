from abc import ABC
class Attack(ABC):
    def __init__(self):
        self.recoveryTime : int = 0
        self.capableTargets = []



    def getRecoveryTime(self):
        return self.recoveryTime

    def getCapableTargets(self):
        return self.capableTargets

    def setRecoveryTime(self,newRecoveryTime):
        self.recoveryTime=newRecoveryTime

    def addToCapableTargets(self,newTarget):
        self.capableTargets.append(newTarget)
