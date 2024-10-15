"""
This module contains a view for the LayerController class.
"""

from lambda_kit.mvc.views.base_view import BaseView


class LayerView(BaseView):
    """
    The LayerView class renders the output of the LayerController class.
    """

    def info(self, message: str) -> None:
        """
        Render the output of the LayerController class.
        """
        self.render_message(message, is_error=False)

    def error(self, message: str) -> None:
        """
        Render an error message.
        """
        self.render_message(message, is_error=True)
