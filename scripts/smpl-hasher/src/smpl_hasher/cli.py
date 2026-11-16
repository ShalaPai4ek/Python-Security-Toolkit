"""Command-line interface for smpl-hasher."""

import argparse
import sys

from .core import DEFAULT_ALGORITHM, DEFAULT_CHUNK_SIZE, calculate_hash, compare_hash


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="smpl-hasher",
        description="Calculate and verify cryptographic file hashes.",
    )
    parser.add_argument("path", help="Path to the file to hash")
    parser.add_argument("-c", "--check", metavar="HASH_FILE", help="Verify against a digest text file")
    parser.add_argument("-a", "--algorithm", "--algorythm", default=DEFAULT_ALGORITHM,
                        help=f"Hash algorithm (default: {DEFAULT_ALGORITHM})")
    parser.add_argument("-s", "--size", type=int, default=DEFAULT_CHUNK_SIZE,
                        help=f"Read chunk size in bytes (default: {DEFAULT_CHUNK_SIZE})")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.check:
            valid = compare_hash(args.path, args.check, args.algorithm, args.size)
            if valid:
                print("OK: hashes match")
            else:
                print("ERROR: hashes do not match", file=sys.stderr)
                raise SystemExit(1)
        else:
            print(calculate_hash(args.path, args.algorithm, args.size))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"{parser.prog}: error: {exc}\n")


if __name__ == "__main__":
    main()
