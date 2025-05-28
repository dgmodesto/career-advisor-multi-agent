from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.tools import BaseTool
import os
import json

class DadosDoCandidato(BaseModel):
    perfil: str = Field(description="Perfil do candidato, como por exemplo 'comunicativo', 'analítico', etc.")

class RecomendadorDeCarreira(BaseTool):
    name = "RecomendadorDeCarreira"
    description = "Sugere áreas de atuação com base no perfil do candidato."

    def _run(self, input: str) -> str:
        llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
        parser = JsonOutputParser(pydantic_object=DadosDoCandidato)

        template = PromptTemplate(
            template="""A seguir está uma descrição do perfil de um candidato.
Extraia o perfil principal do candidato e gere uma sugestão de área de atuação.
-----------------
{input}
-----------------
Formato de saída:
{formato_saida}
""",
            input_variables=["input"],
            partial_variables={"formato_saida": parser.get_format_instructions()}
        )

        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input": input})
        perfil = resposta.perfil.lower().strip()

        return f"Área sugerida com base no perfil '{perfil}': Tecnologia da Informação."
