#!usr/bin/env python3
# uvx --with pydantic mypy --strict .
from pydantic import BaseModel, Field, model_validator, ValidationError
from typing_extensions import Self
from datetime import datetime
from enum import Enum


class CrewRanks(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def safety_requirements(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(member.rank in (CrewRanks.COMMANDER, CrewRanks.CAPTAIN)
                   for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            expert_crew = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    expert_crew += 1
            if expert_crew / len(self.crew) < 0.5:
                raise ValueError("Long missions (> 365 days) need 50% "
                                 "experienced crew (5+ years)")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def display_mission(mission: SpaceMission) -> None:
    print(f"ID: {mission.mission_id}",
          f"Destination: {mission.destination}",
          f"Duration: {mission.duration_days} days",
          f"Mission Status: {mission.mission_status}",
          f"Budget: ${mission.budget_millions}M",
          f"Crew size: {len(mission.crew)}",
          "Crew members:", sep='\n')

    for member in mission.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")


def display_error(e: ValidationError) -> None:
    print("Expected validation error:\n")

    print(f"{e.error_count()} validation errors found for Space Mission")
    errors = e.errors()
    for error in errors:
        if error["loc"]:
            print(error['loc'][0], "-", end='')
        print(f"  {error['msg']}")
    print()


def main() -> None:
    print("\n====================================================")
    print("Space Mision Crew Validation")
    try:
        print("====================================================")
        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[CrewMember(
                member_id="001",
                name="Sarah Connor",
                rank=CrewRanks.COMMANDER,
                age=30,
                specialization="Mission Command",
                years_experience=10,
            ),
                CrewMember(
                member_id="002",
                name="John Smith",
                rank=CrewRanks.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=5,
            ),
                CrewMember(
                member_id="003",
                name="Alice Johnson",
                rank=CrewRanks.OFFICER,
                age=29,
                specialization="Engineering",
                years_experience=5,
            )
            ],
            mission_status="Ongoing",
            budget_millions=2500
        )
        print("Valid mission created:")
        display_mission(mission1)
    except (ValidationError) as e:
        display_error(e)

    try:
        print("\n====================================================")
        mission2 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[CrewMember(
                member_id="001",
                name="Sarah Connor",
                rank=CrewRanks.CADET,
                age=30,
                specialization="Mission Command",
                years_experience=5,
                is_active=True
            ),
                CrewMember(
                member_id="002",
                name="John Smith",
                rank=CrewRanks.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=0,
                is_active=True
            ),
                CrewMember(
                member_id="003",
                name="Alice Johnson",
                rank=CrewRanks.OFFICER,
                age=29,
                specialization="Engineering",
                years_experience=5,
                is_active=True
            )
            ],
            budget_millions=5000
        )
        print("Valid mission created:")
        display_mission(mission2)
    except (ValidationError) as e:
        display_error(e)


if __name__ == "__main__":
    main()
