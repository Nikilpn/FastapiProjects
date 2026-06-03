from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import UserCreate
from app.models import User
from app.dependencies import get_db
from app.core.security import hash_password

router = APIRouter()

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user