from dataclasses import dataclass, field
from typing import List


@dataclass
class CandidateProfile:

    name: str = ""

    skills: List[str] = field(
        default_factory=list
    )

    summary: str = ""

    experiences: List[str] = field(
        default_factory=list
    )