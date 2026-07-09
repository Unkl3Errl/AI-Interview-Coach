from pathlib import Path


class ResumeParser:


    def extract_text(self, filename):

        path = Path(filename)


        if path.suffix.lower() == ".txt":

            return path.read_text(
                encoding="utf-8"
            )


        if path.suffix.lower() == ".docx":

            from docx import Document


            document = Document(
                filename
            )


            paragraphs = []


            for paragraph in document.paragraphs:

                if paragraph.text.strip():

                    paragraphs.append(
                        paragraph.text
                    )


            return "\n".join(
                paragraphs
            )


        raise ValueError(
            "Unsupported file type"
        )