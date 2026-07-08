from pathlib import Path


class ResumeParser:

    def extract_text(self, filename):

        path = Path(filename)

        if path.suffix == ".txt":
            return path.read_text()

        if path.suffix == ".docx":
            from docx import Document

            doc = Document(filename)

            return "\n".join(
                p.text for p in doc.paragraphs
            )

        raise ValueError(
            "Unsupported resume format"
        )