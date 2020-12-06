import fifth.vehicle.driveable as d
import fifth.vehicle.direction as di
import fifth.vehicle.boat as b
import fifth.part.gas_tank as gt
import fifth.part.gasoline_engine as ge
import fifth.part.boat_gear as bg
import fifth.vehicle.car as c
import fifth.vehicle.solar_car as sc
import fifth.part.car_gear as cg


def test_drive(driveable: d.Driveable):
    driveable.accelerate()
    driveable.turn(di.Direction.Left)
    driveable.turn(di.Direction.Right)
    driveable.brake()
    driveable.accelerate()
    driveable.brake()


class Main:

    def __init__(self):
        boat = b.Boat(gt.GasTank(50), ge.GasolineEngine(), bg.BoatGear())
        car = c.Car(gt.GasTank(50), ge.GasolineEngine(), cg.CarGear())
        solar_car = sc.SolarCar(50)
        vehicles = [boat, car, solar_car]
        for vehicle in vehicles:
            test_drive(vehicle)

Main()
