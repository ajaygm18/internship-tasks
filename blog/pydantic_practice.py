from pydantic import BaseModel, computed_field,field_validator, model_validator, ValidationInfo,ValidationError, Field, EmailStr, SecretStr, HttpUrl
from datetime import datetime, UTC
from typing import Optional, Literal, Annotated
from uuid import UUID, uuid4


class Sample(BaseModel):
    name: str
    usn: Annotated[int, Field(gt=8, le=100)] 
    uid: UUID = Field(default_factory=uuid4)
    email: EmailStr
    pwd: SecretStr
    website: HttpUrl | None
    sub: list[str] = []
    friends: Optional[list[str]]
    projects: list[str] = Field(default_factory=list)
    timestamps: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    status: Literal['studying', 'working', 'sleeping'] = 'working'
    slug: Annotated[str, Field(pattern=r'^[a-z0-9-]+$')]


    @field_validator('name')
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace('_', '').isalnum():
            raise ValueError('uname must be alpha numeric')
        return v.lower()

    @field_validator('website', mode='before')
    @classmethod
    def validate_website(cls, v:str):
        if v.startswith(('http://', 'https://')):
            return v
        else:
            return 'https://' + v
        


try:
    usr = Sample(name='ajay', usn=33, friends=['god', 'myself', 'family'],
                 slug='ajay352d', email='huidw@gmail.com',
                 website='google.com', pwd='abcd'
    )
    print(usr)
    print(usr.model_dump_json(indent=4))
    print(usr.pwd.get_secret_value())
except ValidationError as e:
    print(e)
