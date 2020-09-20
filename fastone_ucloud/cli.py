"""Console script for fastone_ucloud."""
from __future__ import print_function
import sys
import click


@click.command()
def main(args=None):
    """Console script for fastone_ucloud."""
    click.echo("Replace this message by putting your code into "
               "fastone_ucloud.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


@click.command(name="hello")
def hello():
    """Simple hello world command for demo purpose"""
    click.echo("Hello fastone_ucloud")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
