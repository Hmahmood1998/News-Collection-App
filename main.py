import streamlit as st
from newsscrapper import newsNDTV, IndiaToday, IndianExpress, BusinessStandard
import pandas as pd
from datetime import datetime
import os

st.title("News Collection App")

st.image("title.jpg", use_column_width=True)

sidebar = st.sidebar

sidebar.title("User Options")


def introduction():
    st.markdown("""
        ## Latest News
    
    Name : Hamid Mahamood
    \nQualification : Bachelor of Technology(B.Tech)
    \nStream : Technical 
    \nUniversity : JNTUH
    \nLocation : Hyderabad, INDIA
    \nThis Project is collection of news from India's Top Website. Here we use various libraries of Python for making this project.
        
        - The Libraries I used in Project are:
            BeautifulSoup Explore here
            requests Explore here
            datetime Explore here  
            Pandas Explore here
            os Explore here
            Streamlit Explore here
        
        - Their Following Tasks are Implemented in the Project:
            To read the Latest News of India's Top News Websites.
            I collect the News by using Web scrapping tool which is most valuable tool for extract
            the huge amount of Data that is constantly generated online.
            You can also Archive the News Data in csv format.
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

    selWebsite = st.selectbox('Select the Website', [
                              'newsNDTV', 'IndiaToday', 'IndianExpress', 'BusinessStandard'])
    websiteImages = {'newsNDTV': 'NDTV.png', 'IndiaToday': 'indiatoday.jpg',
                     'IndianExpress': 'expresslogo.jpg', 'BusinessStandard': 'bslogo.png', }
    
    st.image(websiteImages.get(selWebsite))
    st.subheader('Click here to latest News')

    start = st.checkbox('View News')
    data = []
    if start:
        if selWebsite == 'newsNDTV':
            data = newsNDTV()
        elif selWebsite == 'IndiaToday':
            data = IndiaToday()
        elif selWebsite == 'IndianExpress':
            data=IndianExpress()
        elif selWebsite == 'BusinessStandard':
            data=BusinessStandard()
        # elif selWebsite == 'News18':
        #     data=News18()
        # showText = st.checkbox('View in Text Form')
        # if showText:
        # st.write(data)
        for news in data:
            c1, c2 = st.columns([1, 2.5])
            if news.get('image'):
                c1.markdown(f"![]({news.get('image')})")
            c2.markdown(f"""
                #### {news.get('heading')}
            """)
            c2.text(f"{news.get('summary')}")
            if news.get('src'):
                c2.text(f"{news.get('src')}")
            c2.markdown(f"[View Full Article]({news.get('link')})")

        save_news = st.checkbox('Archive News')
        if save_news:
            try:
                pd.DataFrame(data).to_csv(f'archived_news/{selWebsite}_{datetime.now().strftime("%d-%m-%Y_%H-%M")}.csv')
            except Exception as e:
                print(e)
                st.error('Error Saving News')

def view_archived():

    news_file_list = os.listdir('archived_news')
    selFile = st.selectbox('Select File to View', news_file_list)

    if selFile:

        csv_data = pd.read_csv('archived_news/'+selFile)
        st.dataframe(csv_data)

        with open('archived_news/'+selFile, 'rb') as f:
            st.download_button('Download CSV', f, 'text/csv')


options = ['Project Introduction', 'Execution', 'View Archived News']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()
elif selOption == options[2]:
    view_archived()
