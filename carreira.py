from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.tools import BaseTool
import os
import json

class DadosDoCandidato(BaseModel):
    perfil: str = Field(description="Candidate profile, e.g. 'communicative', 'analytical', etc.")

class RecomendadorDeCarreira(BaseTool):
    name = "RecomendadorDeCarreira"
    description = "Suggests career areas based on the candidate's profile."

    def _run(self, input: str) -> str:
        llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
        parser = JsonOutputParser(pydantic_object=DadosDoCandidato)

        template = PromptTemplate(
            template="""Below is a description of a candidate's profile.
Extract the candidate's main profile and generate a suggested career area.
-----------------
{input}
-----------------
Output format:
{formato_saida}
""",
            input_variables=["input"],
            partial_variables={"formato_saida": parser.get_format_instructions()}
        )

        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input": input})
        perfil = resposta.perfil.lower().strip()

        return f"Suggested area based on the profile '{perfil}': Information Technology."
