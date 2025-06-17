# 📧 OutreachXpert

**OutreachXpert** is a Streamlit-powered application that helps fresh graduates craft personalized and professional cold emails to recruiters. It uses the Groq API to extract job-specific details and generate customized outreach messages based on a user’s portfolio and the job description.

---

## 🚀 Features

- 🔗 Scrapes job descriptions from provided job posting URLs  
- 🤖 Uses LLMs (via Groq API) to extract job information and skills  
- 📂 Matches required skills with projects from your personal portfolio  
- 📨 Generates professional, personalized cold emails to recruiters  
- 🧼 Cleans job descriptions for better processing and relevance  
- 🧠 Perfect for job seekers wanting to stand out with targeted messaging

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Web interface  
- [LangChain](https://www.langchain.com/) – Framework for LLM chaining  
- [Groq API](https://groq.com/) – LLM backend for fast, cost-effective inference  
- Python – Backend logic  
- Custom modules:
  - `chains.py`: Handles LLM logic and email generation
  - `portfolio.py`: Manages portfolio data and matches
  - `utils.py`: Utility functions (e.g., cleaning HTML/text)

---

## 📂 Project Structure

📁 outreachxpert/
├── main.py # Streamlit app entry point
├── chains.py # LLM logic and job/email processing
├── portfolio.py # User portfolio and skill matcher
├── utils.py # Content cleaning utilities
└── README.md # Project documentation


---

## 🧪 How It Works

1. Input a job URL (e.g., from Amazon Jobs or LinkedIn).
2. Enter your full name.
3. Click **Submit**.
4. The app:
   - Scrapes and cleans the job page.
   - Extracts relevant information and skills using the Groq LLM.
   - Matches required skills with your portfolio.
   - Outputs a markdown-formatted cold email tailored to the job.

---

## 🧰 Installation
### Clone the repository
   ```bash
     git clone https://github.com/your-username/outreachxpert.git
     cd outreachxpert
   ```
### Install the dependencies
  ```bash
    pip install -r requirements.txt
  ```
### Set your Groq API key
  #### Create a .env file or set the environment variable:
   ```plaintext
     GROQ_API_KEY=your_groq_api_key
  ```
### Run the app
   ```bash
     streamlit run main.py
   ```


