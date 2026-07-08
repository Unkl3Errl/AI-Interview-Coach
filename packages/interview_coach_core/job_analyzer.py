from .models import JobProfile


class JobAnalyzer:

    def analyze(self, text):

        profile = JobProfile()

        lines = text.splitlines()

        for line in lines:
            lower = line.lower()

            if "python" in lower:
                profile.required_skills.append("Python")

            if "sql" in lower:
                profile.required_skills.append("SQL")

            if "hl7" in lower:
                profile.required_skills.append("HL7")

        return profile