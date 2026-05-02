from agents.data_ingestion import DataIngestionAgent
from agents.long_reasoning import LongReasoningAgent
from agents.report_generation import ReportGenerationAgent
from memory.company_memory import CompanyMemory

class ResearchPipeline:
    def run(self, company: str):
        docs = DataIngestionAgent(company).run()
        memory = CompanyMemory(company).load()

        signals = LongReasoningAgent(docs, memory).run()
        report = ReportGenerationAgent(company, signals).run()

        with open(f"report_{company}.md", "w", encoding="utf-8") as f:
            f.write(report)