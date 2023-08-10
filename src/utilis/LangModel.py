import utilis.prompts as pm
from langchain.prompts import ChatPromptTemplate
from utilis.prompts import *
from langchain.llms import OpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from dotenv import load_dotenv, find_dotenv
import warnings
warnings.filterwarnings('ignore')
_ = load_dotenv(find_dotenv())


class LangModel:
    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.0,request_timeout=120, max_tokens=1500)

    def find_name(resume):
        prompt = find_name_from_cv.format(resume=resume)
        # response = LangModel.llm(prompt)
        return LangModel.llm(prompt)

    def describe_position(name: str, description: str):
        prompt = describe_position.format(name=name, description=description, n=5)
        output = LangModel.llm(prompt)
        return output
    
    def rate_cv(name: str, description: str, characteristics: str, cv: str):
        parsed_characteristics = "\n".join(characteristics)
        prompt = pm.rate_cv.format(name=name, description=description, characteristics=parsed_characteristics, cv=cv)
        output = LangModel.llm(prompt)
        return CommaSeparatedListOutputParser().parse(output)

