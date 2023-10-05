from src.common.domain.value_objects.name_vo import Name

def test_name_value_object():
    name = Name('John Doe')
    assert name.value == 'John Doe'
    assert name.to_string() == 'John Doe'
    assert name.__str__() == 'John Doe'
    try:
        name.value = 'Jane Doe'
    except Exception as e:
        assert str(e) == 'Value cannot be changed'