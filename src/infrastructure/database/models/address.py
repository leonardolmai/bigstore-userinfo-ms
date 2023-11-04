from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.models.base import Base
from src.infrastructure.database.models.user import User


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    postal_code: Mapped[str] = mapped_column(
        "Postal Code", String(length=8), nullable=False
    )
    uf: Mapped[str] = mapped_column("UF", String(length=2), nullable=False)
    city: Mapped[str] = mapped_column("City", String(length=150), nullable=False)
    neighborhood: Mapped[str] = mapped_column(
        "Neighborhood", String(length=150), nullable=False
    )
    street: Mapped[str] = mapped_column("Street", String(length=150), nullable=False)
    number: Mapped[str] = mapped_column("Number", String(length=20), nullable=False)
    complement: Mapped[str] = mapped_column("Complement", String(length=150))
    user: Mapped["User"] = relationship(back_populates="address", uselist=False)
