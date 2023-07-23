from utilis import *
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from position import Position
import dics.default_position as dp

cv_read_list = file_reader()

position = Position() \
    .set_name(dp.name) \
    .set_description(dp.description) \
    .gen_characteristics()

for cv in cv_read_list:
    print(position.rate_cv(cv))



#position_response = get_completion_from_prompt(postion_perfect_description)
#print(position_response)
#messages_vals = messages(cv_analysis_system_message, cv_analysis_user_message, cv_read_list)
#final_response = get_completion_from_messages(messages=messages_vals)
#print(final_response)
