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
        Bem-vindo ao sistema de recomendação de carreira inteligente!  
        Faça perguntas sobre perfis profissionais, áreas, habilidades, e receba recomendações personalizadas com base em inteligência artificial.
        """
    )
    st.divider()

    agente = AgenteCarreiraIA()

    pergunta = st.text_area("Digite sua pergunta aqui:", height=120)

    if st.button("Enviar"):
        if pergunta.strip():
            with st.spinner("Analisando sua pergunta..."):
                resposta = agente.executar(pergunta)
            st.markdown("### Resposta:")
            st.success(resposta)
        else:
            st.warning("Por favor, digite uma pergunta para continuar.")

if __name__ == "__main__":
    main()
