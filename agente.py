from langchain.agents import create_openai_tools_agent
from langchain_openai import ChatOpenAI
from carreira import RecomendadorDeCarreira
from habilidades import HabilidadesTecnicas
from psicologia import PerfilPsicologico
from oportunidades import TodasOportunidades

class AgenteCarreiraIA:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o")
        self.tools = [
            RecomendadorDeCarreira(),
            HabilidadesTecnicas(),
            PerfilPsicologico(),
            TodasOportunidades()
        ]
        self.agent = create_openai_tools_agent(self.llm, self.tools)

    def executar(self, pergunta: str) -> str:
        return self.agent.invoke({"input": pergunta})["output"]
