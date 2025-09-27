from .trainer import Trainer
from .tijuamon import Tijuamon

class Tijuaball:
    def __init__(self, trainer: Trainer = None):
        self.owner = trainer
        self.captured_tijuamones: list[Tijuamon] = []