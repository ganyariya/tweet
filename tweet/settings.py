import os
from typing import Final
from dotenv import load_dotenv

HOME_DIR: Final[str] = os.environ.get("HOME")
ENV_PATH: Final[str] = os.path.join(HOME_DIR, '.twitter-env')
load_dotenv(ENV_PATH)

CONSUMER_TOKEN: Final[str] = os.environ.get("CONSUMER_TOKEN")
CONSUMER_SECRET: Final[str] = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN: Final[str] = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET: Final[str] = os.environ.get("ACCESS_SECRET")
