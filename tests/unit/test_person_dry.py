from src.person import Person
def person():
    person = Person("Emi")
    return person


def test_person_is_adult(person):
    person.age = 19
    assert person.is_adult()


def test_person_is_not_adult(person):
    person.age = 10
    assert not person.is_adult() 