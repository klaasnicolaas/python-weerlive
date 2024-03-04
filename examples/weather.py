"""Asynchronous Python client for Weerlive."""

from __future__ import annotations

import asyncio

from weerlive import Weerlive


async def main() -> None:
    """Show example on using the Weerlive API client."""
    async with Weerlive(
        api_key="API_KEY",
        longitude=52.1009166,
        latitude=5.6462914,
    ) as client:
        weather = await client.weather()
        print(weather)


if __name__ == "__main__":
    asyncio.run(main())
