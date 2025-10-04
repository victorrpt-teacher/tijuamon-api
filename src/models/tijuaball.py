from .trainer import Trainer
from .tijuamon import Tijuamon


class Tijuaball:
    """Container device that stores captured Tijuamon creatures."""

    def __init__(self, trainer: Trainer | None = None) -> None:
        """Creates a Tijuaball optionally owned by a trainer.

        Args:
            trainer: Trainer who owns the device; use None when unassigned.
        """
        self.owner = trainer
        self.captured_tijuamones: list[Tijuamon] = []