from langchain.tools import BaseTool

class PerfilPsicologico(BaseTool):
    name = "PerfilPsicologico"
    description = "Analisa o perfil psicológico do candidato."

    def _run(self, input: str) -> str:
        return "Perfil psicológico avaliado como INFJ."
