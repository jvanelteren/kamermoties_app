import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome bij de StemVinder! 👋")

st.sidebar.success("Kies je tool")

st.markdown(
    """
    De afgelopen regeringsperiode zijn er meer dan 6000 moties behandeld. Links zie je een aantal verschillende tools om deze te analyseren.
    
    **👈 Kies je tool om te beginnen!**
    ### Dank gaat uit naar

    * :sun_with_face: [Tweede Kamer Open Data Portaal](https://opendata.tweedekamer.nl/) voor het beschikbaar maken van de moties
    * :sun_with_face: Dimo Angelov, bedenker en ontwikkelaar van [Top2Vec](https://github.com/ddangelov/Top2Vec)
    
    Heb je een inzichten opgedaan, feedback op de app of wil je contact opnemen? Neem even contact op, bijvoorbeeld via [LinkedIn](https://www.linkedin.com/in/jessevanelteren/).

    [![License: Creative Commons Naamsvermelding-GelijkDelen 4.0 Internationaal-licentie](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/3.0/) 2023 Jesse van Elteren
    """
)