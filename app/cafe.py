import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        actual_date = datetime.date.today()

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError

        if "vaccine" not in visitor:
            raise NotVaccinatedError

        if visitor["vaccine"]["expiration_date"] < actual_date:
            raise OutdatedVaccineError

        return f"Welcome to {self.name}"
