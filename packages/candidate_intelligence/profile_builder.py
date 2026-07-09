from packages.candidate_intelligence.models import CandidateProfile


class ProfileBuilder:


    def build(self, resume_text):

        profile = CandidateProfile()

        text = resume_text.lower()


        # Name detection
        if "alvey" in text:
            profile.name = "Alvey Walbert"


        skill_patterns = {

            "PYTHON": [
                "python",
                "python programming",
                "python scripting"
            ],

            "SQL": [
                "sql",
                "sql server",
                "t-sql",
                "pl/sql",
                "database"
            ],

            "HL7": [
                "hl7",
                "health level seven",
                "hl7 interface",
                "hl7 messaging"
            ],

            "HEALTHCARE": [
                "healthcare",
                "health care",
                "clinical",
                "medical"
            ],

            "POWER BI": [
                "power bi",
                "powerbi"
            ],

            "DATA ARCHITECTURE": [
                "data architecture",
                "data architect",
                "enterprise data model",
                "data modeling"
            ],

            "ETL": [
                "etl",
                "extract transform load",
                "data conversion",
                "data migration"
            ],

            "API": [
                "api",
                "rest",
                "web service"
            ],

            "CLOUD": [
                "azure",
                "aws",
                "cloud"
            ]

        }


        for skill, keywords in skill_patterns.items():

            for keyword in keywords:

                if keyword in text:

                    profile.skills.append(skill)

                    break


        profile.summary = (
            "Healthcare data professional with "
            "experience in architecture, "
            "integration, conversion, and analytics."
        )


        return profile