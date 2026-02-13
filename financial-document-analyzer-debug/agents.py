import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from tools import ReadFinancialDocumentTool

llm = LLM(model="gpt-4o-mini")

# Tool instance (IMPORTANT)
pdf_tool = ReadFinancialDocumentTool()

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Read the document at {path} and answer: {query}",
    verbose=True,
    memory=True,
    backstory="You are an expert financial analyst who provides clear and data-driven insights.",
    tools=[pdf_tool],   
    llm=llm,
    max_iter=2,
    allow_delegation=False
)



