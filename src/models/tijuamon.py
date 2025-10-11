from __future__ import annotations

from sqlalchemy import JSON

from src.extensions import db


class Tijuamon(db.Model):
    """Represents an individual Tijuamon creature owned by a trainer."""

    __tablename__ = "tijuamones"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    element_type = db.Column(db.String(40), nullable=False)
    level = db.Column(db.Integer, nullable=False, default=1)
    hp = db.Column(db.Integer, nullable=False, default=20)
    attack = db.Column(db.Integer, nullable=False, default=10)
    defense = db.Column(db.Integer, nullable=False, default=10)
    habilities = db.Column(JSON, nullable=False, default=list)

    trainer_id = db.Column(
        db.Integer,
        db.ForeignKey("trainers.id", ondelete="SET NULL"),
        nullable=True,
    )
    trainer = db.relationship(
        "Trainer",
        back_populates="tijuamones",
    )

    def to_dict(self) -> dict[str, object]:
        """Convert the creature into a JSON-serializable dictionary for API responses."""
        return {
            "id": self.id,
            "name": self.name,
            "element_type": self.element_type,
            "level": self.level,
            "hp": self.hp,
            "attack": self.attack,
            "defense": self.defense,
            "habilities": list(self.habilities or []),
            "trainer_id": self.trainer_id,
        }
