from .models import CandidateProfile, Experience


class ProfileBuilder:


    def build(self, resume_text):

        profile = CandidateProfile()

        text = resume_text.lower()


        if "alvey" in text:
            profile.name = "Alvey Walbert"


        keywords = [
            "python",
            "sql",
            "hl7",
            "healthcare",
            "data architecture",
            "data conversion",
            "etl",
            "power bi"
        ]


        for skill in keywords:
            if skill in text:
                profile.skills.append(skill.upper())


        profile.experiences = self.extract_experience(
            resume_text
        )


        return profile



    def extract_experience(self, text):

        experiences = []


        companies = [
            "SIU School of Medicine",
            "Galen Healthcare",
            "22nd Century Technologies",
            "LRS"
        ]


        for company in companies:

            if company.lower() in text.lower():

                experiences.append(
                    Experience(
                        company=company,
                        role="Relevant technical role"
                    )
                )


        return experiences