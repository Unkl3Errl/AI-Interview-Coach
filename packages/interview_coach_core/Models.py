from dataclasses import dataclass, field
from typing import List


@dataclass
class CandidateProfile:
    name: str = ""
    skills: List[str] = field(default_factory=list)
    experience: List[str] = field(default_factory=list)
    certifications: List[str] = field(default_factory=list)
    summary: str = ""


@dataclass
class JobProfile:
    title: str = ""
    company: str = ""
    required_skills: List[str] = field(default_factory=list)
    responsibilities: List[str] = field(default_factory=list)


@dataclass
class InterviewAnswer:
    question: str
    response: str
    score: float = 0
    feedback: str = ""