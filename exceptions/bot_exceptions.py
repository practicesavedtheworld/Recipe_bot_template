from dataclasses import dataclass

from exceptions.base import BaseRecipeBotException


@dataclass
class FailedLoadBotException(BaseRecipeBotException):
    info: str = "Failed to load bot. WRONG TOKEN or TOKEN FORMAT. CHECK IT"
