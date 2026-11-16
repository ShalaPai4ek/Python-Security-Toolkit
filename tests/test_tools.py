import hashlib
import pytest

from smpl_hasher import calculate_hash, compare_hash
from smpl_passgen import generate_password


def test_hash_file(tmp_path):
    target = tmp_path / "hello.txt"
    target.write_bytes(b"hello world")
    assert calculate_hash(target) == hashlib.sha256(b"hello world").hexdigest()


def test_hash_chunk_size(tmp_path):
    target = tmp_path / "data.bin"
    target.write_bytes(b"abc" * 1000)
    assert calculate_hash(target, "sha512", 17) == hashlib.sha512(target.read_bytes()).hexdigest()


def test_compare_hash_plain_and_sum_format(tmp_path):
    target = tmp_path / "data.txt"
    target.write_text("content")
    digest = hashlib.sha256(b"content").hexdigest()
    expected = tmp_path / "data.sha256"
    expected.write_text(f"{digest}  data.txt\n")
    assert compare_hash(target, expected)
    expected.write_text("0" * 64)
    assert not compare_hash(target, expected)


def test_hash_rejects_bad_chunk_and_algorithm(tmp_path):
    target = tmp_path / "file"
    target.write_text("x")
    with pytest.raises(ValueError):
        calculate_hash(target, chunk=0)
    with pytest.raises(ValueError):
        calculate_hash(target, algo="not-a-real-hash")


def test_password_length_and_character_groups():
    password = generate_password(40)
    assert len(password) == 40
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in __import__("string").punctuation for c in password)


def test_password_custom_groups():
    password = generate_password(20, use_uppercase=False, use_symbols=False)
    assert len(password) == 20
    assert password.islower() or password.isdigit() or all(c.islower() or c.isdigit() for c in password)
    assert not any(c in __import__("string").punctuation for c in password)


def test_password_rejects_invalid_options():
    with pytest.raises(ValueError):
        generate_password(0)
    with pytest.raises(ValueError):
        generate_password(2)
    with pytest.raises(ValueError):
        generate_password(10, use_lowercase=False, use_uppercase=False, use_digits=False, use_symbols=False)
