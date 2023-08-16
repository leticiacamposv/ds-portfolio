import streamlit as st
import webbrowser
st.set_page_config(page_title="Projetos", page_icon="🎈", layout="wide")

st.markdown("# Clique em um projeto para ser redirecionado ao github")

st.markdown("""<style>body {
  display: flex;
  height:100vh;
  align-items: center;
  justify-content: center;
  background-color: black;
}

.button {
  color: #6b3c81;
  border: 6px solid #6b3c81;
  border-radius:15px;
  padding: 15px 25px;
  font-size: 30px;
  top: 50%;
  left: 50%;
  font-family: tahoma;
  letter-spacing:5px;
  cursor: pointer;
  font-weight: bold;
  filter: drop-shadow(0 0 15px #6b3c81) drop-shadow(0 0 50px #6b3c81) contrast(2) brightness(2);
  transition: .5s;
}

.button:hover {
  color: black;
  background-color: #6b3c81;
  filter: drop-shadow(0 0 20px #6b3c81) contrast(2) brightness(2);
}
            
</style>""", unsafe_allow_html=True)

st.markdown('<div class="button"><a style="color: white;text-decoration: none;" href="https://github.com/leticiacamposv/exemplo-risco-credito">Credit risk prediction</a></div>', unsafe_allow_html=True)
st.markdown('<div class="button"><a style="color: white;text-decoration: none;" href="https://github.com/leticiacamposv/neural-network-raw">Neural Network from Scratch</a></div>', unsafe_allow_html=True)
st.markdown('<div class="button"><a style="color: white;text-decoration: none;" href="https://github.com/leticiacamposv/data-wrangling-exercise">Data Wrangling Exercise</a></div>', unsafe_allow_html=True)
st.markdown('<div class="button"><a style="color: white;text-decoration: none;" href="https://github.com/leticiacamposv/star_wars_sql_challenge">Star Wars SQL Challenge</a></div>', unsafe_allow_html=True)
st.markdown('<div class="button"><a style="color: white;text-decoration: none;" href="https://github.com/leticiacamposv/pacote-desafios-pythonicos">Pacote de Desafios Pythonicos</a></div>', unsafe_allow_html=True)
st.markdown('<div class="button"><a style="color: white;text-decoration: none;" href="https://github.com/leticiacamposv/hardware-test-ml">ML Hardware Testing</a></div>', unsafe_allow_html=True)