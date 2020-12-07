import fifth.part.energy_source as es
import fifth.part.engine as e
import fifth.part.gear as g
import fifth.vehicle.driveable as d
import math


class Vehicle(d.Driveable):
    def __init__(self, energy_source: es.EnergySource, engine: e.Engine, gear: g.Gear):
        self.__energy_source = energy_source
        self.__engine = engine
        self.__gear = gear
        self.__speed = 0

    def accelerate(self):
        energy = self.__energy_source.get()
        force = self.__engine.transform(energy)
        self.__speed = self.__speed + force.get_amount()
        print("speed:", self.__speed, " km/h")

    def turn(self, direction: d.Driveable):
        if direction == 1:
            print("turns left")
        elif direction == 2:
            print("turns right")

    def brake(self):
        while self.__speed != 0:
            self.__speed = self.__speed - math.ceil(self.__speed / 2)
            if self.__speed == 1:
                self.__speed = 0
            print("speed: ", self.__speed, " km/h")
        print("stop")
