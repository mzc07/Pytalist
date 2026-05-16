import argparse
import pathlib


def build_parser():
    parser_global = argparse.ArgumentParser(
        prog="pytalist", description="CSV analyzer tool", epilog="version: 0.1"
    )

    parser_global.add_argument(
        "archivo", type=pathlib.Path, help="Archivo utilizado para el flow del proyecto"
    )

    parser_global.add_argument(
        "--output", action="store", default="results.txt", help="Salida del archivo"
    )

    return parser_global


def main():
    parser = build_parser()


if __name__ == "__main__":
    main()
