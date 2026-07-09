class SkillMatcher:


    def compare(
        self,
        candidate,
        job
    ):

        candidate_skills = set(
            candidate.skills
        )


        required_skills = set(
            job.required_skills
        )


        matched = (
            candidate_skills
            &
            required_skills
        )


        missing = (
            required_skills
            -
            candidate_skills
        )


        if required_skills:

            score = int(
                len(matched)
                /
                len(required_skills)
                *
                100
            )

        else:

            score = 0


        return {

            "score": score,

            "matched": list(
                matched
            ),

            "missing": list(
                missing
            )
        }