"""Test the models for Weerlive."""

from __future__ import annotations

from typing import TYPE_CHECKING

from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from . import load_fixtures

if TYPE_CHECKING:
    from weerlive import Weather, Weerlive


async def test_weather_data(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    weerlive_client: Weerlive,
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
    weather: Weather = await weerlive_client.weather()
    assert weather == snapshot

    assert weather.to_json() == snapshot
    assert weather.alarm is False
    assert weather.alarm_message is None


async def test_weather_alarm_data(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    weerlive_client: Weerlive,
) -> None:
    """Test weather data function."""
    aresponses.add(
        "weerlive.nl",
        "/api/json-data-10min.php",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("weather_alarm.json"),
        ),
    )
    weather: Weather = await weerlive_client.weather()
    assert weather == snapshot
    assert weather.to_json() == snapshot
    assert weather.alarm is True
