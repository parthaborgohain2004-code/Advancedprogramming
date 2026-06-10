import re 
 
 
class InvalidEmailError(ValueError): 
    """Raised when the email is invalid.""" 
    pass 
 
 
class UnderageError(RuntimeError): 
    """Raised when the user's age is below 18.""" 
    pass 
 
 
class RegistrationService: 
 
    EMAIL_PATTERN = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' 
 
    def register_user(self, email: str, age: int) -> bool: 
 
        # Internal invariant check 
        assert email is not None, "System invariant violated: email cannot be None" 
 
        # Validate email 
        if not email or email.strip() == "": 
            raise InvalidEmailError("Email cannot be empty.") 
 
        if not re.match(self.EMAIL_PATTERN, email): 
            raise InvalidEmailError("Invalid email format.") 
 
        # Validate age 
        if age < 18: 
            raise UnderageError("User must be at least 18 years old.") 
 
        return True