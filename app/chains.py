
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links, user_name):
        prompt_email = PromptTemplate.from_template(
            """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are {user_name}, a recent college graduate with a degree in [Your Degree]. You're proactively reaching out to companies in your field of interest, even if they haven't advertised specific job openings. Your task is to write a concise, compelling cold email to introduce yourself and inquire about potential entry-level opportunities.
        
        In your cold email:
        
        1.Briefly introduce yourself, mentioning your recent graduation and degree.
        2.Express your genuine interest in the company and explain why you're reaching out to them specifically.
        3.Highlight 2-3 of your most relevant skills or experiences that align with the company's work.
        4.Mention any notable projects, internships, or achievements that showcase your potential.
        5.If applicable, include a link to your online portfolio or LinkedIn profile.
        6.Inquire about any entry-level positions or internship opportunities that might be available.
        7.Offer to provide additional information or to schedule a brief call to discuss further.
        8.Keep the email concise, professional, and tailored to the specific company.
        9.Have correct punctuation and grammar, also use good formatting and escape sequences.
        Remember, you are {user_name}, a new graduate initiating contact. Focus on your potential, eagerness to learn, and how you could contribute to the company.
        Do not provide a preamble.
        COLD EMAIL (NO PREAMBLE):
        ''' 
        """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links, "user_name": user_name})
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
