from fastapi import APIRouter, status,Depends, HTTPException
from sqlalchemy.orm import Session
from myapp.database import get_db
from myapp.models import Student

router= APIRouter(prefix="/student")

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id, db: Session=Depends(get_db)):
    student= db.query(Student).filter(Student.student_id==id)
    if not student.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'student id {id} not available')
    student.delete()
    db.commit()
    return "Student deleted"