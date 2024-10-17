"""
This module contains the data models for AWS Lambda layers.
"""

from pydantic import BaseModel, Field


class LayerModel(BaseModel):
    """
    Represents an AWS Lambda layer
    """

    name: str = Field(..., alias="layer_name")
    source_dir: str = Field(..., alias="source_dir")
