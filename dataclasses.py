from dataclasses import dataclass, field
import hashlib
import random

def encrypt_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def generate_id() -> int:
    return int(random.random() * 10000)

class User():
    def __init__(self, name: str, surname: str, email: str, phone_number: str, age: int, password: str, id: int) -> None:
        self.name: str = name
        self.surname: str = surname
        self.email: str = email
        self.phone_number: str = phone_number
        self.age: int = age
        self.password: str = password
        self.id: int = id

# @dataclass(kw_only=True, frozen=True)
class UserDataclass:
    name: str
    surname: str
    email: str
    phone_number: str
    age: int
    password: str = field(repr=False)
    id: int = field(init=False, default_factory=generate_id)
    
    def __post_init__(self):
        self.password = encrypt_password(self.password)
    
    def __str__(self) -> str:
        return f"{self.name} {self.surname} ({self.email})"
    
def main() -> None:
    user_without_dataclass = User("John", "Doe", "john@doe.com", "123-456-7890", 25, "secret_password", 2137)
    user_with_dataclass = UserDataclass(name="John", surname="Doe", email="john@doe.com", phone_number="123-456-7890", age=25, password="secret_password")

    print("Without dataclass:", user_without_dataclass)
    print("With dataclass: ", user_with_dataclass)

    # user_with_dataclass.name = "Changed"
    print(user_with_dataclass)  # User-friendly string representation
    print(repr(user_with_dataclass))  # Developer-friendly representation (includes id and password)


if __name__ == "__main__":
    main()