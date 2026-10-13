from myapp.services.llm import get_llm
from myapp.services.query_prompt import get_sqlalchemy_prompt, get_formatting_prompt
from fastapi import APIRouter, status,Depends, HTTPException
from sqlalchemy.orm import Session
from myapp.database import get_db
from myapp.models import Student
from myapp.schema import aiResponse, AIQueryRequest
from sqlalchemy import func 
import sqlalchemy
router= APIRouter(prefix="/student")

llm= get_llm()
def generate_sqlalchemy(query):

    prompt= get_sqlalchemy_prompt(query)
    response= llm.invoke(prompt)
    generated = response.content[0]["text"].strip()
    return generated


@router.post('/ai', response_model = aiResponse,status_code=status.HTTP_200_OK)
def AiQueryResponse(request:AIQueryRequest ,db: Session=Depends(get_db) ):
    query= request.question
    sqlalchemy_query= generate_sqlalchemy(query)
    print(sqlalchemy_query)
    if sqlalchemy_query.startswith("db.query("):
        local_vars = {"db": db, "Student": Student,"func": func, "sqlalchemy": sqlalchemy}
        response = eval(sqlalchemy_query, {"__builtins__": {}}, local_vars)
        print('response: ',response)
        prompt= get_formatting_prompt(query, response)
        answer= llm.invoke(prompt)
         
        return {'question':query, 'answer':answer.content[0]["text"]}

        
    else:
        raise  HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Can't complete your this query: {query}")
    

