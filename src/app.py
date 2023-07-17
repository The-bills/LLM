from utilis import *
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

position_response = get_completion_from_prompt(postion_perfect_description)

cv_read_list = file_reader()
messages_vals = messages(cv_analysis_system_message, cv_analysis_user_message, cv_read_list)
final_response = get_completion_from_messages(messages=messages_vals)
print(final_response)
