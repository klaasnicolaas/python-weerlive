"""Auth tests for Weerlive."""
# pylint: disable=protected-access
import pytest
from aiohttp import ClientSession
from aresponses import ResponsesMockServer

from weerlive import Weerlive
from weerlive.exceptions import WeerliveAuthenticationError, WeerliveRateLimitError

from . import load_fixtures


async def test_missing_api_key(aresponses: ResponsesMockServer) -> None:
    """Test missing API key."""
    aresponses.add(
        "weerlive.nl",
        "/api/json-data-10min.php",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("weather.json"),
        ),
    )
    async with ClientSession() as session:
        client = Weerlive(
            api_key="",
            longitude=66.6699498,
            latitude=26.0317749,
            session=session,
        )
        with pytest.raises(WeerliveAuthenticationError):
            await client.weather()


async def test_invalid_api_key(aresponses: ResponsesMockServer) -> None:
    """Test invalid API key."""
    aresponses.add(
        "weerlive.nl",
        "/api/json-data-10min.php",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("error_auth.txt"),
        ),
    )
    async with ClientSession() as session:
        client = Weerlive(
            api_key="invalid",
            longitude=66.6699498,
            latitude=26.0317749,
            session=session,
        )
        with pytest.raises(WeerliveAuthenticationError):
            await client.weather()


async def test_rate_limit(aresponses: ResponsesMockServer) -> None:
    """Test rate limit."""
    aresponses.add(
        "weerlive.nl",
        "/api/json-data-10min.php",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("error_rate_limit.txt"),
        ),
    )
    async with ClientSession() as session:
        client = Weerlive(
            api_key="test",
            longitude=66.6699498,
            latitude=26.0317749,
            session=session,
        )
        with pytest.raises(WeerliveRateLimitError):
            await client.weather()
