"""Cryptographically secure password generation."""

__version__ = "1.1.0"

from .core import generate_password

__all__ = ["generate_password", "__version__"]
