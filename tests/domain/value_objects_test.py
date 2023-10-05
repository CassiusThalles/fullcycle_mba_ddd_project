from src.common.domain.value_objects.value_objects import ValueObject

def test_value_object():
    value_object = ValueObject('John Doe')
    assert value_object.value == 'John Doe'
    assert value_object.value != 'Jane Doe'
    assert value_object.__repr__() == 'ValueObject(John Doe)'
    try:
        assert value_object.value == 'Jane Doe'
    except Exception as e:
        assert type(e) == AssertionError
    assert value_object.to_string() == 'John Doe'
    assert str(value_object) == 'John Doe'
    try:
        value_object.value = 'Jane Doe'
    except Exception as e:
        assert str(e) == 'Value cannot be changed'
    try:
        value_object.value = 'Jane Doe'
    except Exception as e:
        assert str(e) == 'Value cannot be changed'