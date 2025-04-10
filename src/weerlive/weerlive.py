"""Asynchronous Python client for Weerlive."""

from __future__ import annotations

import asyncio
import socket
from dataclasses import dataclass
from importlib import metadata
from typing import Any, Self

from aiohttp import ClientError, ClientSession
from aiohttp.hdrs import METH_GET
from yarl import URL

from .exceptions import (
    WeerliveAuthenticationError,
    WeerliveConnectionError,
    WeerliveError,
    WeerliveRateLimitError,
)
from .models import Weather

VERSION = metadata.version(__package__)


@dataclass
class Weerlive:
    """Main class for handling connections with the Weerlive API."""

    api_key: str
    latitude: float
    longitude: float
    request_timeout: float = 10.0
    session: ClientSession | None = None

    _close_session: bool = False

    async def _request(
        self,
        uri: str,
        *,
        method: str = METH_GET,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Handle a request to the Weerlive API.

        Args:
        ----
            uri: Request URI, without '/api/', for example, 'status'.
            method: HTTP method to use.
            params: Extra options to improve or limit the response.

        Returns:
        -------
            A Python dictionary (JSON decoded) with the response from
            the Weerlive API.

        Raises:
        ------
            WeerliveAuthenticationError: If the API key is invalid.
            WeerliveConnectionError: An error occurred while communicating
                with the Weerlive API.
            WeerliveError: Received an unexpected response from the Weerlive API.

        """
        url = URL.build(scheme="https", host="weerlive.nl", path="/api/").join(URL(uri))

        headers = {
            "Accept": "application/json",
            "User-Agent": f"PythonWeerlive/{VERSION}",
        }

        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        if self.api_key is None or self.api_key == "":
            msg = "No API key provided"
            raise WeerliveAuthenticationError(msg)

        try:
            async with asyncio.timeout(self.request_timeout):
                response = await self.session.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                    ssl=True,
                )
                response.raise_for_status()
        except TimeoutError as exception:
            msg = "Timeout occurred while connecting to the Weerlive API."
            raise WeerliveConnectionError(msg) from exception
        except (ClientError, socket.gaierror) as exception:
            msg = "Error occurred while communicating with the Weerlive API."
            raise WeerliveConnectionError(msg) from exception

        # The API does not use status codes for error handling
        # Errors are therefore still returned with status 200
        response_text = await response.text()
        if "Vraag eerst een API-key op" in response_text:
            msg = "The given API key is invalid"
            raise WeerliveAuthenticationError(msg)
        if "Dagelijkse limiet" in response_text:
            msg = "The API rate limit has been exceeded"
            raise WeerliveRateLimitError(msg)

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            msg = "Unexpected content type response from the Weerlive API"
            raise WeerliveError(
                msg,
                {"Content-Type": content_type, "response": response_text},
            )

        return await response.json()

    async def weather(self) -> Weather:
        """Get the current weather forecast.

        Returns
        -------
            A Weather data object from the API.

        """
        data = await self._request(
            "json-data-10min.php",
            params={
                "key": self.api_key,
                "locatie": f"{self.latitude},{self.longitude}",
            },
        )
        return Weather.from_dict(data["liveweer"][0])

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> Self:
        """Async enter.

        Returns
        -------
            The Weerlive object.

        """
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.

        """
        await self.close()
