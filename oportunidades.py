import json
import pandas as pd
from langchain.tools import BaseTool

class TodasOportunidades(BaseTool):
    name = "TodasOportunidades"
    description = "Lists all available opportunities with their requirements and areas."

    def _run(self, input: str) -> str:
        try:
            df = pd.read_csv("documentos/oportunidades.csv")
            oportunidades = df.to_dict(orient="records")
            return json.dumps(oportunidades, ensure_ascii=False)
        except Exception as e:
            return f"Error loading opportunities: {str(e)}"
