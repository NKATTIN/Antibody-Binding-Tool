from argparse import ArgumentParser

from ._version import __version__

__all__ = ["main"]


def main(args=None):
    parser = ArgumentParser()
    parser.add_argument("--version", action="version", version=__version__)
    args = parser.parse_args(args)


if __name__ == "__main__":
    main()