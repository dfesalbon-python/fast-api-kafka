from pydantic import BaseModel


class Employee(BaseModel):
    id: str
    first_name: str
    last_name: str
