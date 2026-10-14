from langchain.tools import BaseTool


class PerfilPsicologico(BaseTool):
    name = "PerfilPsicologico"
    description = "Analyzes the candidate's psychological profile."

    def _run(self, input: str) -> str:
        # Ideally, connect an LLM here for a real analysis.
        return "The candidate has an INFJ psychological profile - Advocate."
