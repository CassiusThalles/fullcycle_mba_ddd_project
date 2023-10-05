from .value_objects import ValueObject

class Name(ValueObject[str]):
    def __init__(self, value: str):
        super().__init__(value)
