class TombaException(Exception):
    """Exception raised for Tomba API errors.

    Attributes:
        message: Human-readable error description.
        code: HTTP status code (0 if not from an HTTP response).
        response: Full API error response body, if available.
    """

    def __init__(self, message, code=0, response=None):
        self.message = message
        self.code = code
        self.response = response
        super().__init__(self.message)
