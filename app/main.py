import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text): 
    st.title("📧 OutreachXpert")
    st.write("A tool that helps fresh graduates craft personalized, professional cold emails to potential employers and networking contacts.")
    
    # User inputs
    url_input = st.text_input("Enter a URL:", value="https://www.amazon.jobs/en/jobs/2802318/software-dev-engineer-iii-aws-payments")
    name_input = st.text_input("Enter Your Full Name: ")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                
                # Pass the user's name to the email generation function
                email = llm.write_mail(job, links, name_input)
                st.code(email, language='markdown')
        
        except Exception as e:
            st.error(f"An Error Occurred: {e}")



if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)