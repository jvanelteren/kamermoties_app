import streamlit as st
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
    for partij, choice, color in zip(partijen, choices, colors):
        if partij in choice:
            additional_score = 1 / len(choice)
            score += additional_score
            with color:
                annotated_text(("Deze had je goed", str(round(additional_score*10)) + ' punten', "#afa"))
        else:
            with color:
                annotated_text((f"Deze had je niet goed, het was {partij}", '0 punten', "#faa"))
    return round(score * 10)

st.set_page_config(page_title="ChatGPT Samenvattingen", page_icon="🧠")

st.markdown("# ChatGPT Samenvattingen")

st.sidebar.header("ChatGPT Samenvattingen")

st.write(
    """Met ChatGPT kan je samenvatten waar de partijen voor staan aan de hand van de moties die ze hebben ingediend. Lukt het je om de juiste partij bij de samenvatting te vinden?"""
)
i = Image.open('data/moties.jpg')
st.image(i , use_column_width=True)
if st.button('Klik hier als je direct de antwoorden wilt zien'):
    partijen, df = load_df()
    # st.dataframe(df)
    for _, (partij, summary, n_moties, motie_samenvattingen) in df.iterrows():
        st.subheader(partij)
        st.write(summary)
       
        st.divider()


else:
    
    try:
        partijen, df = load_df()
        # st.dataframe(df)
        choices = []
        colors = []
        for _, (partij, summary, n_moties, motie_samenvattingen) in df.iterrows():
            choices.append(st.multiselect(
                "Welke partij is dit?", partijen, key=partij
            ))
            colors.append(st.empty())
            st.write(summary)
        
            st.divider()
        
        
        if st.button('Wat is mijn score?'):
            score = get_score()
            if score < 20:
                message = 'Nog even oefenen'
            elif score < 30:
                message = 'Goed gedaan'
            else:
                message = 'Topper!'
            st.success(f'Je score is {score} punten')
            st.write(message)
            if score < 5:
                st.snow()
            else:
                st.balloons()
        else:
            st.write('')
        
        

    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )