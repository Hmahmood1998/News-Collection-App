import streamlit as st
from newsscrapper import newsNDTV
from newsscrapper import IndiaToday

st.title("News Collection App")

st.image("title.jpg", use_column_width=True)

sidebar = st.sidebar

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

    selWebsite = st.selectbox('Select the Website', ['newsNDTV', 'IndiaToday','IndianExpress','BusinessStandard','News18'])
    websiteImages = {'newsNDTV': 'NDTV.png','IndiaToday': 'indiatoday.jpg','IndianExpress':'expresslogo.jpg','BusinessStandard':'bslogo.png','News18': 'news18breakingnews.webp'}
    st.image(websiteImages.get(selWebsite))
    st.subheader('Click here for collect News')

    start = st.button('Collect News')
    if start:
        data = newsNDTV()
        st.text(data)

        for news in data:
            c1, c2 = st.columns([1,2.5])
            c1.markdown(f"![]({news.get('image')})")
            c2.markdown(f"""
                #### {news.get('heading')}
                {news.get('summary')}
                {news.get('src')}
                [View Full Article]({news.get('link')})
            """)

        data = IndiaToday()
        st.text(data)

        for news in data:
            c1, c2 = st.columns([1,2])
            c1.markdown(f"![]({news.get('image')})")
            c2.markdown(f"""
                #### {news.get('heading')}
                {news.get('summary')}
                
                [View Full Article]({news.get('link')})
            """)
            
            


options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()
