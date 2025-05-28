from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_tools_agent, create_react_agent
from langchain import hub
from langchain.agents import Tool
from langchain.agents import AgentExecutor
import os
from langchain_openai import ChatOpenAI
from carreira import RecomendadorDeCarreira
from habilidades import HabilidadesTecnicas
from psicologia import PerfilPsicologico
from oportunidades import TodasOportunidades

class AgenteCarreiraIA:
    def __init__(self):
        llm = ChatOpenAI(model="gpt-4o",
                         api_key=os.getenv("OPENAI_API_KEY"))

        recomendador_carreira = RecomendadorDeCarreira()
        habilidades_tecnicas = HabilidadesTecnicas()
        perfil_psicologico = PerfilPsicologico()
        todas_oportunidades =  TodasOportunidades()

        self.tools = [
            Tool(
                name=recomendador_carreira.name,
                func=recomendador_carreira.run,
                description=recomendador_carreira.description,
                return_direct=False
            ),
            Tool(
                name=habilidades_tecnicas.name,
                func=habilidades_tecnicas.run,
                description=habilidades_tecnicas.description,
                return_direct=False
            ),
            Tool(
                name=perfil_psicologico.name,
                func=perfil_psicologico.run,
                description=perfil_psicologico.description,
                return_direct=False
            ),
            Tool(
                name=todas_oportunidades.name,
                func=todas_oportunidades.run,
                description=todas_oportunidades.description,
                return_direct=False
            ),
        ]
        prompt = hub.pull("hwchase17/react")
        self.agent = create_react_agent(llm, self.tools, prompt)
        
    def executar(self, pergunta: str) -> str:
        # return self.agent.invoke({"input": pergunta})["output"]
        executor = AgentExecutor(agent=self.agent,
                        tools=self.tools,
                        verbose=True)
        resposta = executor.invoke({"input" : pergunta})    
        return resposta["output"]