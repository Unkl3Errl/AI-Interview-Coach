class ExperienceMapper:


    def match(self, candidate, job):

        matches = []


        for required in job.required_skills:

            for skill in candidate.skills:

                if required.lower() in skill.lower():

                    matches.append(
                        {
                            "skill": required,
                            "evidence":
                            "Candidate has related professional experience"
                        }
                    )


        return matches