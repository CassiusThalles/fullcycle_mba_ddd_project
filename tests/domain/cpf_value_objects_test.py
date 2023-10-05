from src.common.domain.value_objects.cpf_vo import CPF

def test_cpf_value_object():
    try:
        CPF('1')
    except Exception as e:
        assert str(e) == 'CPF must have 11 digits'
    try:
        CPF('11111111111')
    except Exception as e:
        assert str(e) == 'CPF cannot be a sequence of repeated digits'
    try:
        CPF('abcdefghijk')
    except Exception as e:
        assert str(e) == 'CPF must have 11 digits'
    try:
        cpf = CPF('12345678901')
    except Exception as e:
        assert str(e) == 'CPF is invalid'
    cpf = CPF('12345678909')
    assert cpf.value == '12345678909'
    try:
        cpf.value = '12345678901'
    except Exception as e:
        assert str(e) == 'Value cannot be changed'
