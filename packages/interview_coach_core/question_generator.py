class QuestionGenerator:

    def generate(self, job_profile):

        questions = []

        for skill in job_profile.required_skills:
            questions.append(
                f"Describe your experience working with {skill}."
            )

        questions.extend([
            "Tell me about yourself.",
            "Describe a difficult technical problem you solved.",
            "Why are you interested in this role?"
        ])

        return questions