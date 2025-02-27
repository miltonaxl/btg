""" util index file for the app """


from typing import Optional, Any
import re
from bson import ObjectId


def normalize_and_convert_ids(data: Any) -> Any:
    """
    Recursively normalizes '_id' fields and converts all 'id' values to strings:
    - Renames '_id' to 'id'.
    - If 'id' is None but '_id' exists, replace 'id' with '_id'.
    - Converts any 'id' or '*_id' values to strings.
    
    Args:
        data (Any): Input data (dict, list, or other types).
    
    Returns:
        Any: Processed data with normalized 'id' fields.
    """
    if isinstance(data, dict):
        processed = {
            ("id" if key == "_id" else key): normalize_and_convert_ids(value)
            for key, value in data.items()
        }

        if processed.get("id") is None and "_id" in data:
            processed["id"] = str(data["_id"])
        for key in processed:
            if key.endswith("_id") or key == "id":
                processed[key] = str(processed[key])

        return processed

    elif isinstance(data, list):
        return [normalize_and_convert_ids(item) for item in data]

    return data


def clean_and_format_string(text: str) -> str:
    """
    Replaces underscores, hyphens, and dots with spaces in a string.

    Args:
        text (str): The input string.

    Returns:
        str: The formatted string with spaces instead of _, -, and .
    """
    return re.sub(r"[_\-.]", " ", text)


def format_number(value: float) -> str:
    """
    Formats a number to a custom string format where:
    - Thousands are separated by a dot.
    - Decimal places are always two digits.
    
    Args:
        value (float): The number to format.

    Returns:
        str: The formatted number as a string.
    """
    if value == int(value):
        value = int(value)
    
    integer_part, decimal_part = f"{value:.2f}".split(".")
    
    formatted_integer = f"{int(integer_part):,}".replace(",", ".")
    
    return f"{formatted_integer}.{decimal_part}"


class PyObjectId(ObjectId):
    """Clase para permitir ObjectId en Pydantic."""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any):
        if not isinstance(v, ObjectId):
            raise ValueError("Invalid ObjectId")
        return str(v)


