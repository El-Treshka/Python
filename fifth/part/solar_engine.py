from fifth import force as f
from fifth import energy as e
from fifth.part import engine


class SolarEngine(engine.Engine):
    def transform(self, energy: e.Energy) -> f.Force:
        return f.Force(energy.get_amount())
