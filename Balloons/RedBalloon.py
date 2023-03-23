from Balloon import Balloon


class RedBalloon(Balloon):
    FLOAT_SPEED = 0.75
    RISE_SPEED = 0
    def __init__(self):
        Balloon.__init__(self, self.FLOAT_SPEED, self.RISE_SPEED)
