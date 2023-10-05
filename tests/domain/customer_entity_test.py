from src.common.domain.value_objects.cpf_vo import CPF
from src.common.domain.value_objects.name_vo import Name
from src.events.domain.entities.customer_entity import Customer

def test_customer_aggregate():
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
