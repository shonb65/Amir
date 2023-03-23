from abc import ABC


class Balloon (ABC):
    def __init__(self, floatSpeed, riseSpeed):
        self.floatSpeed = floatSpeed
        self.riseSpeed = riseSpeed

    def getFloatSpeed(self):
        return self.floatSpeed

    def getRiseSpeed(self):
        return self.riseSpeed