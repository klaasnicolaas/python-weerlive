"""Test the models for Weerlive."""
from __future__ import annotations

from aiohttp import ClientSession
from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from weerlive import Weather, Weerlive

from . import load_fixtures


async def test_weather_data(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
) -> None:
    """Test weather data function."""
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
            api_key="test",
            longitude=66.6699498,
            latitude=26.0317749,
            session=session,
        )
        weather: Weather = await client.weather()
        assert weather == snapshot
        assert weather.to_json() == snapshot
