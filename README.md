# Python Security Toolkit

A small collection of practical Python security utilities. The repository currently contains:

- **smpl-hasher** — calculate file hashes and verify files against saved digests.
- **smpl-passgen** — generate cryptographically secure random passwords.

Both tools support Python 3.10+ and have no runtime third-party dependencies.

## Install the whole toolkit

From the repository root:

```bash
python -m pip install https://github.com/ShalaPai4ek/Python-Security-Toolkit.git
```

For an isolated command-line installation, use `pipx`:

```bash
pipx install https://github.com/ShalaPai4ek/Python-Security-Toolkit.git
```

## Use the tools

```bash
# Generate a SHA-256 digest
smpl-hasher ./archive.zip

# Verify against a file containing a digest (plain digest or sha256sum format)
smpl-hasher ./archive.zip --check ./archive.sha256

# Select an algorithm and chunk size
smpl-hasher ./archive.zip --algorithm sha512 --size 131072

# Generate a 24-character password
smpl-passgen --length 24

# Generate without punctuation
smpl-passgen --length 20 --no-symbols
```

## Install tools separately

```bash
python -m pip install ./scripts/smpl-hasher
python -m pip install ./scripts/smpl-passgen
```

## Development and tests

```bash
python -m pip install -e https://github.com/ShalaPai4ek/Python-Security-Toolkit.git pytest
python -m pytest
```

## Security notes

- Passwords are generated with Python's `secrets` module, backed by the operating system's secure random source.
- Enabled character groups are guaranteed to appear in each generated password.
- File hashing reads data in bounded chunks, so large files do not need to fit in memory.
