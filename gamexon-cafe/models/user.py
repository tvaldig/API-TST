from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str
    password: str
    class Config:
        schema_extra = {
            "example":{
                "email" : "example@gmail.com",
                "password" : "password123",
            }
        }

class RegisterSchema(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        schema_extra = {
            "example":{
                "username" : "example", 
                "email" : "example@gmail.com",
                "password" : "password123",
            }
        }