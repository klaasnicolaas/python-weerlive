"""Asynchronous Python client for Weerlive."""


class WeerliveError(Exception):
    """General exception for Weerlive."""


class WeerliveConnectionError(WeerliveError):
    """Weerlive connection exception."""


class WeerliveAuthenticationError(WeerliveError):
    """Weerlive authentication exception."""


class WeerliveRateLimitError(WeerliveError):
    """Weerlive rate limit exception."""
