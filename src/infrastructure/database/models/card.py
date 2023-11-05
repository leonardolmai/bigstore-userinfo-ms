from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.models.base import Base
from src.infrastructure.database.models.user import User


class Card(Base):
    __tablename__ = "card"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    name: Mapped[str] = mapped_column("Name", String(length=255), nullable=False)
    number: Mapped[str] = mapped_column(
        "Card Number", String(length=16), nullable=False
    )
    expiration_month: Mapped[str] = mapped_column(
        "Expiration Month", String(length=2), nullable=False
    )
    expiration_year: Mapped[str] = mapped_column(
        "Expiration Year", String(length=4), nullable=False
    )
    cvc: Mapped[str] = mapped_column("CVC", String(length=3), nullable=False)
    user: Mapped["User"] = relationship(back_populates="card", uselist=False)
