import streamlit as st
from agente import AgenteCarreiraIA

def main():
    st.set_page_config(
        page_title="Career Advisor Multi-Agent",
        page_icon="🎯",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.title("🎯 Career Advisor Multi-Agent")
    st.markdown(
        """
        Welcome to the intelligent career recommendation system!  
        Ask about professional profiles, career areas and skills, and get personalized AI-based recommendations.
        """
    )
    st.divider()

    agente = AgenteCarreiraIA()

    pergunta = st.text_area("Type your question here:", height=120)

    if st.button("Send"):
        if pergunta.strip():
            with st.spinner("Analyzing your question..."):
                resposta = agente.executar(pergunta)
            st.markdown("### Answer:")
            st.success(resposta)
        else:
            st.warning("Please type a question to continue.")

if __name__ == "__main__":
    main()
