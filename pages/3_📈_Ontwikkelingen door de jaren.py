#%%
import streamlit as st


st.set_page_config(page_title="Ontwikkeling door de jaren", page_icon="📈")

src = 'https://jvanelteren.github.io/blog/posts/energy/2023-05-22-prices.html'
st.components.v1.iframe(src, width=800, height=5500, scrolling=False)