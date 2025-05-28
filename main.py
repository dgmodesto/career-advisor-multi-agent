from agente import AgenteCarreiraIA

if __name__ == "__main__":
    agente = AgenteCarreiraIA()
    pergunta = input("Faça sua pergunta sobre carreira: ")
    resposta = agente.executar(pergunta)
    print(resposta)
