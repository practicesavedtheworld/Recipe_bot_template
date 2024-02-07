from dataclasses import dataclass

from bot.exceptions.base import BaseRecipeBotException


@dataclass
class FailedLoadSettingsException(BaseRecipeBotException):
    info: str = "Failed to load settings. WRONG FORMAT of .env files. CHECK IT"
