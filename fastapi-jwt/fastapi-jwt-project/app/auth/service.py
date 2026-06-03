from sqlalchemy.orm import Session
from datetime import datetime
from app.users.service import get_user_by_email
from app.core.security import (
    verify_password,
    create_access_token,
    create_refresh_token,
    get_refresh_token_expiry
)
from app.auth.models import RefreshToken

def login(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.password):
        return None, None

    access_token  = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token()

    # DB-ൽ refresh token save ചെയ്യുന്നു
    db_token = RefreshToken(
        token      = refresh_token,
        user_id    = user.id,
        expires_at = get_refresh_token_expiry(),
        is_revoked = False
    )
    db.add(db_token)
    db.commit()

    return access_token, refresh_token

def refresh_access_token(db: Session, refresh_token: str):
    # DB-ൽ token check ചെയ്യുന്നു
    db_token = db.query(RefreshToken).filter(
        RefreshToken.token == refresh_token,
        RefreshToken.is_revoked == False
    ).first()

    if not db_token:
        return None

    # Expire ആയോ എന്ന് check ചെയ്യുന്നു
    if db_token.expires_at < datetime.utcnow():
        return None

    # New access token കൊടുക്കുന്നു
    new_access_token = create_access_token(data={"sub": db_token.user.email})
    return new_access_token

def logout(db: Session, refresh_token: str):
    db_token = db.query(RefreshToken).filter(
        RefreshToken.token == refresh_token
    ).first()
    if db_token:
        db_token.is_revoked = True
        db.commit()