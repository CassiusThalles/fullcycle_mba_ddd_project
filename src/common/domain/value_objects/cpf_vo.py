from .value_objects import ValueObject
import re

class CPF(ValueObject[str]):
    def __init__(self, value: str):
        corrected_value = self.__sanitize_cpf(value)
        self.__validate_cpf(corrected_value)
        super().__init__(corrected_value)
        
    
    def __sanitize_cpf(self, value: str) -> str:
        return ''.join(re.findall('[0-9]', value))
    
    def __validate_cpf(self, value: str) -> None:
        if(len(value) != 11):
            raise Exception('CPF must have 11 digits')
        if(len(set(re.findall('[0-9]', value))) == 1):
            raise Exception('CPF cannot be a sequence of repeated digits')
        if(not value.isdigit()):
            raise Exception('CPF must have only digits')
        
        sum = 0
        for i in range(9):
            sum += (10 - i) * int(value[i])
        first_digit = 11 - (sum % 11)
        if(first_digit > 9):
            first_digit = 0
        
        sum = 0
        for i in range(10):
            sum += (11 - i) * int(value[i])
        second_digit = 11 - (sum % 11)
        if(second_digit > 9):
            second_digit = 0
        
        if(first_digit != int(value[9]) or second_digit != int(value[10])):
            raise Exception('CPF is invalid')
