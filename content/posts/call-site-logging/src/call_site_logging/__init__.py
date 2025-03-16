from logging import *  # noqa:F403 , provided as drop-in replacement for logging
from logging import getLogger as _logging_getLogger
from .context import getName


def getLogger(
    name: str | None = None, use_filename: bool = False, absolute_filepath: bool = False
) -> Logger:  # noqa:F405
    logger = _logging_getLogger(
        getName(
            use_filename=use_filename, absolute_filepath=absolute_filepath, f_back=2
        )
    )
    if name:
        logger = logger.getChild(name)
    return logger
