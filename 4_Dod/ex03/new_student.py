import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """creates a student class with a random id"""
    try :
        name: str
        surname: str
        active: bool = field(default=True, init=False)
        id: str = field(default=generate_id(), init=False)

    except Exception as e:
        print(e.str())
