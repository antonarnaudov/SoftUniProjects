class Customer:
    autoincremental_id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.autoincremental_id
        Customer.autoincremental_id += 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; " \
               f"Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.autoincremental_id
