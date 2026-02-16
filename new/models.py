from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    marks: int
    year: int
    usn: str

class MinData(BaseModel):
    name: str
    age: int
    