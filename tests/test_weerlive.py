"""Basic tests for Weerlive."""
# pylint: disable=protected-access
import asyncio
from unittest.mock import patch

import pytest
from aiohttp import ClientError, ClientResponse, ClientSession
from aresponses import Response, ResponsesMockServer

from weerlive import Weerlive
from weerlive.exceptions import WeerliveConnectionError, WeerliveError

from . import load_fixtures


async def test_json_request(aresponses: ResponsesMockServer) -> None:
    """Test JSON response is handled correctly."""
    aresponses.add(
        "weerlive.nl",
        "/api/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("weather.json"),
        ),
    )
    async with ClientSession() as session:
        client = Weerlive(
            api_key="test",
            longitude=66.6699498,
            latitude=26.0317749,
            session=session,
        )
        response = await client._request("test")
        assert response is not None
        await client.close()


async def test_internal_session(aresponses: ResponsesMockServer) -> None:
    """Test internal session is handled correctly."""
    aresponses.add(
        "weerlive.nl",
        "/api/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("weather.json"),
        ),
    )
    async with Weerlive(
        api_key="test",
        longitude=66.6699498,
        latitude=26.0317749,
    ) as client:
        await client._request("test")


async def test_timeout(aresponses: ResponsesMockServer) -> None:
    """Test request timeout from the Weerlive API."""

    # Faking a timeout by sleeping
    async def response_handler(_: ClientResponse) -> Response:
        await asyncio.sleep(0.2)
        return aresponses.Response(
            body="Goodmorning!",
            text=load_fixtures("weather.json"),
        )

    aresponses.add(
        "weerlive.nl",
        "/api/test",
        "GET",
        response_handler,
    )

    async with ClientSession() as session:
        client = Weerlive(
            api_key="test",
            longitude=66.6699498,
            latitude=26.0317749,
            session=session,
            request_timeout=0.1,
        )
        with pytest.raises(WeerliveConnectionError):
            await client._request("test")


async def test_content_type(aresponses: ResponsesMockServer) -> None:
    """Test content type is handled correctly."""
    aresponses.add(
        "weerlive.nl",
        "/api/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "text/html"},
            text=load_fixtures("weather.json"),
        ),
    )
    async with ClientSession() as session:
        client = Weerlive(
            api_key="test",
            longitude=66.6699498,
            latitude=26.0317749,
            session=session,
        )
        with pytest.raises(WeerliveError):
            assert await client._request("test")


async def test_client_error() -> None:
    """Test client error is handled correctly."""
    async with ClientSession() as session:
        client = Weerlive(
            api_key="test",
            longitude=66.6699498,
            latitude=26.0317749,
            session=session,
        )
        with patch.object(
            session,
            "request",
            side_effect=ClientError,
        ), pytest.raises(WeerliveConnectionError):
            assert await client._request("test")
