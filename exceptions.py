class APIKeyError(Exception):
  """
  An error for when a given API key is bad.
  """

class XSSDetectedError(Exception):
  """
  An error for when XSS is detected in a message.
  """

class OwnerBannedError(Exception):
  """
  An error for when the owner of an API key is banned.
  """
