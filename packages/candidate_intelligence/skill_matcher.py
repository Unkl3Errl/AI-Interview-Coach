class SkillMatcher:


    def analyze(self, candidate, job):

        strengths = []
        gaps = []


        for skill in job.required_skills:

            found = False

            for candidate_skill in candidate.skills:

                if skill.lower() in candidate_skill.lower():
                    found = True


            if found:
                strengths.append(skill)

            else:
                gaps.append(skill)


        return {
            "strengths": strengths,
            "development_areas": gaps
        }