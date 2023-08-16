import streamlit as st
from streamlit_lottie import st_lottie
import base64

def main():
    #display gif
    file_ = open("assets/gif_home.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    with st.container():
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="hello_gif" height=250>',
            unsafe_allow_html=True,
        )
        subcol1, subcol2, subcol3, subcol4, subcol5 = st.columns([.2,.5,.5,.5,6])
        with subcol2:
            st.markdown('<a href="https://github.com/leticiacamposv/"><button type="submit" style="background-color:transparent;border:none"><img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/eada014d-bf37-420a-8f2e-f8b9239a576d/dg4rbot-72af04cc-3f15-4a83-b885-040c7a694d2a.png/v1/fill/w_32,h_32/github_11_32_by_holiefake_dg4rbot-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzIiLCJwYXRoIjoiXC9mXC9lYWRhMDE0ZC1iZjM3LTQyMGEtOGYyZS1mOGI5MjM5YTU3NmRcL2RnNHJib3QtNzJhZjA0Y2MtM2YxNS00YTgzLWI4ODUtMDQwYzdhNjk0ZDJhLnBuZyIsIndpZHRoIjoiPD0zMiJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.aWJbh9p9F7bS9Apw4czYDnHUoapm8d8Re_gSvqO35zM" width="32" height="32" alt="buttonpng" border="0" /></button><a>', unsafe_allow_html=True)
        with subcol3:
            st.markdown('<a href="https://www.linkedin.com/in/leticia-campos-valente"><button type="submit" style="background-color:transparent;border:none"><img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/eada014d-bf37-420a-8f2e-f8b9239a576d/dg4rcg1-7afbcfea-33b0-4bd1-9faa-69ce3a7e98bf.png/v1/fill/w_50,h_50/icons8_linkedin_50_by_holiefake_dg4rcg1-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTAiLCJwYXRoIjoiXC9mXC9lYWRhMDE0ZC1iZjM3LTQyMGEtOGYyZS1mOGI5MjM5YTU3NmRcL2RnNHJjZzEtN2FmYmNmZWEtMzNiMC00YmQxLTlmYWEtNjljZTNhN2U5OGJmLnBuZyIsIndpZHRoIjoiPD01MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.2RE-oA5yhbCkvFVQV6ozCrs4r5mGs8XkoWpwW-bBNmc" width="32" height="32" alt="buttonpng" border="0" /></button><a>', unsafe_allow_html=True)
        with subcol4:
            st.markdown('<a href="https://www.udemy.com/user/leticia-campos-valente/"><button type="button" style="background-color:transparent;border:none"><img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/eada014d-bf37-420a-8f2e-f8b9239a576d/dg4rd23-eee3d6c8-5e6e-4372-a8e0-ccb82d56f465.png/v1/fill/w_987,h_810/pngaaa_com_3866524_by_holiefake_dg4rd23-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTA1MCIsInBhdGgiOiJcL2ZcL2VhZGEwMTRkLWJmMzctNDIwYS04ZjJlLWY4YjkyMzlhNTc2ZFwvZGc0cmQyMy1lZWUzZDZjOC01ZTZlLTQzNzItYThlMC1jY2I4MmQ1NmY0NjUucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.UjuM0aywxIOUpdZRYtjzlnenadcepVqmUFsb-2K_5wc" width="39" height="32" alt="buttonpng" border="0" /></button><a>', unsafe_allow_html=True)
        with subcol5:
            st.markdown('<a href="mailto:leticiacamposv@hotmail.com"><button type="button" style="background-color:transparent;border:none"><img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/eada014d-bf37-420a-8f2e-f8b9239a576d/dg4rey9-74818533-e121-45f2-bd11-eb8b7ff03121.png/v1/fill/w_50,h_50/icons8_nova_mensagem_50_by_holiefake_dg4rey9-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTAiLCJwYXRoIjoiXC9mXC9lYWRhMDE0ZC1iZjM3LTQyMGEtOGYyZS1mOGI5MjM5YTU3NmRcL2RnNHJleTktNzQ4MTg1MzMtZTEyMS00NWYyLWJkMTEtZWI4YjdmZjAzMTIxLnBuZyIsIndpZHRoIjoiPD01MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.4-qZmDYzpQ6e4Cx7QJ87oYUe3V0Cq_omSf8K2dc1bOE" width="39" height="32" alt="buttonpng" border="0" /></button><a>', unsafe_allow_html=True)
        
        st.markdown("""---""")
        
        col1, col2 = st.columns([2,1])

        with col1:
            st.title('Sobre mim')  
            st.write('')

            st.write('Olá! Sou Data Scientist e Engenheira de Machine Learning com quase 4 anos de experiência em análise de dados e mais de 2 anos de experiência em produção e monitoramento de modelos preditivos e análises usando estatística avançada. Meu objetivo é ajudar as empresas na exploração dos dados e extração de insights para a tomada de melhores decisões de negócio. Apaixonada por dados, tenho sede por aprendizado contínuo e uma mente muito curiosa e criativa. Como especialista em deploy de modelos em nuvem, minhas produções atuam com melhor escalabilidade, confiabilidade e segurança, providas em maioria em serviços de cloud como GCP e AWS. Além disso, ofereço sempre a melhor solução possível por meio de testes extensivos, controle e bom tratamento de grandes escalas de dados.')
            

        with col2:
            st_lottie('https://lottie.host/a4df3066-0865-487d-823d-6b84b0bac650/D5OvF5jMMG.json', key="dsgirl", height=400)


    
    # with st.echo():
    #     st_lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
    
if __name__ == "__main__":
    st.set_page_config(page_title="Leticia Portfólio", page_icon="🎈", layout="wide")
    main()