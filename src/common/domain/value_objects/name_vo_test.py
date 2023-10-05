from .name_vo import Name
from src.events.domain.entities.customer_entity import Customer

# Must create a valid name
def test_name_value_object():
    name = Name('John Doe')
    assert name.value == 'John Doe'
    assert name.to_string() == 'John Doe'
    assert name.__str__() == 'John Doe'
    try:
        name.value = 'Jane Doe'
    except Exception as e:
        assert str(e) == 'Value cannot be changed'

def test_customer_aggregate():
    customer = Customer.create(
        {
            'cpf': '12345678901',
            'name': Name('John Doe')
        }
    )
    try:
        customer.name = 'Jane Doe'
    except Exception as e:
        assert str(e) == 'Value cannot be changed'
    customer.name = Name('Jane Doe')
    assert customer.name.value == 'Jane Doe'


