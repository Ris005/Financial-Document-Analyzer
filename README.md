<img width="1910" height="863" alt="image" src="https://github.com/user-attachments/assets/810e4c4c-8837-4ad9-9774-3e89a16687d3" />

#  Financial Document Analyzer  
**AI-Powered Investment Insight & Risk Assessment System**

---

##  Overview
The **Financial Document Analyzer** is an AI-powered web application that automates the analysis of financial PDF documents such as quarterly earnings, annual statements, and corporate updates.  

It leverages **Large Language Models (LLMs)** to interpret financial text and generate **structured investment insights** and **risk assessments**, reducing manual effort and improving decision-making speed.

---

##  Problem Statement
Manual financial document analysis is:
- Time-consuming  
- Inconsistent across analysts  
- Prone to human error  

This project solves these challenges by automating the extraction of financial metrics, performance evaluation, and risk assessment.

---

##  Objectives
- Automate financial document analysis  
- Extract structured insights from reports  
- Provide investment recommendations  
- Generate risk assessment summaries  
- Build a scalable API-driven architecture  

---

##  System Architecture
**Workflow:**
1. User uploads a financial PDF  
2. File is temporarily stored  
3. **CrewAI agent** reads the document using a custom tool  
4. **LLM** processes the extracted text  
5. Insights are returned as a **JSON response**  

**Pipeline:**  
`User → FastAPI Server → CrewAI Agent → LLM → Structured Insights`

---

##  Technologies Used
- **Python** – Backend programming  
- **FastAPI** – REST API framework  
- **CrewAI** – Multi-agent orchestration  
- **OpenAI / LLMs** – AI reasoning engine  
- **LangChain** – PDF parsing  
- **Uvicorn** – ASGI server  
- **python-multipart** – File upload handling  
- **dotenv** – Environment variable management  

---

##  Key Features
- Upload and process financial PDFs  
- Extract structured text from reports  
- AI-powered financial interpretation  
- Automated investment insights  
- Risk assessment generation  
- Clean, modular API architecture  
- Automatic file cleanup  

---

##  Challenges & Solutions
**Challenges:**  
- Tool validation errors in CrewAI  
- Pydantic model conflicts  
- Dependency installation issues  
- File upload handling errors  

**Solutions:**  
- Implemented proper Base Tool class  
- Fixed type annotations for Pydantic  
- Installed required dependencies  
- Designed structured file handling workflow  

---

##  Business Value
- Reduces analysis time significantly  
- Standardizes evaluation methodology  
- Improves decision-making speed  
- Scalable for enterprise use  
- Can integrate into fintech or investment platforms  

---

##  Future Enhancements
- Multi-agent architecture (Risk + Investment specialists)  
- Financial ratio computation engine  
- Vector database integration (RAG architecture)  
- Frontend dashboard (React-based)  
- Database storage for reports  
- Authentication & enterprise-grade security  

---

# Run the FastAPI server
uvicorn main:app --reload
