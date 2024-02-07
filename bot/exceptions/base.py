from dataclasses import dataclass


@dataclass
class BaseRecipeBotException(BaseException):
    info: str = "exc information"
    exc_details: str = ""

    def __repr__(self) -> str:
        return self.info + "\n" + self.exc_details

    def __str__(self) -> str:
        return self.__repr__()
