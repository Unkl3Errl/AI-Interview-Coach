from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class QuestionRecord:
    question: str
    answer: str = ""
    score: float = 0.0
    feedback: str = ""


@dataclass
class InterviewSession:

    candidate_name: str

    job_title: str

    company: str

    started: datetime = field(default_factory=datetime.now)

    completed: bool = False

    questions: list[QuestionRecord] = field(default_factory=list)