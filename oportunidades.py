from langchain.tools import BaseTool

class TodasOportunidades(BaseTool):
    name = "TodasOportunidades"
    description = "Lista todas as oportunidades disponíveis."

    def _run(self, input: str) -> str:
        return "Oportunidades listadas com sucesso."
