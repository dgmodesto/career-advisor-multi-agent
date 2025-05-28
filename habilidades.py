from langchain.tools import BaseTool

class HabilidadesTecnicas(BaseTool):
    name = "HabilidadesTecnicas"
    description = "Extrai habilidades do candidato a partir dos dados."

    def _run(self, input: str) -> str:
        return "Habilidades técnicas identificadas com sucesso."
