#%%
import streamlit as st


st.set_page_config(page_title="Analyse per onderwerp", page_icon="📚")

src = 'https://jvanelteren.github.io/blog/posts/moties2023/2023-09-11-kamermoties_topics.html'
st.components.v1.iframe(src, width=800, height=5500, scrolling=False)