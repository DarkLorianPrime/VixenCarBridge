import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class PassportModel(SQLModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    sex: bool
    series: int = Field(max_length=4)
    number: int = Field(max_length=6)
    subdiv_code: str = Field(max_length=7)
    issue_date: datetime.date
    issuing_place: str
    birth_day: datetime.date
    birth_place: str
