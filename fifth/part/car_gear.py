import fifth.part.gear as g
from fifth import force as f


class CarGear(g.Gear):
    def consume(self, force: f.Force):
        print("start motion")
