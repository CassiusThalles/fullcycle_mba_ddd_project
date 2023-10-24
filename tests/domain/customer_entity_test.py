from src.common.domain.value_objects.cpf_vo import CPF
from src.common.domain.value_objects.name_vo import Name
from src.events.domain.entities.customer_entity import Customer
from types import NotImplementedType
import pytest

"""
This test will check if the Customer entity is working as expected.
"""

def test_customer_entity():
    """
    This test will check if the Customer entity is created with the correct values when not provided with an ID.
    """
    customer = Customer.create(
        {
            'cpf': CPF('12345678909'),
            'name': Name('John Doe')
        }
    )
    assert customer.cpf == CPF('12345678909')
    assert customer.name == Name('John Doe')
    assert customer.id != None
    assert type(customer.id) != NotImplementedType

def test_customer_entity_with_id():
    """
    This test will check if the Customer entity is created with the correct values when provided with an ID.
    """
    customer = Customer.create(
        {
            'id': '123e4567-e89b-12d3-a456-426614174000',
            'cpf': CPF('12345678909'),
            'name': Name('John Doe')
        }
    )
    assert customer.cpf == CPF('12345678909')
    assert customer.name == Name('John Doe')
    assert customer.id == '123e4567-e89b-12d3-a456-426614174000'

def test_customer_entity_with_invalid_id():
    """
    This test will check if the Customer entity raises an exception when provided with an invalid ID.
    """
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'id': '11111111-1111-1111-1111-111111111111',
                'cpf': CPF('12345678909'),
                'name': Name('John Doe')
            }
        )
        assert str(e) == 'Unsafe UUID'
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'id': 'testing anything as an uuid',
                'cpf': CPF('12345678909'),
                'name': Name('John Doe')
            }
        )
        assert str(e) == 'badly formed hexadecimal UUID string'

def test_customer_entity_with_invalid_cpf():
    """
    This test will check if the Customer entity raises an exception when provided with an invalid CPF.
    """
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'cpf': '1234567890',
                'name': Name('John Doe')
            }
        )
        assert str(e) == 'CPF must be a CPF Value Object instance'
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'cpf': '',
                'name': Name('John Doe')
            }
        )
        assert str(e) == 'CPF is required'
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'cpf': None,
                'name': Name('John Doe')
            }
        )
        assert str(e) == 'CPF is required'

def test_customer_entity_with_invalid_name():
    """
    This test will check if the Customer entity raises an exception when provided with an invalid name.
    """
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'cpf': CPF('12345678909'),
                'name': 'John Doe'
            }
        )
        assert str(e) == 'Name must be a Name Value Object instance'
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'cpf': CPF('12345678909'),
                'name': ''
            }
        )
        assert str(e) == 'Name is required'
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'cpf': CPF('12345678909'),
                'name': None
            }
        )
        assert str(e) == 'Name is required'

def test_customer_entity_changing_values():
    """
    This test will check if the Customer entity raises an exception when trying to change its values.
    """
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'cpf': CPF('12345678909'),
                'name': Name('John Doe')
            }
        )
        customer.cpf.value = '13366591064'
        assert str(e) == 'Value cannot be changed'
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'cpf': CPF('12345678909'),
                'name': Name('John Doe')
            }
        )
        customer.name.value = 'Jane Doe'
        assert str(e) == 'Value cannot be changed'
    with pytest.raises(Exception) as e:
        customer = Customer.create(
            {
                'cpf': CPF('12345678909'),
                'name': Name('John Doe')
            }
        )
        customer.id.value = '123e4567-e89b-12d3-a456-426614174000'
        assert str(e) == 'Value cannot be changed'

def test_customer_change_values_using_value_objects():
    """
    This test will check if the Customer entity changes its values when provided with a valid value object.
    """
    customer = Customer.create(
        {
            'cpf': CPF('12345678909'),
            'name': Name('John Doe')
        }
    )
    
    customer = Customer.create(
        {
            'cpf': CPF('12345678909'),
            'name': Name('John Doe')
        }
    )
    try:
        customer.name = 'Jane Doe'
    except Exception as e:
        assert str(e) == 'Value cannot be changed'
    customer.name = Name('Jane Doe')
    assert customer.name.value == 'Jane Doe'
    try:
        customer.cpf = '13366591064'
    except Exception as e:
        assert str(e) == 'Value cannot be changed'
    customer.cpf = CPF('13366591064')
    assert customer.cpf == CPF('13366591064')
