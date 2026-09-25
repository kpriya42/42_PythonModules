#!/usr/bin/env python3
# uvx --with pydantic mypy --strict .
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def display_station(ss: SpaceStation) -> None:
    status = "Operational" if ss.is_operational else "Not operational"
    print(f"ID: {ss.station_id}",
          f"Name: {ss.name}",
          f"Crew: {ss.crew_size} people",
          f"Power: {ss.power_level}%",
          f"Oxygen: {ss.oxygen_level}%",
          f"last maintenance: {ss.last_maintenance.strftime('%c')}",
          f"Status: {status}",
          f"notes: {ss.notes}", sep='\n')


def display_error(e: ValidationError) -> None:
    print("Expected validation error:\n"
          f"{e.error_count()} validation errors found for SpaceStation")
    errors = e.errors()
    for error in errors:
        attribute = error["loc"][0]
        err_msg = error["msg"]
        print(f"  {attribute} - {err_msg}")
    print()


def main() -> None:
    print("\n====================================================")
    print("Space Station Data Validation")
    try:
        print("====================================================")
        ss1 = SpaceStation(
            station_id="LGW125",
            name="Titan Mining Outpost",
            crew_size=6,
            power_level=76.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 8, 28, 21, 26, 15),
            is_operational=True,
            notes=None)

        print("Valid station created:")
        display_station(ss1)
    except ValidationError as e:
        display_error(e)

    try:
        print("\n====================================================")
        ss2 = SpaceStation(
                    station_id="ISS674",
                    name="Europa Research Station",
                    crew_size=50,
                    power_level=185.5,
                    oxygen_level=92.3,
                    last_maintenance=datetime(2026, 8, 20, 16, 26, 35),
                    is_operational=False,
                    notes="System diagnostics required")

        print("Valid station created:")
        display_station(ss2)
    except ValidationError as e:
        display_error(e)


if __name__ == "__main__":
    main()
