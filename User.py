class User:
    def __init__(self, name, id):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name = name
        self.id = id
