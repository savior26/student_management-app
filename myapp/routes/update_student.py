from fastapi import APIRouter, status,Depends, HTTPException
from sqlalchemy.orm import Session
from myapp.database import get_db
from myapp.models import Student
from myapp.schema import StudentResponse, updateStudent

router= APIRouter(prefix="/student")

@router.put('/{id}', response_model= StudentResponse,status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: updateStudent, db: Session=Depends(get_db) ):
    student = db.query(Student).filter(Student.student_id==id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'student id {id} not available')
    student_data = request.model_dump(exclude_unset=True)

    for key, value in student_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student