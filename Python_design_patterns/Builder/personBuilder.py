
class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment inof
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' +\
            f'Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}'

class PersonBuilder: # facade
    def __init__(self, person=None) -> None:
        if person is None:
            self.person = Person()
        else:
            self.person = person
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)
    
    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name:str):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self

if __name__ == "__main__":
    pb = PersonBuilder()
    p = pb\
        .lives\
            .at("2864 Brighton beach")\
            .in_city("Brooklyn")\
            .with_postcode('4654648')\
        .works\
            .at('Entreprenaur')\
            .as_a('Software Engineer/Data Science')\
            .earning('190000')\
        .build()

    print(p)
    person2 = PersonBuilder().build()
    print(person2)







