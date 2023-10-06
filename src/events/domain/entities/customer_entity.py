from typing import TypedDict, NotRequired, Required
from src.common.domain.aggregate_root import AggregateRoot
from src.common.domain.value_objects.name_vo import Name
from src.common.domain.value_objects.cpf_vo import CPF
from src.common.domain.value_objects.uuid_vo import UUID
import json

class CustomerCustomProperties(TypedDict):
    id: NotRequired[UUID]
    cpf: Required[CPF]
    name: Required[Name]

class Customer(AggregateRoot):
    def __init__(self, properties: CustomerCustomProperties):
        self.__validate_input(properties)
        self.__id = properties['id']
        self.__cpf = properties['cpf']
        self.__name = properties['name']
    
    def __validate_input(self, properties: CustomerCustomProperties) -> None:
        if('cpf' not in properties or properties['cpf'] == '' or properties['cpf'] == None):
            raise Exception('CPF is required')
        if('name' not in properties or properties['name'] == '' or properties['name'] == None):
            raise Exception('Name is required')
        if(type(properties['cpf']) != CPF):
            raise Exception('CPF must be a CPF Value Object instance')
        if(type(properties['name']) != Name):
            raise Exception('Name must be a Name Value Object instance')
    
    def __dict__(self) -> dict:
        return {
            'id': self.__id,
            'cpf': self.__cpf.value,
            'name': self.__name.value
        }
    
    @property
    def id(self) -> str:
        return self.__id
    
    @id.setter
    def id(self, value: str) -> None:
        self.__id = value
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @cpf.setter
    def cpf(self, new_cpf: str|CPF) -> None:
        if type(new_cpf) == str:
            self.__cpf.value = new_cpf
        else:
            self.__cpf = CPF(new_cpf.value)
    
    @property
    def name(self) -> Name:
        return self.__name
    
    @name.setter
    def name(self, new_name: str|Name) -> None:
        if type(new_name) == str:
            self.__name.value = new_name
        else:
            self.__name = Name(new_name.value)
    
    @staticmethod
    def create(command: CustomerCustomProperties) -> 'Customer':
        if('cpf' not in command or command['cpf'] == '' or command['cpf'] == None):
            raise Exception('CPF is required')
        if('name' not in command or command['name'] == '' or command['name'] == None):
            raise Exception('Name is required')
        if('id' not in command or command['id'] == '' or command['id'] == None):
            command['id'] = UUID()
        if(type(command['id']) == str):
            command['id'] = UUID(command['id'])
        elif(type(command['id']) != UUID):
            raise Exception('ID must be a UUID Value Object instance')
        return Customer(command)
    
    def to_json(self) -> str:
        return json.dumps(self.__dict__())
    
    def dtypes(self) -> dict:
        return {
            'id': type(self.__id),
            'cpf': type(self.__cpf),
            'name': type(self.__name)
        }
