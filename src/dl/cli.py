import sys

import click

from . import downloader


@click.command()
@click.argument("url")
@click.option(
    "-p",
    "--path",
    type=click.Path(),
    default=None,
    help="Path to save the downloaded file",
)
def main(url, path):
    try:
        downloader.download(url, path)
    except ConnectionError as e:
        click.echo(click.style(f"Error: {e}", fg="red"), err=True)
        sys.exit(1)
    except KeyboardInterrupt:
        click.echo("\nDownload cancelled by user.", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
