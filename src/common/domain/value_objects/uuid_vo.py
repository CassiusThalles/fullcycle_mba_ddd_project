from .value_objects import ValueObject
import uuid

class UUID(ValueObject[str]):
    def __init__(self, value: str = None):
        if value == None:
            use_value = str(uuid.uuid4())
        else:
            use_value = uuid.UUID(str(value))
        self.__validate(use_value)
        use_value = str(use_value)
        super().__init__(use_value)
    
    def __validate(self, value: str) -> None:
        validating_uuid = uuid.UUID(str(value))
        if not validating_uuid.is_safe:
            raise Exception('Unsafe UUID')
        
