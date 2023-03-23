from Balloon import Balloon

class GreenBalloon (Balloon):
    FLOAT_SPEED = 2
    RISE_SPEED = 5
    def __init__(self):
        Balloon.__init__(self, self.FLOAT_SPEED, self.RISE_SPEED)