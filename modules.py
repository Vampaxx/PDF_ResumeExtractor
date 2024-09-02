import os
import re
from datetime import date
from typing import Union,Optional,List,Dict
from pydantic import BaseModel,ValidationError,Field,Extra,validator,field_validator,EmailStr,constr

from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import JsonOutputParser


def load_pdf(file_path:str):

  file_loader   = PyPDFLoader(file_path)
  pages         = file_loader.load_and_split()
  text = "\n\n".join(doc.page_content for doc in pages)
  return text

def path_processing(file_path: str) -> str:
  
    directory     = os.path.dirname(file_path)
    old_file_name = os.path.basename(file_path)
    new_file_name = old_file_name.replace("-", "_").replace(" ", "_")
    new_file_path = os.path.join(directory, new_file_name)

    os.rename(file_path, new_file_path)
    return new_file_path



class PersonalInformation(BaseModel):
    """Model for storing personal information"""
    name        : str
    email       : EmailStr
    phone_number: Optional[str] = None

    @field_validator('phone_number')
    def validate_phone_number(cls, number):
        if number:
            # Regular expression pattern to validate phone number
            pattern = r'^(?:\+?\d{1,3}-\d{10}|\d{10})$'
            if not re.match(pattern, number):
                raise ValueError("Invalid phone number format.")
        return number
    
class ProjectTitle(BaseModel):
  title: list[str] = Field(default=[],max_items=6,description="List of project titles")

class Details(BaseModel):
  project_titles : ProjectTitle
  personal_info  : PersonalInformation


def parsing():

  parser  = JsonOutputParser(pydantic_object=Details)
  prompt  = PromptTemplate(
      template = """
      You are a data extraction and summarization expert.Given the following text, perform the following tasks:
      1. Summarize the text and extract all the project titles (include if any freelancing work is present). Ensure that project titles are returned in a list format.
      2. Extract the following details: name, email, and phone number.
      Return the result in JSON format with the following structure:

        1. "project_titles": "<extracted project title 1>", "<extracted project title 2>", ...,
        2. "name"  : "<name of candidate>",
        3. "email" : "<email address>",
        4. "phone_number": "<extracted phone number>"
        5. "experience":"summarize" in 25 words.

      {format_instructions}
      Context:{context}
      """,
      input_variables   = ["context"],
      partial_variables = {"format_instructions": parser.get_format_instructions()},)
  
  return parser,prompt
  
