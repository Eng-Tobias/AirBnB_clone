#!/usr/bin/python3
"""
BaseModel class module
"""
import uuid
from datetime import datetime

class BaseModel:
    """Represents the base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel object"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue  # Skip the __class__ key
                if key in ("created_at", "updated_at"):
                    # Convert string to datetime object
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """String representation of the BaseModel"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
