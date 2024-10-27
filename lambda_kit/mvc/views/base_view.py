from abc import ABC, abstractmethod


class BaseView(ABC):
    """
    Abstract base class for views.
    """

    def __init__(self) -> None:
        self.info_display_func = print
        self.error_display_func = print

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
