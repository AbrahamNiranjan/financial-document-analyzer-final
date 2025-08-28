
# Financial Document Analyzer

## Project Overview
An AI-powered system for financial document analysis, built with **CrewAI** and **FastAPI**.  
It accepts a PDF financial report, processes it through multiple agents (Analyst, Verifier, Investment Advisor, Risk Assessor), and delivers structured investment recommendations and risk insights.

## Getting Started

### 1. Clone the Repository
```sh
git clone https://github.com/AbrahamNiranjan/financial-document-analyzer.git
cd financial-doc-analyzer
```

### 2. Create a Virtual Environment (Recommended)

```sh
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```sh
pip install -r requirement.txt
```

### 4. Configure Environment

Create a `.env` file and include your OpenAI API key:

```sh
OPENAI_API_KEY=your_api_key_here
```

## Running the Server

Start the FastAPI application with **Uvicorn**:

```sh
uvicorn main:app --reload
```

The server will be available at:
**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

## API Documentation

### Health Check

**GET /**

```json
{
  "message": "Financial Document Analyzer API is running"
}
```

### Analyze Financial Document

**POST /analyze**

Form-data:

* `file` → PDF financial document
* `query` → (optional) Custom query, e.g., `"Summarize risks in this report"`

**Example Request:**

```sh
curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "file=@sample_report.pdf" \
  -F "query=Summarize the risks and opportunities"
```

**Example Response:**

```json
{
  "status": "success",
  "query": "Summarize the risks and opportunities",
  "analysis": "... AI generated response ...",
  "file_processed": "sample_report.pdf"
}
```

## Bug Fixes

| File               | Problem                                               | Resolution                                                         |
| ------------------ | ----------------------------------------------------- | ------------------------------------------------------------------ |
| `agents.py`        | `llm = llm` not defined                               | Added `LLM(model="gpt-4")` initialization                          |
| `agents.py`        | Used `tool=` instead of `tools=`                      | Fixed parameter usage                                              |
| `main.py`          | Function name conflict (`analyze_financial_document`) | Endpoint renamed to `analyze_file`                                 |
| `task.py`          | Wrong agent used for `verification`                   | Corrected to use `verifier`                                        |
| `task.py`          | Incorrect `tool=` usage                               | Updated everywhere to `tools=`                                     |
| `tools.py`         | Missing `Pdf` import                                  | Replaced with `PyPDFLoader` from `langchain`                       |
| `tools.py`         | Async function used in sync context                   | Converted to `@staticmethod`                                       |
| `tools.py`         | No file existence validation                          | Added file existence check with error handling                     |
| `requirements.txt` | Incorrect name & dependency conflicts                 | Renamed to `requirements.txt`, reduced to minimal working packages |

## Agents and Tasks

### Agents

* **Financial Analyst** → Extracts financial insights from documents.
* **Verifier** → Validates the file as a genuine financial report.
* **Investment Advisor** → Suggests potential investment opportunities.
* **Risk Assessor** → Identifies risks highlighted in the document.

---

### Tasks

* **analyze\_financial\_document** → Produces an overall analysis of the report.
* **investment\_analysis** → Provides investment strategies based on financial data.
* **risk\_assessment** → Generates a risk profile of the market or company.
* **verification** → Ensures the uploaded file is valid and processable.

## Contact Details

* **Name:** Abraham Niranjan Isaac
* **Email:** [abrahamisaac74692@gmail.com](mailto:abrahamisaac74692@gmail.com)
* **GitHub:** [https://github.com/AbrahamNiranjan](https://github.com/AbrahamNiranjan)


---
