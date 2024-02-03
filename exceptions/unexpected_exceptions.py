from dataclasses import dataclass

from exceptions.base import BaseRecipeBotException


@dataclass
class UnexpectedException(BaseRecipeBotException):
    info: str = "Stopped due to unexpected error. Details: "


@dataclass
class StoppedByUserSignalException(BaseRecipeBotException):
    info: str = "Stopped by user. Details: "
