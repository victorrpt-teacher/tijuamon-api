from src.extensions import db


class Trainer(db.Model):
    """
    Trainer model representing a user who can own Tijuamones.
    This SQLAlchemy declarative model maps to the "trainers" table and stores
    basic account information for a trainer. Instances of this class are
    ORM-managed and may be transient (not yet persisted) or attached to a
    session.
    Attributes:
        id (int | None): Primary key. May be None for transient (unsaved) instances.
        username (str): Unique username used for login and display.
        email (str): Unique email address for the trainer.
        password_hash (str): Hashed password. This is a sensitive field and
            must never be exposed in API responses or logs.
        tijuamones (list[Tijuamon]): Relationship to the trainer's Tijuamones.
            Configured with selectin loading for efficient bulk access.
    Methods:
        to_dict() -> dict[str, object]:
            Return a JSON-serializable representation of the trainer suitable
            for API responses. The returned payload deliberately omits
            sensitive fields (e.g., password_hash). If the instance has no
            persisted id, the 'id' key is removed to keep payloads compact.
    Usage example:
        trainer = Trainer(username="ash", email="ash@example.com")
        # Persist with a session, then:
        result = trainer.to_dict()  # -> {'username': 'ash', 'email': 'ash@example.com', 'id': ...}
    Notes:
        - Do not include or log `password_hash` in responses or debug output.
        - Validation (e.g., email format, password strength) should be performed
          elsewhere (e.g., service layer or input schema) before creating or
          persisting Trainer instances.
        - This docstring follows best practices for clarity and security-conscious
          API model documentation.
    """

    __tablename__ = "trainers"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    tijuamones = db.relationship(
        "Tijuamon",
        back_populates="trainer",
        lazy="selectin",
    )

    def to_dict(self) -> dict[str, object]:
        """Converts the trainer into a JSON-serializable dictionary for API responses."""
        payload = {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }
        # Remove None id to keep payloads compact when an id is not set.
        if self.id is None:
            payload.pop("id")
        return payload
