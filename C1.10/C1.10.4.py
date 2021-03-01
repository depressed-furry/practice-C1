class Client:
    status = "Client"

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def get_status(self):
        return self.status


class Mentor(Client):
    status = "Mentor"


visitors = [
    ("Ivan Petrov", "Moscow city", "Client"),
    ("Peter Ivanov", "Moscow city", "Client"),
    ("Arsen", "Minsk city", "Client"),
    ("Paul Walker", "Glendale city", "Mentor"),
    ("Calvin Klein", "New York city", "Mentor"),
    ("Tom Cruise", "New York city", "Mentor"),
]

for person in visitors:
    if person[2] == "Client":
        p = Client(person[0], person[1])
    else:
        p = Mentor(person[0], person[1])
    print(f'«{p.get_name()}, {p.get_city()}, статус "{p.get_status()}"»')
