from requests import get, post

class Client:
  def __init__(self, api_key: str) -> None:
    self.api_key = api_key
  def getTheme(self, user: str) -> str:
    data = post("https://chat.element1010.repl.co/api/get-theme", json={
      "apiKey": self.api_key,
      "user": user
    })
    if data.status_code != 200:
      data.raise_for_status()
    data = data.json()
