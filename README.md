# Student Management API

A FastAPI application for managing student records, with an AI-powered natural-language query endpoint.

## Requirements

- Python 3.10 or newer
- A Google Gemini API key for the AI query endpoint
- A database URL in the format accepted by SQLAlchemy (the database module is configured for SQLite)

## Setup

From the project directory, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root and set the database URL and Google API key:

```dotenv
DATABASE_URL=sqlite:///./students.db
GOOGLE_API_KEY=your_google_api_key
```

Keep `.env` private; it is excluded from version control.

## Run

Start the development server from the project root:

```powershell
uvicorn main2:app --reload
```

Open the interactive API documentation at <http://127.0.0.1:8000/docs>.

## API

All endpoints use the `/student` prefix:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/student/` | Create a student |
| `GET` | `/student/` | List students |
| `GET` | `/student/{id}` | Get a student by ID |
| `PUT` | `/student/{id}` | Update a student |
| `DELETE` | `/student/{id}` | Delete a student |
| `POST` | `/student/ai` | Ask a natural-language question about student records |

Student creation and update requests accept JSON with these fields:

```json
{
  "student_name": "Avery Example",
  "student_dob": "2004-06-15",
  "student_phone": "5551234567",
  "student_email": "avery@example.com",
  "student_course": "Computer Science",
  "student_address": "Example City",
  "student_enrolDate": "2023-09-01"
}
```

`student_name`, `student_dob`, and `student_email` are required. The other fields are optional; phone numbers, when provided, must contain 10 characters. Dates use the `YYYY-MM-DD` format.

The AI endpoint accepts a JSON body such as:

```json
{
  "question": "How many students are enrolled in Computer Science?"
}
```

It requires `GOOGLE_API_KEY` to be configured.
