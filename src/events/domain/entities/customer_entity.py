from typing import Any, TypedDict, NotRequired, Required
from src.common.domain.aggregate_root import AggregateRoot
from src.common.domain.value_objects.name_vo import Name
import json

class CustomerCustomProperties(TypedDict):
    id: NotRequired[str]
    cpf: Required[str]
    name: Required[Name]
    # name: Required[str]

class Customer(AggregateRoot):
    def __init__(self, properties: CustomerCustomProperties):
        self._id_ = properties['id']
        self._cpf_ = properties['cpf']
        self._name_ = properties['name']
    
    def __dict__(self) -> dict:
        return {
            'id': self._id_,
            'cpf': self._cpf_,
            'name': self._name_
        }
    
    @property
    def id(self) -> str:
        return self._id_
    
    @id.setter
    def id(self, value: str) -> None:
        self._id_ = value
    
    @property
    def cpf(self) -> str:
        return self._cpf_
    
    @cpf.setter
    def cpf(self, value: str) -> None:
        self._cpf_ = value
    
    @property
    def name(self) -> Name:
        return self._name_
    
    @name.setter
    def name(self, value: str|Name) -> None:
        if type(value) == str:
            self._name_.value = value
        else:
            self._name_ = value
    
    @staticmethod
    def create(command: CustomerCustomProperties) -> 'Customer':
        if('cpf' not in command or command['cpf'] == '' or command['cpf'] == None):
            raise Exception('CPF is required')
        if('name' not in command or command['name'] == '' or command['name'] == None):
            raise Exception('Name is required')
        if('id' not in command or command['id'] == '' or command['id'] == None):
            command['id'] = 'id'
        return Customer(command)
    
    def to_json(self) -> str:
        return json.dumps(self.__dict__())
