import pytest 
from registration_service import ( 
    RegistrationService, 
    InvalidEmailError, 
    UnderageError 
) 
 
 
@pytest.fixture 
def service(): 
    return RegistrationService() 
 
 
def test_successful_registration(service): 
    assert service.register_user("user@example.com", 22) is True 
 
 
def test_empty_email(service): 
    with pytest.raises(InvalidEmailError): 
        service.register_user("", 25) 
 
 
def test_invalid_email_format(service): 
    with pytest.raises(InvalidEmailError): 
        service.register_user("invalid-email", 25) 
 
 
def test_underage_user(service): 
    with pytest.raises(UnderageError): 
        service.register_user("user@example.com", 16) 
 
 
def test_none_email_assertion(service): 
    with pytest.raises(AssertionError): 
        service.register_user(None, 20)