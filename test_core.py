from interview_coach_core import (
    ResumeParser,
    JobAnalyzer,
    QuestionGenerator
)


parser = ResumeParser()

resume = parser.extract_text(
    "data/resumes/Alvey Walbert CV Current.docx"
)

analyzer = JobAnalyzer()

job = analyzer.analyze(
    resume
)

generator = QuestionGenerator()

questions = generator.generate(job)

for q in questions:
    print(q)