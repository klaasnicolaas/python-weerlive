"""Asynchronous Python client for Weerlive."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, time

from mashumaro import field_options
from mashumaro.config import BaseConfig
from mashumaro.mixins.orjson import DataClassORJSONMixin
from mashumaro.types import SerializationStrategy


class IntegerIsBoolean(SerializationStrategy):
    """Boolean serialization strategy for integers."""

    def serialize(self, value: bool) -> int:  # noqa: FBT001
        """Serialize a boolean to an integer."""
        return int(value)

    def deserialize(self, value: str) -> bool:
        """Deserialize an integer to a boolean."""
        return bool(int(value))


class TimeStrategy(SerializationStrategy):
    """String serialization strategy to handle the time format."""

    def serialize(self, value: time) -> str:
        """Serialize time to string."""
        return value.strftime("%H:%M")

    def deserialize(self, value: str) -> time:
        """Deserialize string to time."""
        return datetime.strptime(value, "%H:%M").astimezone().time()


@dataclass
# pylint: disable-next=too-many-instance-attributes
class Weather(DataClassORJSONMixin):
    """Object representing an Weather model.

    Attributes
    ----------
        location: The location of the weather.
        temperature: Current temperature.
        wind_chill: Perceived temperature.
        summary: Description of weather conditions.
        humidity: Relative air humidity.
        wind_d: Wind direction.
        wind_ms: Wind speed in ms.
        wind_f: Wind force (Beaufort).
        wind_kn: Wind speed in knots.
        wind_kmh: Wind speed in km/h.
        air_pressure: Air pressure in hPa.
        air_pressure_mmhg: Air pressure in mmHg.
        dew_point: Dew point in degrees Celsius.
        visibility: Visibility in kilometers.
        forecast: Weather forecast for the next 24 hours.
        sun_up: Time of sunrise.
        sun_down: Time of sunset.
        icon: Weather icon.

        d0_weather: Weather forecast for today.
        d0_temp_max: Maximum temperature for today.
        d0_temp_min: Minimum temperature for today.
        d0_wind_f: Wind force (Beaufort) for today.
        d0_wind_kn: Wind speed in knots for today.
        d0_wind_ms: Wind speed in ms for today.
        d0_wind_kmh: Wind speed in km/h for today.
        d0_wind_d: Wind direction for today.
        d0_wind_ddg: Wind direction in degrees for today.
        d0_rainfall: Change of rainfall in % for today.
        d0_sun: Chance of sunshine in % for today.

        d1_weather: Weather forecast for tomorrow.
        d1_temp_max: Maximum temperature for tomorrow.
        d1_temp_min: Minimum temperature for tomorrow.
        d1_wind_f: Wind force (Beaufort) for tomorrow.
        d1_wind_kn: Wind speed in knots for tomorrow.
        d1_wind_ms: Wind speed in ms for tomorrow.
        d1_wind_kmh: Wind speed in km/h for tomorrow.
        d1_wind_d: Wind direction for tomorrow.
        d1_wind_ddg: Wind direction in degrees
        d1_rainfall: Change of rainfall in % for tomorrow.
        d1_sun: Chance of sunshine in % for tomorrow.

        d2_weather: Weather forecast for the day after tomorrow.
        d2_temp_max: Maximum temperature for the day after tomorrow.
        d2_temp_min: Minimum temperature for the day after tomorrow.
        d2_wind_f: Wind force (Beaufort) for the day after tomorrow.
        d2_wind_kn: Wind speed in knots for the day after tomorrow.
        d2_wind_ms: Wind speed in ms for the day after tomorrow.
        d2_wind_kmh: Wind speed in km/h for the day after tomorrow.
        d2_wind_d: Wind direction for the day after tomorrow.
        d2_wind_ddg: Wind direction in degrees
        d2_rainfall: Change of rainfall in % for the day after tomorrow.
        d2_sun: Chance of sunshine in % for the day after tomorrow.

        alarm_code: Boolean value indicating if there is an alarm.
        alarm_message: Message of the alarm.
    """

    def __post_init__(self) -> None:
        """Post init function."""
        if self.alarm_message == "":
            self.alarm_message = None

    # pylint: disable-next=too-few-public-methods
    class Config(BaseConfig):
        """Mashumaro configuration."""

        serialization_strategy = {time: TimeStrategy(), bool: IntegerIsBoolean()}  # noqa: RUF012
        serialize_by_alias = True

    location: str = field(metadata=field_options(alias="plaats"))
    temperature: float = field(metadata=field_options(alias="temp"))
    wind_chill: float = field(metadata=field_options(alias="gtemp"))
    summary: str = field(metadata=field_options(alias="samenv"))
    humidity: int = field(metadata=field_options(alias="lv"))
    wind_d: str = field(metadata=field_options(alias="windr"))
    wind_ms: float = field(metadata=field_options(alias="windms"))
    wind_f: int = field(metadata=field_options(alias="winds"))
    wind_kn: float = field(metadata=field_options(alias="windk"))
    wind_kmh: float = field(metadata=field_options(alias="windkmh"))
    air_pressure: float = field(metadata=field_options(alias="luchtd"))
    air_pressure_mmhg: int = field(metadata=field_options(alias="ldmmhg"))
    dew_point: float = field(metadata=field_options(alias="dauwp"))
    visibility: int = field(metadata=field_options(alias="zicht"))
    forecast: str = field(metadata=field_options(alias="verw"))
    sun_up: time = field(metadata=field_options(alias="sup"))
    sun_down: time = field(metadata=field_options(alias="sunder"))
    icon: str = field(metadata=field_options(alias="image"))

    d0_weather: str = field(metadata=field_options(alias="d0weer"))
    d0_temp_max: int = field(metadata=field_options(alias="d0tmax"))
    d0_temp_min: int = field(metadata=field_options(alias="d0tmin"))
    d0_wind_f: int = field(metadata=field_options(alias="d0windk"))
    d0_wind_kn: int = field(metadata=field_options(alias="d0windknp"))
    d0_wind_ms: int = field(metadata=field_options(alias="d0windms"))
    d0_wind_kmh: int = field(metadata=field_options(alias="d0windkmh"))
    d0_wind_d: str = field(metadata=field_options(alias="d0windr"))
    d0_wind_ddg: int = field(metadata=field_options(alias="d0windrgr"))
    d0_rainfall: int = field(metadata=field_options(alias="d0neerslag"))
    d0_sun: int = field(metadata=field_options(alias="d0zon"))

    d1_weather: str = field(metadata=field_options(alias="d1weer"))
    d1_temp_max: int = field(metadata=field_options(alias="d1tmax"))
    d1_temp_min: int = field(metadata=field_options(alias="d1tmin"))
    d1_wind_f: int = field(metadata=field_options(alias="d1windk"))
    d1_wind_kn: int = field(metadata=field_options(alias="d1windknp"))
    d1_wind_ms: int = field(metadata=field_options(alias="d1windms"))
    d1_wind_kmh: int = field(metadata=field_options(alias="d1windkmh"))
    d1_wind_d: str = field(metadata=field_options(alias="d1windr"))
    d1_wind_ddg: int = field(metadata=field_options(alias="d1windrgr"))
    d1_rainfall: int = field(metadata=field_options(alias="d1neerslag"))
    d1_sun: int = field(metadata=field_options(alias="d1zon"))

    d2_weather: str = field(metadata=field_options(alias="d2weer"))
    d2_temp_max: int = field(metadata=field_options(alias="d2tmax"))
    d2_temp_min: int = field(metadata=field_options(alias="d2tmin"))
    d2_wind_f: int = field(metadata=field_options(alias="d2windk"))
    d2_wind_kn: int = field(metadata=field_options(alias="d2windknp"))
    d2_wind_ms: int = field(metadata=field_options(alias="d2windms"))
    d2_wind_kmh: int = field(metadata=field_options(alias="d2windkmh"))
    d2_wind_d: str = field(metadata=field_options(alias="d2windr"))
    d2_wind_ddg: int = field(metadata=field_options(alias="d2windrgr"))
    d2_rainfall: int = field(metadata=field_options(alias="d2neerslag"))
    d2_sun: int = field(metadata=field_options(alias="d2zon"))

    alarm: bool = field(metadata=field_options(alias="alarm"))
    alarm_message: str | None = field(
        default=None, metadata=field_options(alias="alarmtxt")
    )
