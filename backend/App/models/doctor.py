from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

from app.database.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100))

    specialization: Mapped[str] = mapped_column(String(100))