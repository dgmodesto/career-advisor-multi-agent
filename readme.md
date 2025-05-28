---

# 💼 career-advisor-multi-agent

Sistema inteligente que recomenda carreiras ideais com base em **habilidades técnicas**, **experiências profissionais**, **interesses pessoais** e **perfil psicológico**, utilizando **LangChain**, **OpenAI GPT-4o** e **multi-agentes**.

## 🧠 Visão Geral

Este projeto usa uma arquitetura orientada a agentes para simular um processo de aconselhamento profissional. A IA analisa dados do candidato (armazenados em `.csv`) e sugere áreas e cargos ideais, cruzando habilidades, experiências e perfis com oportunidades disponíveis.

## 🛠️ Tecnologias Utilizadas

* Python 3.10+
* [LangChain](https://www.langchain.com/)
* [OpenAI GPT-4o](https://platform.openai.com/docs/models/gpt-4o)
* Streamlit (versão com front-end)
* dotenv
* pandas

---

## 📁 Estrutura do Projeto

```
career-advisor-multi-agent/
│
├── .env                       # Chaves de API (OpenAI)
├── README.md
├── main.py                    # Execução principal (CLI)
├── streamlit_app.py           # Interface web com Streamlit
│
├── agente.py                  # Montagem do agente principal
├── carreira.py                # Ferramenta de recomendação de carreira
├── habilidades.py             # Ferramenta de leitura de habilidades
├── psicologia.py              # Ferramenta de leitura de perfil psicológico
├── oportunidades.py           # Ferramenta de leitura de vagas
│
├── documentos/
│   ├── candidatos.csv         # Dados dos candidatos
│   └── oportunidades.csv      # Banco de oportunidades/vagas
```

---

## 🔐 Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/career-advisor-multi-agent.git
cd career-advisor-multi-agent
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar

### Modo 1: Linha de Comando

```bash
python main.py
```

Você poderá fazer perguntas como:

* "Qual carreira ideal para Joana?"
* "Carlos é melhor para marketing ou produto?"
* "Compare Joana e Carlos para vaga de Cientista de Dados."

---

### Modo 2: Interface Web com Streamlit

```bash
streamlit run streamlit_app.py
```

A interface será aberta no navegador. Você poderá escolher um candidato e ver as recomendações de carreira automaticamente.

---

## 🧪 Dados de Exemplo

### `documentos/candidatos.csv`

```csv
NOME,HABILIDADES,EXPERIENCIAS,INTERESSES,TESTE_PSI
Joana,"Python,SQL,Análise","2 anos como Analista","Dados,Ensino","INFJ"
Carlos,"Design,UX,Adobe","1 ano como Estagiário","Criação,Produtos","ENFP"
```

### `documentos/oportunidades.csv`

```csv
CARGO,AREA,REQUISITOS,PESO_INTERESSE,PESO_HABILIDADES
Cientista de Dados,TI,"Python,SQL",0.4,0.6
UX Designer,Design,"UX,Adobe",0.5,0.5
```

---

## 🤖 Como Funciona

1. **Ferramentas** (Tools) são carregadas com os dados do candidato.
2. O **agente LangChain** é montado com raciocínio baseado em ferramentas (`OpenAIFunctionsAgent` ou `ReActAgent`).
3. A pergunta do usuário é analisada e o agente orquestra o uso das ferramentas para compor a resposta final.

---

## ✅ Funcionalidades

* Recomendações personalizadas
* Suporte a múltiplos candidatos
* Interface amigável (CLI ou Web)
* Explicações baseadas em perfil psicológico e técnico

---

## 📌 Melhorias Futuras

* Integração com APIs de vagas reais (ex: LinkedIn, Glassdoor)
* Chatbot em tempo real com memória
* Ajuste de pesos por aprendizado de máquina

---

## 📄 Licença

MIT License

---
