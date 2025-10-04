class Trainer:
    """Represents a human trainer that can own and command Tijuamones."""

    def __init__(self, name: str) -> None:
        """Creates a trainer with a display name.

        Args:
            name: Public name used to identify the trainer within the league.
        """
        self.name = name