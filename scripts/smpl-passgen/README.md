# smpl-passgen

Generate cryptographically secure random passwords using Python's `secrets` module.

## Install

```bash
python -m pip install .
# or: pipx install .
```

## Examples

```bash
smpl-passgen
smpl-passgen --length 24
smpl-passgen --length 20 --no-symbols
smpl-passgen --length 18 --no-digits --no-symbols
```

Lowercase, uppercase, digits, and symbols are enabled by default. Every enabled group is guaranteed to appear at least once. Run `smpl-passgen --help` for all options.
