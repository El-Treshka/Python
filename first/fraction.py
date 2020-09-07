class Fraction:
    def __init__(self, numerator: float, denomerator: float):
        self.set_numerator(numerator)
        self.set_denomerator(denomerator)

    def get_numerator(self) -> float:
        return self._numerator

    def set_numerator(self, numerator: float):
        self._numerator = numerator

    def get_denomerator(self) -> float:
        return self._denomerator

    def set_denomerator(self, denomerator: float):
        if denomerator == 0:
            raise Exception()
        else:
            self._denomerator = denomerator

    def get_multiplication(self) -> float:
        return self._numerator * self._denomerator

    def get_division(self) -> float:
        return self._numerator / self._denomerator

    def get_addition(self) -> float:
        return self._numerator / self._denomerator

    def get_subtraction(self) -> float:
        return self._numerator - self._denomerator
