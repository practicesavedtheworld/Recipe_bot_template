from pathlib import Path
from typing import Literal, TypeAlias

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
    try:
        DEFAULT_RECIPE_IMAGE_PATH = f"{PROJECT_ROOT}/static/images/def.png"
    except FileNotFoundError:
        # TODO exception + logging
        print("FILE NOT FOUND")
except Exception as unexpected_error:
    # TODO exception + logging
    print(unexpected_error)
