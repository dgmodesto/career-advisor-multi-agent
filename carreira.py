import json
from langchain.tools import BaseTool

class RecomendadorDeCarreira(BaseTool):
    name = "RecomendadorDeCarreira"
    description = "Sugere áreas de atuação com base no perfil do candidato."

    def _run(self, input: str) -> str:
        dados = json.loads(input)
        return f"Recomendação baseada no perfil: {dados.get('perfil', 'desconhecido')}"
