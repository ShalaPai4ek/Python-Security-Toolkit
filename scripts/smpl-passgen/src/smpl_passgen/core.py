"""Core password generation functions."""

import secrets
import string


def generate_password(
    length: int = 12,
    *,
    use_lowercase: bool = True,
    use_uppercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Generate a password using the system cryptographic random source.

    When enabled, each selected character class is guaranteed to appear at
    least once. The final character order is securely shuffled.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    groups = []
    if use_lowercase:
        groups.append(string.ascii_lowercase)
    if use_uppercase:
        groups.append(string.ascii_uppercase)
    if use_digits:
        groups.append(string.digits)
    if use_symbols:
        groups.append(string.punctuation)
    if not groups:
        raise ValueError("Enable at least one character group")
    if length < len(groups):
        raise ValueError(f"Length must be at least {len(groups)} for the selected character groups")

    alphabet = "".join(groups)
    password = [secrets.choice(group) for group in groups]
    password.extend(secrets.choice(alphabet) for _ in range(length - len(password)))
    secrets.SystemRandom().shuffle(password)
    return "".join(password)
