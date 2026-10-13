from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

class studentBase(BaseModel):
    student_name: str
    student_dob:date
    student_phone: Optional[str] = Field(None ,min_length=10, max_length=10)
    student_email: EmailStr
    student_course:  Optional[str] = None
    student_address: Optional[str] = None
    student_enrolDate : Optional[date] = None


class createStudent(studentBase):
    pass


class StudentResponse(studentBase):
    student_id: int

    class Config: 
        from_attributes=True

    
class AIQueryRequest(BaseModel):
    question:str


class aiResponse(AIQueryRequest):
    answer:str
    class Config: 
            from_attributes=True