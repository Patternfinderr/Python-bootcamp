
class person:
    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.dob = None

    def __str__(self) -> str:
        return f"{self.name} born on {self.dob}\
                works as a {self.position}"

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()

    def build(self) - object:
        return self.person

