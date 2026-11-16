# Python Security Toolkit

A small collection of practical Python security utilities. The repository currently contains:

- **smpl-hasher** — calculate file hashes and verify files against saved digests.
- **smpl-passgen** — generate cryptographically secure random passwords.

Both tools support Python 3.10+ and have no runtime third-party dependencies.

## Install the whole toolkit

Install the toolkit directly from GitHub:

```bash
python -m pip install "git+https://github.com/ShalaPai4ek/Python-Security-Toolkit.git"
```

For an isolated command-line installation, use `pipx`:

```bash
pipx install "git+https://github.com/ShalaPai4ek/Python-Security-Toolkit.git"
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

You can install each tool from its own directory:

```bash
python -m pip install ./scripts/smpl-hasher
python -m pip install ./scripts/smpl-passgen
```

You can also install them directly from GitHub using `pipx`:

```bash
pipx install "git+https://github.com/ShalaPai4ek/Python-Security-Toolkit.git#subdirectory=scripts/smpl-hasher"

pipx install "git+https://github.com/ShalaPai4ek/Python-Security-Toolkit.git#subdirectory=scripts/smpl-passgen"
```

## Development and tests

Clone the repository:

```bash
git clone https://github.com/ShalaPai4ek/Python-Security-Toolkit.git
cd Python-Security-Toolkit
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project in editable mode and install the testing tool:

```bash
python -m pip install -e .
python -m pip install pytest
```

Run the tests:

```bash
python -m pytest
```

Editable mode (`-e`) allows you to modify the source code without reinstalling the package after every change.

## Security notes

- Passwords are generated with Python's `secrets` module, backed by the operating system's secure random source.
- Enabled character groups are guaranteed to appear in each generated password.
- File hashing reads data in bounded chunks, so large files do not need to fit in memory.
