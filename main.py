import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv


from modules import load_pdf,parsing,Details,path_processing



class ResumeProcessor:
    def __init__(self, file_path: str):
        self.file_path  = file_path
        self.model_name = "llama3-8b-8192"
        self.api_key    = self.load_groq_api_key()
        self.llm        = self.initialize_llm()

    def load_groq_api_key(self) -> str:
        """Load the Groq API key from environment variables."""
        load_dotenv()
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            raise ValueError("GROQ_API_KEY is not set in the environment variables.")
        return api_key

    def initialize_llm(self):
        """Initialize the LLM using the Groq API."""
        return ChatGroq(model       = self.model_name,
                        temperature = 0,
                        api_key     = self.api_key)

    def process_resume(self):
        """Process the resume PDF and return the parsed results."""
        parser, prompt  = parsing()
        sample          = load_pdf(self.file_path)

        chain           = prompt | self.llm | parser
        result          = chain.invoke({"context": sample})

        return result
    

if __name__ == "__main__":
    extractor = ResumeProcessor(file_path="uploaded_pdf\Arjun_ML_engineer_1.pdf")
    result = extractor.process_resume()
    print(result)


