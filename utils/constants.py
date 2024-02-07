import logging
import os.path
from pathlib import Path
from typing import Literal, TypeAlias

from bot.exceptions.bot_exceptions import StaticFileNotFoundException
from bot.exceptions.unexpected_exceptions import UnexpectedException
from utils.logger import create_logger

constants_logger = create_logger(
    loger_name="constants logger",
    logger_level=logging.ERROR,
    file_info=Path(__file__).name,
)

try:
    LogLevel: TypeAlias = Literal[
        "NOTSET",
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ]
    PROJECT_ROOT: Path = Path(__file__).parent.parent
    DEFAULT_RECIPE_IMAGE_PATH = f"{PROJECT_ROOT}/bot/static/images/def.png"
    if not os.path.exists(DEFAULT_RECIPE_IMAGE_PATH):
        constants_logger.error(
            f"Some file not found. Path: {DEFAULT_RECIPE_IMAGE_PATH}"
        )
        raise StaticFileNotFoundException(
            exc_details=f"{DEFAULT_RECIPE_IMAGE_PATH} doesn't exist"
        )
except Exception as unexpected_error:
    constants_logger.error(f"Unexpected error. Details: {str(unexpected_error)}")
    raise UnexpectedException(exc_details=str(unexpected_error))
