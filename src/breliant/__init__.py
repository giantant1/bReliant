# pragma: no cover
from os import environ

from breliant.__about__ import __version__, _about
from breliant.context import Context
from breliant.logger import LoggingFactory
from breliant.models import BaseModel, ExtraParamsMixin
from breliant.steps import Step, StepOutput
from breliant.utils import convert_str_to_bool

_breliant_print_logo = convert_str_to_bool(environ.get("breliant__PRINT_LOGO", "True"))
_logo_printed = False
ABOUT = _about()
VERSION = __version__

__all__ = [
    "ABOUT",
    "BaseModel",
    "Context",
    "ExtraParamsMixin",
    "LoggingFactory",
    "Step",
    "StepOutput",
    "VERSION",
]


def print_logo() -> None:
    global _logo_printed
    global _breliant_print_logo

    if not _logo_printed and _breliant_print_logo:
        print(ABOUT)
        _logo_printed = True


print_logo()
