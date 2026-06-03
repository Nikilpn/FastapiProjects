from sqlalchemy.orm import Session
from app.users.models import User
from app.users.schemas import UserCreate
from app.core.security import hash_password

def create_user(db: Session, data: UserCreate) -> User:
    user = User(
        email=data.email,
        name=data.name,
        password=hash_password(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def create_superuser(db: Session, data: UserCreate) -> User:
    user = User(
        email=data.email,
        name=data.name,
        password=hash_password(data.password),
        is_superuser=True  # ← superuser
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user