import fifth.vehicle.vehicle as v
from fifth.part import energy_source as es, engine as e, gear as g
from fifth.vehicle import driveable as d


class Car(v.Vehicle):
    def __init__(self, energy_source: es.EnergySource, engine: e.Engine, gear: g.Gear):
        super().__init__(energy_source, engine, gear)

    def accelerate(self):
        super().accelerate()
        print("car accelerated")

    def turn(self, direction: d.Driveable):
        print("car ")
        super().turn(direction)

    def brake(self):
        super().brake()