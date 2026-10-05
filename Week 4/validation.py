"""Validation rules for student marks."""


def validate_mark(mark):
    """Return True when mark is between 0 and 100 inclusive."""
    return 0 <= mark <= 100
