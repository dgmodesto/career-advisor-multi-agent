import json
import pandas as pd
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain.tools import BaseTool

class HabilidadesEntrada(BaseModel):
    texto: str = Field(description="Candidate name used to search the database.")

class HabilidadesTecnicas(BaseTool):
    name = "HabilidadesTecnicas"
    description = "Extracts technical skills from the candidate's name."

    def _run(self, input: str) -> str:
        entrada = HabilidadesEntrada(texto=input)
        try:
            dados = pd.read_csv("documentos/candidatos.csv")
            dados["NOME"] = dados["NOME"].str.lower()
            candidato = dados[dados["NOME"] == entrada.texto.lower()]
            if candidato.empty:
                return f"No candidate found with the name: {entrada.texto}"
            descricao = candidato.iloc[0]["DESCRICAO"]
            # An LLM or regex could be applied here in the future
            habilidades = ["Python", "SQL", "Machine Learning"]  # Simulated
            return f"Skills extracted for {entrada.texto}: {', '.join(habilidades)}"
        except Exception as e:
            return f"Error processing skills: {str(e)}"
