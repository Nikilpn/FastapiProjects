from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings

client = TestClient(app)


def test_auth_routes_registered():
    all_paths = {route.path for route in app.routes}
    assert "/auth/login" in all_paths
    assert "/auth/refresh" in all_paths
    assert "/auth/logout" in all_paths
    assert "/users/register" in all_paths


def test_settings_are_loaded():
    assert settings.DATABASE_URL
    assert settings.SECRET_KEY
