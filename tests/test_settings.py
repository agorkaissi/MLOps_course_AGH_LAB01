import pytest
from settings import Settings


def test_settings_load():
    settings = Settings(ENVIRONMENT="test", APP_NAME="LAB01", API_KEY="test_key")
    assert settings.ENVIRONMENT == "test"


def test_valid_environments():
    for env in ["dev", "test", "prod"]:
        settings = Settings(ENVIRONMENT=env, APP_NAME="X", API_KEY="key")
        assert settings.ENVIRONMENT == env


def test_invalid_environment():
    with pytest.raises(ValueError):
        Settings(ENVIRONMENT="ddev", APP_NAME="X", API_KEY="key")


def test_missing_api_key():
    with pytest.raises(Exception):
        Settings(
            ENVIRONMENT="test",
            APP_NAME="LAB01",
            # no API_KEY
        )
