import streamlit as st
from page_scraper import Scraper

categories = [ "Things to Do",
                "Whats On",
                "Eat Drink",
                "Shopping",
                "Beyond York",
                "Explore",
                "Blog",
                "Your Visit" ]

with st.form("scrape form", clear_on_submit=True):
    url = st.text_input("Input Webpage URL to be scraped")
    category = st.selectbox("Category", options=categories)
    bt1 = st.form_submit_button("Scrape")

    if bt1 and 'scraper' not in st.session_state:
        st.session_state.scraper = Scraper(category, url)
        if st.session_state.scraper.status == 200:
            st.session_state.scraper.getPageInfo()

with st.form("save json form", clear_on_submit=True):
    if 'scraper' in st.session_state:
        st.text(f"Category: {st.session_state.scraper.category}")
        st.text(f"Business: {st.session_state.scraper.business}")
        st.text_area("Scraped Text", st.session_state.scraper.text, height=300)
        st.text(f"Save file in {st.session_state.scraper.output_file}")
        save_file = st.form_submit_button("Save as JSON")      
        if save_file:
            st.text(st.session_state.scraper.savePageInfo()) 
            st.session_state.pop('scraper')   
            
    
