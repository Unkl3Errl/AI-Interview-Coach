from dataclasses import dataclass, field
from typing import List


@dataclass
class Experience:
    company: str
    role: str
    accomplishments: List[str] = field(default_factory=list)
    technologies: List[str] = field(default_factory=list)


@dataclass
class CandidateProfile:
    name: str = ""
    professional_summary: str = ""

    skills: List[str] = field(default_factory=list)

    certifications: List[str] = field(default_factory=list)

    experiences: List[Experience] = field(default_factory=list)