from crewai import Task
from agents import financial_analyst
from tools import ReadFinancialDocumentTool

read_tool = ReadFinancialDocumentTool()

analyze_financial_document = Task(
    description="Read the financial document at {path} and answer the user query: {query}",
    expected_output="Clear financial insights based on the document.",
    agent=financial_analyst,
    tools=[read_tool],
    async_execution=False,
)

investment_analysis = Task(
    description="Read the financial document at {path} and answer the user query: {query}",
    expected_output="Investment insights based on financial data.",
    agent=financial_analyst,
    tools=[read_tool],
    async_execution=False,
)

risk_assessment = Task(
    description="Read the financial document at {path} and create a risk assessment.",
    expected_output="Risk assessment report.",
    agent=financial_analyst,
    tools=[read_tool],
    async_execution=False,
)

verification = Task(
    description="Read the financial document at {path} and verify its contents.",
    expected_output="Verification result.",
    agent=financial_analyst,
    tools=[read_tool],
    async_execution=False,
)
