from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    Interval,
    String,
    Text,
    DateTime,
    ForeignKey,
    Boolean,
    Float,
    Time,
)
from sqlalchemy.orm import relationship
import datetime
from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger,
                primary_key=True,
                unique=True,
                autoincrement=True,
                index=True)
    username = Column(String(255))
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    tg_id = Column(
        String(255),
        unique=True,
    )
    phone = Column(String(255), nullable=True)
    date_join = Column(DateTime, default=datetime.datetime.now)
    is_admin = Column(Boolean, default=False)


    def __str__(self) -> str:
        return self.username