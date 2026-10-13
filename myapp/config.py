import os
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()

DATABASE_URL= os.getenv("DATABASE_URL")


class Settings(BaseModel):
    DATABASE_URL:str= DATABASE_URL
    

settings= Settings() 

