from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document

app = FastAPI(title="Financial Document Analyzer")


def run_crew(query: str, file_path: str):
    """Run CrewAI with the uploaded PDF path + user query"""
    financial_crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential,
    )

    result = financial_crew.kickoff({
        "query": query,
        "path": file_path
    })

    return result


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}


@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights"),
):
    """Analyze financial document and provide recommendations"""

    file_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        # Save uploaded PDF
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Validate query
        if not query or not query.strip():
            query = "Analyze this financial document for investment insights"

        # Run crew
        response = run_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query.strip(),
            "analysis": str(response),
            "file_processed": file.filename,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")

    finally:
        # Cleanup file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
