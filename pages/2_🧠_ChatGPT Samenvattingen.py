import streamlit as st
import random
import pandas as pd
import altair as alt
from urllib.error import URLError
from annotated_text import annotated_text
from PIL import Image

@st.cache_data
def load_df():
    filename = 'data/final_summaries.pickle'
    with open(filename, "rb") as f:
        df = pd.read_pickle(f)
        df = df.sample(frac=1)
        return df['Partij'].unique(), df


def get_score():
    score = 0
    for partij, choice, color in zip(st.session_state['test_partijen'], choices, colors):
        if partij in choice:
            additional_score = 1 / len(choice)
            score += additional_score
            with color:
                annotated_text(("Deze had je goed", str(round(additional_score*10)) + ' punten', "#afa"))
        else:
            with color:
                annotated_text((f"Deze had je niet goed, het was {partij}", '0 punten', "#faa"))
    return round(score * 10)


def get_test(seen):
    if len(st.session_state.get('seen',set())) >= 15:
        st.session_state['seen'] = set()
    num = 5 if len(st.session_state.get('seen',set())) < 10 else 6
    st.session_state['test_partijen'] = random.sample([p for p in partijen if p not in seen], num)
    st.session_state['test_summaries'] = [df[df['Partij']==tp]['Summary'].iloc[0] for tp in st.session_state['test_partijen']]
    
    st.session_state['seen'] = st.session_state.get('seen', set()) | set(st.session_state['test_partijen'])

st.set_page_config(page_title="ChatGPT Samenvattingen", page_icon="🧠")
partijen, df = load_df()

if 'seen' not in st.session_state:
    get_test(set())
    
st.markdown("# ChatGPT Samenvattingen")

st.write(
    """Met ChatGPT kan je samenvatten waar de partijen voor staan aan de hand van de moties die ze hebben ingediend. Lukt het je om de juiste partij bij de samenvatting te vinden?"""
)
i = Image.open('data/moties.jpg')
st.image(i , use_column_width=True)


 
col1, col2 = st.columns(2)

with col1:
    answers =  st.button('Klik hier als je direct de antwoorden wilt zien')
        
with col2:
    e = st.empty()
    
if answers:
    for _, (partij, summary, n_moties, motie_samenvattingen) in df.iterrows():
        st.subheader(partij)
        st.write(summary)  
        st.divider()

else:
    try:
        # st.dataframe(df)
        # choices = []
        # colors = []
        partijen, df = load_df()
        choices = []
        colors = []
        # for _, (partij, summary, n_moties, motie_samenvattingen) in df[:2].iterrows():
        for partij, summary in zip(st.session_state['test_partijen'], st.session_state['test_summaries']):
            # st.write(st.session_state['seen'])
            
            choices.append(st.multiselect(
                "Welke partij is dit?", partijen, key=partij
            ))
            colors.append(st.empty())
            st.write(summary)
            st.divider()
        
        
        if st.button('Wat is mijn score?'):
            

            score = get_score()
            if score < 10:
                message = 'Nog even oefenen'
            elif score < 30:
                message = 'Goed gedaan'
            else:
                message = 'Topper!'

            
            if len(st.session_state['seen']) <= 10:
                get_test(st.session_state['seen'])
            else:
                get_test(set())
            
            if score >= 30:
                st.balloons()
            with e:
                print(len(st.session_state['seen']),st.session_state['seen'] )
                if len(st.session_state['seen'])  == 5:
                    if st.button('Je hebt alle partijen gehad. Nog een keer?'):
                        st.experimental_rerun()

                else:
                    if st.button('Klik hier voor de volgende partijen'):
                        st.experimental_rerun()
            final_message = st.empty()
            with final_message:
                st.success(f'Je score is {score} punten. {message}')

       
        
        

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )
