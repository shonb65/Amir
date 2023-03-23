from abc import ABC
class Attack(ABC):
    def __init__(self):
        self.recoveryTimeInSeconds : float = 0
        self.capableTargets = []



    def getRecoveryTimeInSeconds(self):
        return self.recoveryTimeInSeconds

    def getCapableTargets(self):
        return self.capableTargets

    def setRecoveryTime(self,newRecoveryTimeInSeconds):
        self.recoveryTimeInSeconds=newRecoveryTimeInSeconds

    def addToCapableTargets(self,newTarget):
        self.capableTargets.append(newTarget)
