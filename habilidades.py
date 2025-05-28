import json
import pandas as pd
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain.tools import BaseTool

class HabilidadesEntrada(BaseModel):
    texto: str = Field(description="Nome do candidato para busca no banco de dados.")

class HabilidadesTecnicas(BaseTool):
    name = "HabilidadesTecnicas"
    description = "Extrai habilidades técnicas a partir do nome do candidato."

    def _run(self, input: str) -> str:
        entrada = HabilidadesEntrada(texto=input)
        try:
            dados = pd.read_csv("documentos/candidatos.csv")
            dados["NOME"] = dados["NOME"].str.lower()
            candidato = dados[dados["NOME"] == entrada.texto.lower()]
            if candidato.empty:
                return f"Nenhum candidato encontrado com o nome: {entrada.texto}"
            descricao = candidato.iloc[0]["DESCRICAO"]
            # Aqui você pode aplicar um modelo LLM ou regex no futuro
            habilidades = ["Python", "SQL", "Machine Learning"]  # Simulação
            return f"Habilidades extraídas para {entrada.texto}: {', '.join(habilidades)}"
        except Exception as e:
            return f"Erro ao processar as habilidades: {str(e)}"
