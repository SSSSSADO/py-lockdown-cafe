from app.cafe import Cafe
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list[dict], cafe: str) -> str:
    cafe_obj = Cafe(cafe)
    problems = {"mask": 0, "vaccine": 0}

    for friend in friends:
        try:
            cafe_obj.visit_cafe(friend)
        except NotWearingMaskError:
            problems["mask"] += 1
        except (NotVaccinatedError, OutdatedVaccineError):
            problems["vaccine"] += 1

    if problems["mask"] == 0 and problems["vaccine"] == 0:
        return f"Friends can go to {cafe}"
    if problems["mask"] > 0 and problems["vaccine"] > 0:
        return "Friends should be vaccinated and buy masks"

    return "All friends should be vaccinated"
