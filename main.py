from fastapi import FastAPI, Request
from myapp.routes import create_student
from myapp import models
from myapp.database import engine
from myapp.routes import create_student, ai_query, delete_student, get_students, update_student
app= FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(create_student.router)
app.include_router(get_students.router)
app.include_router(delete_student.router)
app.include_router(update_student.router)
app.include_router(ai_query.router)


