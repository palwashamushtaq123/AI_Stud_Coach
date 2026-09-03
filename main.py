from pathlib import Path

import os
from dotenv import load_dotenv
import google.generativeai as genai

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from run import generate_gemini_content



# --------------------------------------------------
# 1. Project folder path
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

print(f"BASE DIR: {BASE_DIR}")


# --------------------------------------------------
# 2. Load environment variables
# --------------------------------------------------

load_dotenv()

Google_API_KEY = os.getenv("GOOGLE_API_KEY")

if not Google_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY was not found in .env file.")


# --------------------------------------------------
# 3. Configure Gemini
# --------------------------------------------------

genai.configure(api_key=Google_API_KEY)


# --------------------------------------------------
# 4. Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="AI Student Coach",
    version="1.0.0",
)


# --------------------------------------------------
# 5. Make CSS / JavaScript accessible
# --------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)


# --------------------------------------------------
# 6. HTML templates folder
# --------------------------------------------------

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


# --------------------------------------------------
# 7. API input structure
# --------------------------------------------------

class Studycoachinput(BaseModel):

    name: str = Field(
        min_length=1,
        description="Student name"
    )
    
    subject: str = Field(
        min_length=1,
        description="Subject"
    )
    
    weak_topics: str = Field(
        min_length=1,
        description="Weak Topics"
    )
    
    days_left: int = Field(
        gt=0,
        description="Days Left in Exams"
    )
    
    hours: float = Field(
        gt=0,
        description="Study Hours Per Day"
    )
    
    skill_level: str = Field(
        min_length=1,
        description="Skill Level"
    )
    
    technique: str = Field(
        description="Prompting technique"
    )

# --------------------------------------------------
# 8. Home page
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "model_version": "Gemini",
        }
    )


# --------------------------------------------------
# 9. Health check
# --------------------------------------------------

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model_status": "ready",
        "model": "Gemini",
    }

# --------------------------------------------------
# 11. Study Coach endpoint
# --------------------------------------------------

@app.post("/studyplan")
def analyze_studycoach(data: Studycoachinput):

    try:

        student_info = {
            "name": data.name,
            "subject": data.subject,
            "weak_topics": data.weak_topics,
            "days_left": data.days_left,
            "hours": data.hours,
            "skill_level": data.skill_level
        }
        
        result = generate_gemini_content(
            student_info,
            data.technique
        )

        return {
            "student_name": data.name,
            "subject": data.subject,
            "weak_topics": data.weak_topics,
            "days_left": data.days_left,
            "hours": data.hours,
            "skill_level": data.skill_level,
            "technique": data.technique,
            "study_plan": result,
            "model_version": "Gemini",
        }

    except Exception as e:

        return {
            "error": str(e)
        }