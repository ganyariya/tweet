from typing import Final

import typer
import twitter
from tweet import settings

APP_NAME: Final[str] = 'tweet'
app: Final[typer.Typer] = typer.Typer()
api: Final[twitter.Api] = twitter.Api(consumer_key=settings.CONSUMER_TOKEN, consumer_secret=settings.CONSUMER_SECRET, access_token_key=settings.ACCESS_TOKEN, access_token_secret=settings.ACCESS_SECRET)


@app.command()
def tweet(status: str):
    """ツイートする.

    :param status: str
    :return: None
    """
    api.PostUpdate(status=status)


if __name__ == '__main__':
    app()
