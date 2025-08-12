from pydantic import BaseModel
from typing import Optional 
class Contact(BaseModel):
    first_name:Optional[str] = None
    last_name:Optional[str] = None
    email:Optional[str] = None
    phone:Optional[str]= None
    address:Optional[str] = None
