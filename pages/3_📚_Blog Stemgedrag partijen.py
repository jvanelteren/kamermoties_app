#%%
import streamlit as st


st.set_page_config(page_title="Stemgedrag partijen", page_icon="📚")

src = 'https://jvanelteren.github.io/blog/posts/moties2023/2023-08-26-kamermotieseda.html'
st.components.v1.iframe(src, width=740, height=7000, scrolling=False)
# html = """
# <style>
#     #myFrame { width:device-width; height:100%; }
# </style>

#   <iframe
#       src="https://jvanelteren.github.io/blog/posts/moties2023/2023-08-26-kamermotieseda.html"

#       frameborder="0"
#       id="myFrame">
#   </iframe>
# """
# st.components.v1.html(html, width=None, height=None, scrolling=False)
