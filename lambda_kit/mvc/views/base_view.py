from abc import ABC, abstractmethod
from typing import Callable, Optional


class BaseView(ABC):
    """
    Abstract base class for views.
    """

    def __init__(
        self, info: Callable[[str], None], error: Optional[Callable[[str], None]] = None
    ):
        """
        Initialize a new BaseView object.
        """
        self.info_display_func = info
        self.error_display_func = error

    @abstractmethod
    def info(self, message: str) -> None:
        """
        Render an informational message.
        """

    @abstractmethod
    def error(self, message: str) -> None:
        """
        Render an error message.
        """

    def render_message(self, message: str, is_error: bool = False) -> None:
        """
        Render a message.
        """
        if is_error and self.error_display_func is not None:
            self.error_display_func(message)
        else:
            self.info_display_func(message)
