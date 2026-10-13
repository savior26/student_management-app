from fastapi import APIRouter, status,Depends, Response
from sqlalchemy.orm import Session
from myapp.database import get_db
from myapp.models import Student
from myapp.schema import createStudent, StudentResponse
router= APIRouter(prefix="/student")

@router.post('/',response_model=StudentResponse, status_code=status.HTTP_201_CREATED )
def create_student(request:createStudent, db: Session=Depends(get_db)):
    new_student= Student(**request.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student