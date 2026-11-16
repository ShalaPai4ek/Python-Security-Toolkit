"""Command-line interface for smpl-passgen."""

import argparse

from .core import generate_password


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="smpl-passgen", description="Generate secure random passwords.")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length (default: 16)")
    parser.add_argument("--no-lowercase", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude punctuation symbols")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        print(generate_password(
            args.length,
            use_lowercase=not args.no_lowercase,
            use_uppercase=not args.no_uppercase,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
        ))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
