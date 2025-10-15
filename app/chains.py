import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, groq_api_key="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")

    def extract_jobs(self, cleaned_text):
        prompt_template = PromptTemplate.from_template(
            """
                ### SCRAPED TEXT FROM WEBSITE:
                {page_data}
                ### INSTRUCTION:
                The scraped text is from the career's page of a website.
                Your job is to extract the job postings and return them in JSON format containing the 
                following keys: `role`, `experience`, `skills` and `description`.
                Only return the valid JSON.
                ### VALID JSON (NO PREAMBLE):    
                """
        )
        chain_extract = prompt_template | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Anurag, a junior technical associate at Galaxy Office Automation Pvt Ltd. Galaxy is one of the largest IT Infrastructure solution providers in India, offering cutting edge Data Center, Cloud, Networking, Cyber Security and Modern Workplaces solutions 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of Galaxy 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Galaxy's portfolio: {link_list}
            Remember you are Anurag, JTA at Galaxy. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )

        chain_mail = prompt_email | self.llm
        res = chain_mail.invoke({'job_description': str(job), 'link_list': links})
        return res.content

# if __name__ == "__main__":
#     print(os.getenv("GROQ_API_KEY"))