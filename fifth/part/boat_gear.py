import fifth.part.gear as g
from fifth import force as f


class BoatGear(g.Gear):

    def consume(self, force: f.Force):
        print("start motion")
