import streamlit as st
from newsscrapper import newsNDTV

st.title("News ")
st.image("omeg.png", use_column_width=True)

sidebar=st.sidebar

sidebar.title("User Options")

def introduction():
    st.markdown("""
        ## Heading Level 2
        - Feature 1
        - Feature 2
        - Feature 3
    """)

    c1, c2 = st.columns(2)

    c1.header("Column 1 Content")
    c2.header("Column 2 Content")


def execute():
    st.subheader('project working here')
    start = st.button('Collect News')
    if start:
        data = newsNDTV()
        st.text(data)

        for news in data:
            st.subheader(news.get('heading'))
            st.subheader(news.get('summary'))



options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()