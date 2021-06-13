import os
import readline
import signal
from typing import Final

import typer
import twitter
from tweet import settings
from rich.console import Console

APP_NAME: Final[str] = "tweet"

app: Final[typer.Typer] = typer.Typer()
console: Final[Console] = Console()
api: twitter.Api = twitter.Api(
    consumer_key=settings.CONSUMER_TOKEN,
    consumer_secret=settings.CONSUMER_SECRET,
    access_token_key=settings.ACCESS_TOKEN,
    access_token_secret=settings.ACCESS_SECRET,
)


def init_api() -> None:
    global api
    api = twitter.Api(
        consumer_key=settings.CONSUMER_TOKEN,
        consumer_secret=settings.CONSUMER_SECRET,
        access_token_key=settings.ACCESS_TOKEN,
        access_token_secret=settings.ACCESS_SECRET,
    )


def goodbye(*args, **kwargs) -> None:
    console.print("\n:bird: < [bold]Bye![/bold]")
    exit()


@app.command()
def tweet(status: str) -> None:
    """Tweet

    :param status: str
    :return: None
    """
    print(status)
    api.PostUpdate(status=status)


@app.command()
def endless(suffix: str = typer.Argument("")) -> None:
    """
    :return: None
    """
    while True:
        status = console.input(f":bird: < What's happening?  ")
        if len(status) == 0:
            continue
        try:
            api.PostUpdate(status=status)
            console.print(f":bird: < Tweeted! [bold]“{status} {suffix}”[/bold]\n")
        except twitter.error.TwitterError as e:
            console.print(f"[red]{e}[/red]")


if __name__ == "__main__":
    PERIOD: int = 60 * 20
    signal.signal(signal.SIGALRM, init_api)
    signal.signal(signal.SIGINT, goodbye)
    signal.signal(signal.SIGTERM, goodbye)
    signal.setitimer(signal.ITIMER_REAL, PERIOD, PERIOD)
    app()
