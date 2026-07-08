from dataclasses import dataclass, field
from typing import List


@dataclass
class Experience:

    company: str
    title: str
    dates: str

    description: List[str]

    skills: List[str] = field(default_factory=list)

    technologies: List[str] = field(default_factory=list)

    achievements: List[str] = field(default_factory=list)


@dataclass
class Education:

    school: str

    degree: str

    dates: str


@dataclass
class Resume:

    name: str

    summary: str

    experiences: List[Experience]

    education: List[Education]

    skills: List[str]