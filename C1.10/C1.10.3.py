class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance


c1, c2 = Client("Ivan Petrov", "50 руб"), Client("Paul Walker", "456$")
print(f"Клиент: «{c1.get_name()}». Баланс: {c1.get_balance()}.")
print(f"Клиент: «{c2.get_name()}». Баланс: {c2.get_balance()}.")
