"""
This module contains the data models for AWS Lambda functions.
"""

from pydantic import BaseModel, Field


class FunctionModel(BaseModel):
    """
    Represents an AWS Lambda function
    """

    name: str = Field(..., alias="name")
    source_dir: str = Field(..., alias="source_dir")
    output_dir: str = Field(..., alias="output_dir")
