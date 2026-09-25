#!usr/bin/env python3
# uvx --with pydantic mypy --strict .
from pydantic import BaseModel, Field, model_validator, ValidationError
from typing_extensions import Self
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telephatic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def bussines_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.witness_count < 3 and
                self.contact_type == ContactType.TELEPATHIC):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")

        if self.signal_strength >= 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) "
                             "should include received messages")
        return self


def display_contact(alien: AlienContact) -> None:
    print(f"ID:: {alien.contact_id}",
          f"Type: {alien.contact_type.value}",
          f"Location: {alien.location}",
          f"Signal: {alien.signal_strength}/10",
          f"Duration: {alien.duration_minutes} minutes",
          f"Witnesses: {alien.witness_count} people", sep='\n')
    if alien.message_received:
        print(f"Message: '{alien.message_received}'")


def display_error(e: ValidationError) -> None:
    print("Expected validation error:\n")

    print(f"{e.error_count()} validation errors found for Alien contact")
    errors = e.errors()
    for error in errors:
        if error["loc"]:
            print(error['loc'][0], "-", end='')
        print(f"  {error['msg']}")
    print()


def main() -> None:
    print("\n====================================================")
    print("Alien Contact Log Validation")
    try:
        print("====================================================")
        alien1 = AlienContact(
            contact_id="AC_2024_016",
            timestamp=datetime.now(),
            location="Antarctic Research Statio",
            contact_type=ContactType.VISUAL,
            signal_strength=8.6,
            duration_minutes=45,
            witness_count=5,
            message_received="Warning about solar flare activity")

        print("Valid contact report:")
        display_contact(alien1)
    except (ValidationError) as e:
        display_error(e)

    try:
        print("\n====================================================")
        alien2 = AlienContact(
                    contact_id="AC_2024_010",
                    timestamp=datetime.now(),
                    location="Area 51, Nevada",
                    contact_type=ContactType.TELEPATHIC,
                    signal_strength=5.0,
                    duration_minutes=45,
                    witness_count=2,
                    message_received=None,
                    is_verified=False
                    )
        print("Valid station created:")
        display_contact(alien2)
    except (ValidationError) as e:
        display_error(e)


if __name__ == "__main__":
    main()
