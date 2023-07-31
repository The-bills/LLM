import llm.prompts as prompts
from langchain.llms import OpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser

class Llm:
    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.0, max_tokens=1500)

    def find_name(resume: str):
        prompt = prompts.find_name.format(resume=resume)
        return Llm.llm(prompt)

    def describe_position(name: str, description: str):
        prompt = prompts.describe_position.format(name=name, description=description, n=5)
        output = Llm.llm(prompt)
        return CommaSeparatedListOutputParser().parse(output)
    
    def rate_cv(name: str, description: str, characteristics: str, cv: str):
        parsed_characteristics = "\n".join(characteristics)
        prompt = prompts.rate_cv.format(name=name, description=description, characteristics=parsed_characteristics, cv=cv)
        output = Llm.llm(prompt)
        return CommaSeparatedListOutputParser().parse(output)
        