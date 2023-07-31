import os
import openai
from dotenv import load_dotenv, find_dotenv
import PyPDF2
from langchain.llms import OpenAI

_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

# convert this function to use LangChain
def get_completion_from_prompt(prompt, 
                               model="gpt-3.5-turbo",
                               temperature=0.0,
                               max_tokens=1500):
    
    #messages = [{"role": "user", "content": prompt}]
    #response = openai.ChatCompletion.create(
    #    model=model,
    #    messages=messages,
    #    temperature=temperature,
    #    max_tokens=max_tokens 
    #)
    #return response.choices[0].message["content"]
    llm = OpenAI(model_name=model, temperature=temperature, max_tokens=max_tokens)
    return llm.predict(prompt)


def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0.0, 
                                 max_tokens=1500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]


def list_to_string(inputed_list):
    final_string = '[' + ', '.join(map(repr, inputed_list)) + ']'
    return final_string

def file_reader(folder_path=os.getenv('FOLDER_PATH')):
    content_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                page_list = []
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    content = page.extract_text()
                    page_list.append(content)
                content_list.append(page_list)
    return [item for sublist in content_list for item in sublist]


def messages(system_message, user_message, assistant_message):
    messages = [  
    {'role':'system',
    'content': system_message},   
    {'role':'user',
    'content': user_message},  
    {'role':'assistant',
    'content': assistant_message},   
    ]
    return messages
