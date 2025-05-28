from langchain.tools import BaseTool


class PerfilPsicologico(BaseTool):
    name = "PerfilPsicologico"
    description = "Analisa o perfil psicológico do candidato."

    def _run(self, input: str) -> str:
        # Idealmente, conecte com LLM aqui para análise real.
        return "O candidato apresenta perfil psicológico tipo INFJ - Advogado."
