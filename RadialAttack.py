from Attack import Attack

class RadialAttack(Attack):
    def __init__(self):
        self.MAX_DEGREES = 360.00
        self.MIN_DEGREES = 0.00
        self.attackDegrees = 0.00


    def setAttackDegrees(self,newDegrees):
        if self.checkDegrees(newDegrees):
            self.attackDegrees = newDegrees

    def checkDegrees(self,degreesToCheck):
        return (degreesToCheck<self.MAX_DEGREES and degreesToCheck>=self.MIN_DEGREES)