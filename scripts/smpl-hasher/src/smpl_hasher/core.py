"""Core file hashing functions."""

from __future__ import annotations

import hashlib
import hmac
from pathlib import Path

DEFAULT_ALGORITHM = "sha256"
DEFAULT_CHUNK_SIZE = 1024 * 64


def _validate(path: str | Path, chunk_size: int) -> Path:
    file_path = Path(path).expanduser()
    if chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer")
    if not file_path.exists():
        raise FileNotFoundError(f"File does not exist: {file_path}")
    if not file_path.is_file():
        raise IsADirectoryError(f"Not a regular file: {file_path}")
    return file_path


def calculate_hash(
    path_file: str | Path,
    algo: str = DEFAULT_ALGORITHM,
    chunk: int = DEFAULT_CHUNK_SIZE,
) -> str:
    """Return the hexadecimal digest of a file, reading it in chunks."""
    file_path = _validate(path_file, chunk)
    try:
        digest = hashlib.new(algo)
    except (ValueError, TypeError) as exc:
        available = ", ".join(sorted(hashlib.algorithms_available))
        raise ValueError(f"Unsupported hash algorithm {algo!r}. Available: {available}") from exc

    with file_path.open("rb") as file:
        for data in iter(lambda: file.read(chunk), b""):
            digest.update(data)
    return digest.hexdigest()


def read_expected_hash(hash_file: str | Path) -> str:
    """Read a digest from a plain text file or a standard *sum output file."""
    path = Path(hash_file).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"Hash file does not exist: {path}")
    if not path.is_file():
        raise IsADirectoryError(f"Not a regular hash file: {path}")
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        raise ValueError("Hash file is empty")
    # Supports both a bare digest and lines such as: <digest>  filename
    return content.splitlines()[0].split()[0].lower()


def compare_hash(
    path_file: str | Path,
    path_hash: str | Path,
    algo: str = DEFAULT_ALGORITHM,
    chunk: int = DEFAULT_CHUNK_SIZE,
) -> bool:
    """Compare a file's digest with the digest stored in another file."""
    expected = read_expected_hash(path_hash)
    actual = calculate_hash(path_file, algo, chunk)
    if len(expected) != len(actual):
        return False
    return hmac.compare_digest(actual.lower(), expected)
