import datetime


class NotVaccinatedError(Exception):
    pass


class OutdatedVaccineError(Exception):
    pass


class NotWearingMaskError(Exception):
    pass


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        actual_date = datetime.date.today()

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        if not "vaccine" in visitor:
            raise NotVaccinatedError
        else:
            if visitor["vaccine"]["expiration_date"] < actual_date:
                raise OutdatedVaccineError

        return f"Welcome to {self.name}"


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
    elif problems["mask"] > 0:
        return f"Friends should buy {problems['mask']} masks"
    elif problems["vaccine"] > 0:
        return f"All friends should be vaccinated"
