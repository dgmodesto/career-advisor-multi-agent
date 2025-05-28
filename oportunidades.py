import json
import pandas as pd
from langchain.tools import BaseTool

class TodasOportunidades(BaseTool):
    name = "TodasOportunidades"
    description = "Lista todas as oportunidades disponíveis com seus requisitos e áreas de atuação."

    def _run(self, input: str) -> str:
        try:
            df = pd.read_csv("documentos/oportunidades.csv")
            oportunidades = df.to_dict(orient="records")
            return json.dumps(oportunidades, ensure_ascii=False)
        except Exception as e:
            return f"Erro ao carregar oportunidades: {str(e)}"
