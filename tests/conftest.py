"""Fixture for the Weerlive tests."""

from collections.abc import AsyncGenerator

import pytest
from aiohttp import ClientSession

from weerlive import Weerlive


@pytest.fixture(name="weerlive_client")
async def client() -> AsyncGenerator[Weerlive, None]:
    """Return an Weerlive client."""
    async with (
        ClientSession() as session,
        Weerlive(
            api_key="Fake API key",
            longitude=52.1015832,
            latitude=5.1785422,
            session=session,
        ) as weerlive_client,
    ):
        yield weerlive_client
