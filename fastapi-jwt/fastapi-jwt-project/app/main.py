from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
from app.users.models import User
from app.auth.models import RefreshToken
from app.users.router import router as users_router
from app.auth.router import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="JWT Project")
app.add_middleware(SessionMiddleware, secret_key=settings.ADMIN_SECRET_KEY)

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")
        if username == settings.ADMIN_USERNAME and password == settings.ADMIN_PASSWORD:
            request.session["admin"] = "logged_in"
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return request.session.get("admin") == "logged_in"

authentication_backend = AdminAuth(secret_key=settings.ADMIN_SECRET_KEY)
admin = Admin(app, engine, authentication_backend=authentication_backend)

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.name, User.is_active, User.is_superuser]
    column_searchable_list = [User.email, User.name]
    can_create = True
    can_edit = True
    can_delete = True

class RefreshTokenAdmin(ModelView, model=RefreshToken):
    column_list = [
        RefreshToken.id,
        RefreshToken.token,
        RefreshToken.user_id,
        RefreshToken.expires_at,
        RefreshToken.is_revoked,
    ]
    can_create = False
    can_edit = False
    can_delete = True

admin.add_view(UserAdmin)
admin.add_view(RefreshTokenAdmin)

app.include_router(auth_router,  prefix="/auth",  tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])