from crewai.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader
import os

class ReadFinancialDocumentTool(BaseTool):
    name: str = "Read Financial Document"
    description: str = "Reads a PDF from a local path and returns extracted text."

    def _run(self, path: str) -> str:
        if not os.path.exists(path):
            raise FileNotFoundError(f"PDF not found at: {path}")

        loader = PyPDFLoader(path)
        pages = loader.load()

        full_report = ""
        for page in pages:
            content = page.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report




