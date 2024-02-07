import logging
import pathlib

from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

from bot.exceptions.settings_exceptions import FailedLoadSettingsException
from bot.exceptions.unexpected_exceptions import (
    StoppedByUserSignalException,
    UnexpectedException,
)
from utils.constants import PROJECT_ROOT
from utils.logger import create_logger

settings_logger = create_logger(
    loger_name="settings loader logger",
    logger_level=logging.DEBUG,
    file_info=pathlib.Path(__file__).name,
)


class Settings(BaseSettings):
    """Settings for project. If env file contain additional fields,
    this class also must contain them."""

    TELEGRAM_BOT_TOKEN: str

    DATABASE_HOST: str
    DATABASE_PORT: str

    DATABASE_HOST_TEST: str
    DATABASE_PORT_TEST: str

    # .env file has priority over .fake.env. So the first .env file will be used
    # if it exists, otherwise used .fake.env
    model_config = SettingsConfigDict(
        env_file=[f"{PROJECT_ROOT}/.fake.env", f"{PROJECT_ROOT}/.env"],
        env_file_encoding="UTF-8",
    )


try:
    settings = Settings()  # type: ignore[call-arg]
    settings_logger.debug("Settings loaded successfully!")
except ValidationError as validation_error:
    settings_logger.debug(
        f"COULD NOT LOAD SETTINGS! Check .env files, details: {validation_error}"
    )
    raise FailedLoadSettingsException(exc_details=str(validation_error))
except KeyboardInterrupt as signal_err:
    settings_logger.debug(f"Stopped by user. Details: {signal_err}")
    raise StoppedByUserSignalException(exc_details=signal_err.__repr__())
except Exception as unexpected_error:
    settings_logger.debug(f"Unexpected error. Details: {unexpected_error}")
    raise UnexpectedException(exc_details=unexpected_error.__repr__())
