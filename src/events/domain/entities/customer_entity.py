from typing import TypedDict, NotRequired, Required
from src.common.domain.aggregate_root import AggregateRoot
import json

class CustomerCustomProperties(TypedDict):
    id: NotRequired[str]
    cpf: Required[str]
    name: Required[str]

class Customer(AggregateRoot):
    def __init__(self, properties: CustomerCustomProperties):
        self.id = properties['id']
        self.cpf = properties['cpf']
        self.name = properties['name']
    
    def __dict__(self) -> dict:
        return {
            'id': self.id,
            'cpf': self.cpf,
            'name': self.name
        }
    
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
