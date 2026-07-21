from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow requests from the HTML page
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Teacher's examples
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/greet")
def greet_user(name: str):
    return {"message": "Hello, " + name + "!"}


# Feedback model
class Feedback(BaseModel):
    student_name: str
    topic: str
    rating: int
    comment: str


# Feedback API
@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    return {
        "message": "Feedback submitted successfully!",
        "student_name": feedback.student_name,
        "topic": feedback.topic,
        "rating": feedback.rating,
        "comment": feedback.comment
    }