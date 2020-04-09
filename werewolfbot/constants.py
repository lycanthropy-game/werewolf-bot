import base64
from os import environ


DEPLOY = bool(environ.get("DEPLOY"))


def getenv(name: str, fallback: str = "") -> str:
    """Return an (optionally base64-encoded) env var."""
    variable = environ.get(name)
    if DEPLOY and variable is not None:
        variable = base64.b64decode(variable).decode()
    return variable or fallback


BOT_TOKEN = getenv("BOT_TOKEN")
