import fifth.part.energy_source as es
from fifth import energy as e
import math


class SolarBattery(es.EnergySource):
    def __init__(self, capacity: float):
        self.__capacity = capacity

    def get(self) -> e.Energy:
        energy = int(math.ceil(self.__capacity * 2))
        return e.Energy(energy * 3)
