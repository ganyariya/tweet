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
        status = console.input(f":bird: < What's happening?  ")
        if len(status) == 0:
            continue
        try:
            api.PostUpdate(status=status)
            console.print(f":bird: < Tweeted! [bold]“{status}”[/bold]")
        except twitter.error.TwitterError as e:
            console.print(f"[red]{e}[/red]")


def init() -> None:
    global api
    api = twitter.Api(
        consumer_key=settings.CONSUMER_TOKEN,
        consumer_secret=settings.CONSUMER_SECRET,
        access_token_key=settings.ACCESS_TOKEN,
        access_token_secret=settings.ACCESS_SECRET,
    )


if __name__ == "__main__":
    PERIOD: int = 60 * 20
    signal.signal(signal.SIGALRM, init)
    signal.setitimer(signal.ITIMER_REAL, PERIOD, PERIOD)
    app()
