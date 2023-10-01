from typing import TypedDict, NotRequired, Required
import json

class CustomerCustomProperties(TypedDict):
    id: NotRequired[str]
    cpf: Required[str]
    name: Required[str]

class Customer:
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
        return Customer(command)
    
    def to_json(self) -> str:
        return json.dumps(self.__dict__)
