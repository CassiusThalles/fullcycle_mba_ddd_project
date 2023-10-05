from typing import Any, Generic, TypeVar
from types import NotImplementedType

T = TypeVar('T')

class ValueObject(Generic[T]):
    def __init__(self, value: T):
        self._value_ = value
    
    @property
    def value(self) -> T:
        return self._value_
    
    @value.setter
    def value(self, value: T) -> None:
        if(self._value_ != value):
            raise Exception('Value cannot be changed')
    
    def __eq__(self, other: T) -> bool:
        return self.value == other
    
    def __ne__(self, other: T) -> bool:
        return self.value != other
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.value})'
    
    def __str__(self) -> str:
        return str(self.value)
    
    def equals(self, obj: T) -> bool:
        if(obj == None):
            return False
        if(obj is NotImplementedType):
            return False
        if(type(obj) != type(self)):
            return False
        if(obj.value != self.value):
            return False
        if(obj.__class__.__name__ != self.__class__.__name__):
            return False
        return True
    
    def to_string(self) -> str:
        return str(self.value)
