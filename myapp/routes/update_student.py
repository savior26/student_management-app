from fastapi import APIRouter, status,Depends, HTTPException
from sqlalchemy.orm import Session
from myapp.database import get_db
from myapp.models import Student
from myapp.schema import createStudent, StudentResponse

router= APIRouter(prefix="/student")

@router.put('/{id}', response_model= StudentResponse,status_code=status.HTTP_202_ACCEPTED)
def update(id, request: createStudent, db: Session=Depends(get_db) ):
    student = db.query(Student).filter(Student.student_id==id)
    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'student id {id} not available')
    student.update(request.model_dump())
    db.commit()
    return student