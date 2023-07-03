from requests import post
from .exceptions import *

class Client:
  def __init__(self, api_key: str) -> None:
    self.api_key = api_key
  def postMessage(self, message: str, pfp_url: str | None = None) -> None:
    r = post("https://chat.element1010.repl.co/api/post", json={
      "apiKey": self.api_key,
      "pfp": pfp_url,
      "message": message
    })
