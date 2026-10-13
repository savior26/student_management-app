from database import Base
from sqlalchemy import Column, Integer, String, Date
                     

class Student(Base):
    __tablename__= 'student'
    student_id= Column(Integer, primary_key=True, index=True)
    student_name= Column(String)
    student_dob=Column(Date)
    student_phone= Column(String, nullable=True)
    student_email=Column(String,unique=True,index=True, nullable=False)
    student_course= Column(String,nullable=True)
    student_address= Column(String,nullable=True)
    student_enrolDate = Column(Date,nullable=True)





    
