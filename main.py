import streamlit as st
from newsscrapper import newsNDTV
from newsscrapper import IndiaToday

st.title("News Collection App")

st.image("title.jpg",use_column_width=True)

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
    st.header("Instruction")
    st.markdown('''
    - first inst
    - second inst
    ''')

    selWebsite = st.selectbox('Select the Website',['newsNDTV','IndiaToday','News18'])
    websiteImages = {'newsNDTV':'NDTV.png','IndiaToday':'indiatoday.jpg','News18':'news18breakingnews.webp'}
    st.image(websiteImages.get(selWebsite))
    st.subheader('Click here for collect News')
    
    start = st.button('Collect News')
    if start:
        data = newsNDTV()
        st.text(data)

        for news in data:
            st.subheader(news.get('heading'))
            st.subheader(news.get('summary'))
            st.subheader(news.get('src'))
            st.subheader(news.get('image'))
            st.subheader(news.get('link'))

        data = IndiaToday()
        st.text(data)

        for news in data:
            st.subheader(news.get('heading'))
            st.subheader(news.get('summary'))
            st.subheader(news.get('link'))
            
            st.subheader(news.get('image'))



options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()