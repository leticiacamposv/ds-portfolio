import streamlit as st
import webbrowser
st.set_page_config(page_title="Projetos", page_icon="🎈", layout="wide")

st.markdown("# Clique em um projeto para ser redirecionado ao github")
# st.markdown("""<style>div.stButton>button {
#   align-items: center;
#   height: 200px;
#   width: 200px;          
#   background-image: linear-gradient(144deg,#AF40FF, #5B42F3 50%,#00DDEB);
#   border: 0;
#   border-radius: 8px;
#   box-shadow: rgba(151, 65, 252, 0.2) 0 15px 30px -5px;
#   box-sizing: border-box;
#   color: #FFFFFF;
#   display: flex;
#   font-family: Phantomsans, sans-serif;
#   font-size: 20px;
#   justify-content: center;
#   line-height: 1em;
#   max-width: 100%;
#   min-width: 140px;
#   padding: 3px;
#   text-decoration: none;
#   user-select: none;
#   -webkit-user-select: none;
#   touch-action: manipulation;
#   white-space: nowrap;
#   cursor: pointer;
# }

# div.stButton > button:active,
# div.stButton > button:hover {
#   outline: 0;
# }

# div.stButton > button span {
#   background-color: rgb(5, 6, 45);
#   padding: 16px 24px;
#   border-radius: 6px;
#   width: 100%;
#   height: 100%;
#   transition: 300ms;
# }

# div.stButton > button:hover span {
#   background: none;
# }

# @media (min-width: 768px) {
#     div.stButton > button {
#     font-size: 24px;
#     min-width: 196px;
#   }
# }</style>""", unsafe_allow_html=True)

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