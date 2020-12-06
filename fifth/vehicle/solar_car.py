import fifth.vehicle.car as c
from fifth.vehicle import driveable as d
import fifth.part.solar_battery as sb
import fifth.part.solar_engine as se
import fifth.part.car_gear as cg


class SolarCar(c.Car):

    def __init__(self, capacity_battery: float):
        super().__init__(sb.SolarBattery(capacity_battery), se.SolarEngine(), cg.CarGear())

    def accelerate(self):
        print("solar ")
        super().accelerate()

    def turn(self, direction: d.Driveable):
        print("solar ")
        super().turn(direction)

    def brake(self):
        super().brake()
