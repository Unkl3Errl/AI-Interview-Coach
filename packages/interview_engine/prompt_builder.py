class PromptBuilder:

    def build(
        self,
        candidate,
        job,
        memory
    ):

        history = ""

        for item in memory.recent():

            history += (
                f"{item['speaker']}: "
                f"{item['text']}\n"
            )

        prompt = f"""

You are an experienced interviewer.

Candidate:
{candidate.name}

Skills:
{candidate.skills}

Required Skills:
{job.required_skills}

Conversation:
{history}

Ask only ONE interview question.

"""

        return prompt