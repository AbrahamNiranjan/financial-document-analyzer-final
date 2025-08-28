## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools.tools.serper_dev_tool import SerperDevTool
from langchain.document_loaders import PyPDFLoader   # ✅ use LangChain’s loader

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool:
    @staticmethod
    def read_data_tool(path='data/sample.pdf'):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document text
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        loader = PyPDFLoader(path)
        docs = loader.load()

        full_report = ""
        for data in docs:
            content = data.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report.strip()

## Creating Investment Analysis Tool
class InvestmentTool:
    @staticmethod
    async def analyze_investment_tool(financial_document_data):
        # Process and analyze the financial document data
        processed_data = financial_document_data

        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1

        # TODO: Implement investment analysis logic here
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool:
    @staticmethod
    async def create_risk_assessment_tool(financial_document_data):
        # TODO: Implement risk assessment logic here
        return "Risk assessment functionality to be implemented"
