import logging
import pathlib

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.utils.token import TokenValidationError

from exceptions.bot_exceptions import FailedLoadBotException
from exceptions.unexpected_exceptions import (
    StoppedByUserSignalException,
    UnexpectedException,
)
from settings.settings import settings
from utils.logger import create_logger

loader_logger = create_logger(
    loger_name="loader logger",
    logger_level=logging.DEBUG,
    file_info=pathlib.Path(__file__).name,
)

try:
    dp = Dispatcher()
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)

    loader_logger.debug("Bot and Dispatcher loaded successfully!")
except TokenValidationError as token_validation_error:
    loader_logger.debug(
        f"COULD NOT LOAD BOT AND DISPATCHER! "
        f"Check .env files, details: {token_validation_error}"
    )
    raise FailedLoadBotException(exc_details=token_validation_error.__repr__())
except KeyboardInterrupt as signal_err:
    raise StoppedByUserSignalException(exc_details=signal_err.__repr__())
except Exception as unexpected_error:
    raise UnexpectedException(exc_details=unexpected_error.__repr__())
