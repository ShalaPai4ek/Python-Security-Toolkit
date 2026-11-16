# smpl-hasher

Calculate and verify cryptographic hashes of files. Supports algorithms provided by Python's `hashlib` (for example SHA-256 and SHA-512).

## Install

```bash
python -m pip install .
# or: pipx install .
```

## Examples

```bash
smpl-hasher ./file.zip
smpl-hasher ./file.zip --check ./file.sha256
smpl-hasher ./file.zip --algorithm sha512 --size 131072
```

The check file may contain a bare hexadecimal digest or a standard `sha256sum`-style line (`<digest>  filename`). Exit status is `0` for success, `1` for a mismatch, and `2` for invalid input or I/O errors.

Run `smpl-hasher --help` for all options. The Python API is available as `smpl_hasher.calculate_hash()` and `smpl_hasher.compare_hash()`.
