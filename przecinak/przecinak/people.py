class Person:
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def __eq__(self, o):
        return (self.login == o.login and self.password == o.password)