#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review."""
    place_id = ""  # Add these attributes
    user_id = ""
    text = ""
