"""
This module contains a view for the FunctionController class.
"""

from lambda_kit.mvc.views.base_view import BaseView


class FunctionView(BaseView):
    """
    The FunctionView class renders the output of the FunctionController class.
    """

    def info(self, message: str) -> None:
        """
        Render the output of the FunctionController class.
        """
        self.render_message(message, False)

    def error(self, message: str) -> None:
        """
        Render the error of the FunctionController class.

        :param message: The message to display.
        """
        self.render_message(message, True)
