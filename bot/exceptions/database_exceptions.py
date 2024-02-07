from dataclasses import dataclass

from bot.exceptions.base import BaseRecipeBotException


@dataclass
class DatabaseIsNotActiveException(BaseRecipeBotException):
    info: str = "Database is currently not active. Are you connected?"
