from dataclasses import dataclass

from bot.exceptions.base import BaseRecipeBotException


@dataclass
class UnexpectedException(BaseRecipeBotException):
    info: str = "Stopped due to unexpected error. Details: "


@dataclass
class StoppedByUserSignalException(BaseRecipeBotException):
    info: str = "Stopped by user. Details: "
