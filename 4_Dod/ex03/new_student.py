import random
import string
from dataclasses import dataclass, field

# dataclass is designed to ony hold data values
# field is useful when you need to custmize your metadatas


def generate_id() -> str:
    """Generate random student id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """creates a student class with a random id"""
    try:
        name: str
        surname: str
        active: bool = field(default=True)
        login: str = field(init=False)
        id: str = field(default=generate_id(), init=False)

        def __post_init__(self):
            """Post-init method is the last thing __init__
            will call. Its helpful to set a data depending another"""
            self.login = self.name[0] + self.surname

    except Exception as e:
        print(e.str())
