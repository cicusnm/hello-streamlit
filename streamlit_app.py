import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')
#inter
st.sidebar.title('interactive Data Explorer')
st.title("is")
st.header('markdown')
st.markdown('markdown2')
st.subheader('subheader')
st.caption('cca')
st.code('x=2020')
st.latex('fdsf')

st.image("kid.jpg")
st.audio("audio.mp3")
st.video("video.mp4")

st.checkbox('yes')
st.button('click')
st.selectbox('pick your gender', ['male', 'female'])