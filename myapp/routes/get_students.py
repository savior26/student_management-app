from fastapi import APIRouter, status,Depends, HTTPException
from sqlalchemy.orm import Session
from myapp.database import get_db
from myapp.models import Student
from myapp.schema import StudentResponse
from typing import List

router= APIRouter(prefix="/student")

@router.get('/',response_model=List[StudentResponse])
def all_students( db: Session=Depends(get_db)):
    students= db.query(Student).all()
    return students


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=StudentResponse)
def show_student(id ,db: Session=Depends(get_db) ):
    student= db.query(Student).filter(Student.student_id==id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'student id {id} not available')
    return student
