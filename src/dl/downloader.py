import os
from time import sleep

import aria2p
import click

from . import config


def get_aria2_client():
    try:
        return aria2p.API(
            aria2p.Client(
                host=config.ARIA2_HOST,
                port=config.ARIA2_PORT,
                secret=config.ARIA2_SECRET,
            )
        )
    except Exception as e:
        raise ConnectionError(f"Failed to connect to aria2c: {e}") from e


def progress(dl):
    try:
        while not dl.is_complete:
            dl.update()
            progress_string = f"Progress: {dl.completed_length_string()}/{dl.total_length_string()} ({dl.progress_string()}), Speed: {dl.download_speed_string()}, ETA: {dl.eta_string()}            "
            print(
                progress_string,
                end="\r",
                flush=True,
            )
            sleep(config.UPDATE_INTERVAL)
    except KeyboardInterrupt:
        click.echo("\nStopping download...")
        dl.pause()

        if click.confirm(
            "Do you want to delete the incomplete file as well?", default=True
        ):
            dl.remove(force=True, files=True)
        raise


def download(url, path):
    aria2 = get_aria2_client()
    dl = aria2.add(url)[0]

    progress(dl)

    filename = dl.name
    ext = filename.split(".")[-1]

    if path is None:
        for category, exts in config.CATEGORIES.items():
            if ext in exts:
                break
        else:
            category = "misc"
        dl.move_files(os.path.join(config.DOWNLOADS_DIR, category), force=True)
    else:
        dl.move_files(path, force=True)

    dl.purge()

    click.echo(f"""
Downloaded: {click.style(filename, fg="green")}
Saved to: {click.style(path or os.path.join(config.DOWNLOADS_DIR, category), fg="green")}
    """)
