from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id           = Column(Integer, primary_key=True, index=True)
    email        = Column(String, unique=True, index=True, nullable=False)
    name         = Column(String, nullable=False)
    password     = Column(String, nullable=False)
    is_active    = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    refresh_tokens = relationship("RefreshToken", back_populates="user")