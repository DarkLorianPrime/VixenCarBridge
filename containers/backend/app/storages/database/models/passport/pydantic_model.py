import datetime
from typing import Optional, Any

from sqlmodel import SQLModel, Field


class PassportModel(SQLModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    sex: bool
    series: int = Field(ge=1000, le=9999)
    number: int = Field(ge=100000, le=999999)
    subdiv_code: str = Field(max_length=7)
    issue_date: datetime.date
    issuing_place: str
    birth_day: datetime.date
    birth_place: str


class CreatePassportModel(PassportModel):
    returning: Any = False
