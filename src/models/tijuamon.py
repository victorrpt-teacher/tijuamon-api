from __future__ import annotations

from typing import Iterable, Sequence


class Tijuamon:
    """Represents a Tijuamon creature that can participate in battles or be captured.

    Attributes:
        identifier: Optional numeric id used to distinguish the creature in storage.
        name: Public name used to identify the creature.
        element_type: Elemental affinity (e.g. fire, water) used for typing advantages.
        level: Experience-based level that typically scales stats.
        hp: Current hit points that determine when the creature faints.
        attack: Base physical attack strength.
        defense: Base physical defense strength.
        habilities: List of special moves or abilities the creature can use.
    """

    def __init__(
        self,
        name: str,
        element_type: str,
        level: int = 1,
        hp: int = 20,
        attack: int = 10,
        defense: int = 10,
        habilities: Sequence[str] | None = None,
        identifier: int | None = None,
    ) -> None:
        """Initializes a Tijuamon with combat statistics and optional abilities.

        Args:
            name: Display name for the creature.
            element_type: Elemental affinity or category used in battle matchups.
            level: Starting level; higher levels usually grant better stats.
            hp: Base hit points; decrease to zero to faint.
            attack: Base attack stat used when dealing physical damage.
            defense: Base defense stat used when receiving physical damage.
            habilities: Optional iterable of ability names that the creature knows.
            identifier: Optional numeric id that can be used for lookups in APIs.
        """
        self.id = identifier
        self.name = name
        self.element_type = element_type
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.habilities = list(habilities) if habilities else []
        self.type = self.element_type  # Backward compatible alias for legacy code.

    def to_dict(self) -> dict[str, object]:
        """Converts the creature into a JSON-serializable dictionary for API responses."""
        payload = {
            "id": self.id,
            "name": self.name,
            "element_type": self.element_type,
            "level": self.level,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "habilities": list(self.habilities),
        }
        # Remove None id to keep payloads compact when an identifier is not set.
        if self.id is None:
            payload.pop("id")
        return payload

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Tijuamon":
        """Builds a Tijuamon instance from a serialized dictionary.

        Args:
            data: Dictionary with the same keys produced by ``to_dict``.

        Returns:
            A populated ``Tijuamon`` instance.
        """
        habilities_data = data.get("habilities")
        # Ensure habilities is a list of strings; default to empty list if invalid.
        if isinstance(habilities_data, Iterable) and not isinstance(habilities_data, (str, bytes)):
            habilities = list(habilities_data)
        else:
            habilities = []

        identifier = data.get("id")
        if identifier is not None:
            try:
                identifier = int(identifier)
            except (TypeError, ValueError):
                identifier = None

        return cls(
            name=str(data.get("name", "")),
            element_type=str(data.get("element_type", "")),
            level=int(data.get("level", 1)),
            hp=int(data.get("hp", 20)),
            attack=int(data.get("attack", 10)),
            defense=int(data.get("defense", 10)),
            habilities=habilities,
            identifier=identifier,
        )