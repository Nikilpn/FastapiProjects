import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.session import SessionLocal
from app.db.base import Base
from app.db.session import engine
from app.users.models import User
from app.core.security import hash_password

Base.metadata.create_all(bind=engine)

print("=== Create Superuser ===")
email    = input("Email: ")
name     = input("Name: ")
password = input("Password: ")

db = SessionLocal()

# Check if already exists
existing = db.query(User).filter(User.email == email).first()
if existing:
    print(f"Error: {email} already exists!")
    db.close()
    sys.exit(1)

user = User(
    email=email,
    name=name,
    password=hash_password(password),
    is_active=True,
    is_superuser=True
)
db.add(user)
db.commit()
db.refresh(user)
print(f"Superuser created successfully: {user.email}")
db.close()