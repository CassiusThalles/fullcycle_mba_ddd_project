from src.common.domain.value_objects.uuid_vo import UUID
from types import NotImplementedType
import pytest

"""
Define tests to the UUID Value Object
"""

def test_uuid_badly_formed_value():
    """
    Test if the UUID Value Object raises an exception when the value is badly formed
    """
    with pytest.raises(Exception) as e:
        UUID('testing anything as an uuid')
        assert str(e) == 'badly formed hexadecimal UUID string'

def test_uuid_safe_value():
    """
    Test if the UUID Value Object raises an exception when the value is unsafe
    """
    with pytest.raises(Exception) as e:
        UUID('00000000-0000-0000-0000-000000000000')
        assert str(e) == 'Unsafe UUID'

def test_uuid_value():
    """
    Test if the UUID Value Object is created with a valid value
    """
    myid = UUID('828cd456-7bcc-4716-b2af-3a2e2ef53e57')
    assert myid.value == '828cd456-7bcc-4716-b2af-3a2e2ef53e57'

def test_uuid_value_not_implemented():
    """
    Test if the UUID Value Object is created when the value is not provided
    """
    myid = UUID()
    assert myid.value != None
    assert myid.value != ''
    assert myid.value != NotImplementedType

def test_uuid_change_value():
    """
    Test if the UUID Value Object raises an exception when the value is changed
    """
    myid = UUID('828cd456-7bcc-4716-b2af-3a2e2ef53e57')
    assert myid.value == '828cd456-7bcc-4716-b2af-3a2e2ef53e57'
    with pytest.raises(Exception) as e:
        myid.value = 'testing anything as an uuid'
        assert str(e) == 'Value cannot be changed'
    myid = UUID('3bd37a53-8c02-4b4a-b907-9e37be214ffc')
    assert myid.value == '3bd37a53-8c02-4b4a-b907-9e37be214ffc'
