from packages.interview_coach_core.models import JobProfile


class JobAnalyzer:


    def analyze(self, job_text):

        profile = JobProfile()

        text = job_text.lower()


        # Basic title detection

        if "architect" in text:
            profile.title = "Data Architect"

        elif "analyst" in text:
            profile.title = "Data Analyst"

        elif "developer" in text:
            profile.title = "Developer"

        else:
            profile.title = "Unknown"


        skill_patterns = {

            "PYTHON": [
                "python"
            ],

            "SQL": [
                "sql",
                "database",
                "t-sql"
            ],

            "HL7": [
                "hl7",
                "health level seven"
            ],

            "HEALTHCARE": [
                "healthcare",
                "clinical",
                "medical"
            ],

            "DATA ARCHITECTURE": [
                "data architecture",
                "data modeling",
                "enterprise data"
            ],

            "POWER BI": [
                "power bi",
                "powerbi"
            ],

            "CLOUD": [
                "azure",
                "aws",
                "cloud"
            ],

            "ETL": [
                "etl",
                "data pipeline",
                "data migration"
            ]

        }


        for skill, keywords in skill_patterns.items():

            for keyword in keywords:

                if keyword in text:

                    profile.required_skills.append(
                        skill
                    )

                    break


        return profile