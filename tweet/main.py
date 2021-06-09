import readline
from os import stat
from typing import Final
from rich.console import Console

import typer
import twitter
from tweet import settings

APP_NAME: Final[str] = 'tweet'
app: Final[typer.Typer] = typer.Typer()
api: Final[twitter.Api] = twitter.Api(consumer_key=settings.CONSUMER_TOKEN, consumer_secret=settings.CONSUMER_SECRET, access_token_key=settings.ACCESS_TOKEN, access_token_secret=settings.ACCESS_SECRET)
console: Final[Console] = Console()


@app.command()
def tweet(status: str) -> None:
    """Tweet

    :param status: str
    :return: None
    """
    print(status)
    api.PostUpdate(status=status)

@app.command()
def endless() -> None:
    """
    :return: None
    """
    while True:
        status = console.input(f':bird: < What\'s happening?  ')
        if len(status) == 0:
            continue
        api.PostUpdate(status=status)
        console.print(f':bird: < Tweeted! [bold]“{status}”[/bold]')


if __name__ == '__main__':
    app()
