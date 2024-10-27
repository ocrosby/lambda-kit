"""
This module contains the data models for AWS Lambda layers.
"""

from typing import Optional

from pydantic import BaseModel, Field


class LayerModel(BaseModel):
    """
    Represents an AWS Lambda layer
    """

    name: Optional[str] = Field(default=None, alias="name")
    source_dir: Optional[str] = Field(default=None, alias="source_dir")
    output_dir: Optional[str] = Field(default=None, alias="output_dir")
