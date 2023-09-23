#%%
import streamlit as st


st.set_page_config(page_title="Ontwikkeling door de jaren", page_icon="📚")

src = 'https://jvanelteren.github.io/blog/posts/moties2023/2023-08-26-kamermotieseda.html'
st.components.v1.iframe(src, width=800, height=5500, scrolling=True)