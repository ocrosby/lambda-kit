"""
This module contains the data models for AWS Lambda functions.
"""

from pydantic import BaseModel, Field


class FunctionModel(BaseModel):
    """
    Represents an AWS Lambda function
    """

    name: str = Field(..., alias="function_name")
    source_dir: str = Field(..., alias="source_dir")
