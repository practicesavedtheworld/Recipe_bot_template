import logging

from utils.constants import LogLevel


def create_logger(
    loger_name: str,
    logger_level: int | LogLevel = logging.DEBUG,
    file_info=False,
) -> logging.Logger:
    """Create logger for handle unexpected behaviour"""

    logger = logging.getLogger(loger_name)
    logger.setLevel(logger_level)
    file_name_include = file_info if file_info else ""
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s - " + file_name_include
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
