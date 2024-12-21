import inspect
from pathlib import Path

import call_site_logging


def _format_qualname(qualname: str) -> str | None:
    if qualname == "<module>":
        return None
    elif qualname.endswith(".__init__"):
        qualname = qualname.removesuffix(".__init__")

    return qualname


def _format_filename(filepath: str, absolute: bool) -> str:
    if filepath == "<stdin>":
        return "REPL"

    elif not absolute:
        try:
            filepath = str(Path(filepath).relative_to(Path.cwd()))
        except ValueError:  # not in the subpath
            call_site_logging.getLogger().debug(
                f"Unable to determine relative filepath to {filepath}, "
                f"falling back to absolute"
            )

    return filepath


def getName(
    use_filename: bool = False, absolute_filepath: bool = False, f_back: int = 1
):
    frame = inspect.currentframe()

    for _ in range(f_back):
        frame = frame.f_back

    caller_info = inspect.getframeinfo(frame)
    caller_name = frame.f_globals["__name__"]

    file = _format_filename(caller_info.filename, absolute=absolute_filepath)
    qualfied_name = _format_qualname(frame.f_code.co_qualname)

    logger_name = ""

    if use_filename or caller_name == "__main__":
        logger_name += file
    else:
        logger_name += caller_name

    if qualfied_name:
        logger_name += ":" + qualfied_name

    return logger_name
