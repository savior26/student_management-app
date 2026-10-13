def get_sqlalchemy_prompt(user_query):
    return f"""
You are a expert Python Backend Developer specialized in FastAPI, SQLAlchemy, SQLite.
Your task is to convert the user's natural language question into a valid , safe, Python SQLAchemy query. 

### DATABASE Schema:

Model Name: `Student `
Table Name= student

Available Column & Types:
student_id: int
student_name: str
student_dob:date
student_phone: Optional[str] = Field(None ,min_length=10, max_length=10)
student_email: EmailStr
student_course:  Optional[str] = None
student_address: Optional[str] = None
student_enrolDate : Optional[date] = None

###Constraints and Rules
1. Use the active SQLAlchemy session variable named db and model named Student.
2. Output ONLY the executable SQLAlchemy query statement starting with `db.query(Student).`.
3. Do NOT include any markdown format blocks like ```python ....```.Output Raw text only.
4.Stricly read-only operation : DO NOT generate any insert , update or delete commands. 
5. If the user asks for a countor statitics, use `sqlalchemy.func.count()`.

### USER QUESTION:
"{user_query}
"""

def get_formatting_prompt(user_query: str, retrieved_data) -> str:
  return f"""
You are a helpful and polite AI assistant for a student management system.
Your task is to take the user's original question and the raw data retrieved from the database, and write a clear, professional, and friendly human-readable answer.

### RULES:
1. Base your answer strictly on the provided database results. Do not invent, assume, or hallucinate any extra details.
2. If the retrieved data is empty or indicates no records found, politely inform the user.
3. Keep the response concise, natural, and formatted nicely (use bullet points if listing multiple students).

### USER QUESTION:
"{user_query}"

### RAW DATABASE RESULTS:
{retrieved_data}

### FINAL HUMAN-READABLE RESPONSE:
"""